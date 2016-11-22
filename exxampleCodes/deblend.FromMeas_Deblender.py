#
# LSST Data Management System
# Copyright 2008-2015 AURA/LSST.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
import math
import numpy

import lsst.pex.config as pexConf
import lsst.pipe.base as pipeBase
import lsst.afw.math as afwMath
import lsst.afw.geom as afwGeom
import lsst.afw.geom.ellipses as afwEll
import lsst.afw.image as afwImage
import lsst.afw.detection as afwDet
import lsst.afw.table as afwTable

__all__ = 'SourceDeblendConfig', 'SourceDeblendTask'

class SourceDeblendConfig(pexConf.Config):

    edgeHandling = pexConf.ChoiceField(
        doc='What to do when a peak to be deblended is close to the edge of the image',
        dtype=str, default='ramp',
        allowed={
            'clip': 'Clip the template at the edge AND the mirror of the edge.',
            'ramp': 'Ramp down flux at the image edge by the PSF',
            'noclip': 'Ignore the edge when building the symmetric template.',
            }
        )

    strayFluxToPointSources = pexConf.ChoiceField(
        doc='When the deblender should attribute stray flux to point sources',
        dtype=str, default='necessary',
        allowed={
            'necessary': 'When there is not an extended object in the footprint',
            'always': 'Always',
            'never': ('Never; stray flux will not be attributed to any deblended child '
                      'if the deblender thinks all peaks look like point sources'),
            }
        )

    findStrayFlux = pexConf.Field(dtype=bool, default=True,
                                  doc='Find stray flux---flux not claimed by any child in the deblender.')

    assignStrayFlux = pexConf.Field(dtype=bool, default=True,
                                    doc='Assign stray flux to deblend children.  Implies findStrayFlux.')

    strayFluxRule = pexConf.ChoiceField(
        doc='How to split flux among peaks',
        dtype=str, default='trim',
        allowed = {
            'r-to-peak': '~ 1/(1+R^2) to the peak',
            'r-to-footprint': ('~ 1/(1+R^2) to the closest pixel in the footprint.  '
                               'CAUTION: this can be computationally expensive on large footprints!'),
            'nearest-footprint': ('Assign 100% to the nearest footprint (using L-1 norm aka '
                                  'Manhattan distance)'),
            'trim': ('Shrink the parent footprint to pixels that are not assigned to children')
            }
        )

    clipStrayFluxFraction = pexConf.Field(dtype=float, default=0.001,
                                          doc=('When splitting stray flux, clip fractions below '
                                               'this value to zero.'))
    psfChisq1 = pexConf.Field(dtype=float, default=1.5, optional=False,
                              doc=('Chi-squared per DOF cut for deciding a source is '
                                   'a PSF during deblending (un-shifted PSF model)'))
    psfChisq2 = pexConf.Field(dtype=float, default=1.5, optional=False,
                              doc=('Chi-squared per DOF cut for deciding a source is '
                                   'PSF during deblending (shifted PSF model)'))
    psfChisq2b = pexConf.Field(dtype=float, default=1.5, optional=False,
                               doc=('Chi-squared per DOF cut for deciding a source is '
                                    'a PSF during deblending (shifted PSF model #2)'))
    maxNumberOfPeaks = pexConf.Field(dtype=int, default=0,
                                     doc=("Only deblend the brightest maxNumberOfPeaks peaks in the parent"
                                          " (<= 0: unlimited)"))
    maxFootprintArea = pexConf.Field(dtype=int, default=1000000,
                                     doc=("Maximum area for footprints before they are ignored as large; "
                                          "non-positive means no threshold applied"))
    maxFootprintSize = pexConf.Field(dtype=int, default=0,
                                    doc=("Maximum linear dimension for footprints before they are ignored "
                                         "as large; non-positive means no threshold applied"))
    minFootprintAxisRatio = pexConf.Field(dtype=float, default=0.0,
                                          doc=("Minimum axis ratio for footprints before they are ignored "
                                               "as large; non-positive means no threshold applied"))
    notDeblendedMask = pexConf.Field(dtype=str, default="NOT_DEBLENDED", optional=True,
                                     doc="Mask name for footprints not deblended, or None")

    tinyFootprintSize = pexConf.RangeField(dtype=int, default=2, min=2, inclusiveMin=True,
                                      doc=('Footprints smaller in width or height than this value will '
                                           'be ignored; minimum of 2 due to PSF gradient calculation.'))

    propagateAllPeaks = pexConf.Field(dtype=bool, default=False,
                                      doc=('Guarantee that all peaks produce a child source.'))
    catchFailures = pexConf.Field(dtype=bool, default=False,
                                  doc=("If True, catch exceptions thrown by the deblender, log them, "
                                       "and set a flag on the parent, instead of letting them propagate up"))
    maskPlanes = pexConf.ListField(dtype=str, default=["SAT", "INTRP", "NO_DATA"],
                                   doc="Mask planes to ignore when performing statistics")
    maskLimits = pexConf.DictField(
        keytype = str,
        itemtype = float,
        default = {},
        doc = ("Mask planes with the corresponding limit on the fraction of masked pixels. "
               "Sources violating this limit will not be deblended."),
        )

## \addtogroup LSST_task_documentation
## \{
## \page SourceDeblendTask
## \ref SourceDeblendTask_ "SourceDeblendTask"
## \copybrief SourceDeblendTask
## \}

class SourceDeblendTask(pipeBase.Task):
    """!
    \anchor SourceDeblendTask_

    \brief Split blended sources into individual sources.

    This task has no return value; it only modifies the SourceCatalog in-place.
    """
    ConfigClass = SourceDeblendConfig
    _DefaultName = "sourceDeblend"

    def __init__(self, schema, peakSchema=None, **kwargs):
        """!
        Create the task, adding necessary fields to the given schema.

        @param[in,out] schema        Schema object for measurement fields; will be modified in-place.
        @param[in]     peakSchema    Schema of Footprint Peaks that will be passed to the deblender.
                                     Any fields beyond the PeakTable minimal schema will be transferred
                                     to the main source Schema.  If None, no fields will be transferred
                                     from the Peaks.
        @param[in]     **kwargs      Passed to Task.__init__.
        """
        pipeBase.Task.__init__(self, **kwargs)
        peakMinimalSchema = afwDet.PeakTable.makeMinimalSchema()
        if peakSchema is None:
            # In this case, the peakSchemaMapper will transfer nothing, but we'll still have one
            # to simplify downstream code
            self.peakSchemaMapper = afwTable.SchemaMapper(peakMinimalSchema, schema)
        else:
            self.peakSchemaMapper = afwTable.SchemaMapper(peakSchema, schema)
            for item in peakSchema:
                if item.key not in peakMinimalSchema:
                    self.peakSchemaMapper.addMapping(item.key, item.field)
                    # Because SchemaMapper makes a copy of the output schema you give its ctor, it isn't
                    # updating this Schema in place.  That's probably a design flaw, but in the meantime,
                    # we'll keep that schema in sync with the peakSchemaMapper.getOutputSchema() manually,
                    # by adding the same fields to both.
                    schema.addField(item.field)
            assert schema == self.peakSchemaMapper.getOutputSchema(), "Logic bug mapping schemas"
        self.addSchemaKeys(schema)

    def addSchemaKeys(self, schema):
        self.nChildKey = schema.addField('deblend_nChild', type=int,
                                         doc='Number of children this object has (defaults to 0)')
        self.psfKey = schema.addField('deblend_deblendedAsPsf', type='Flag',
                                      doc='Deblender thought this source looked like a PSF')
        self.psfCenterKey = afwTable.Point2DKey.addFields(schema, 'deblend_psfCenter',
                                         'If deblended-as-psf, the PSF centroid', "pixels")
        self.psfFluxKey = schema.addField('deblend_psfFlux', type='D',
                                           doc='If deblended-as-psf, the PSF flux')
        self.tooManyPeaksKey = schema.addField('deblend_tooManyPeaks', type='Flag',
                                               doc='Source had too many peaks; '
                                               'only the brightest were included')
        self.tooBigKey = schema.addField('deblend_parentTooBig', type='Flag',
                                         doc='Parent footprint covered too many pixels')
        self.maskedKey = schema.addField('deblend_masked', type='Flag',
                                         doc='Parent footprint was predominantly masked')

        if self.config.catchFailures:
            self.deblendFailedKey = schema.addField('deblend_failed', type='Flag',
                                                    doc="Deblending failed on source")

        self.deblendSkippedKey = schema.addField('deblend_skipped', type='Flag',
                                                doc="Deblender skipped this source")

        self.deblendRampedTemplateKey = schema.addField(
            'deblend_rampedTemplate', type='Flag',
            doc=('This source was near an image edge and the deblender used '
                 '"ramp" edge-handling.'))

        self.deblendPatchedTemplateKey = schema.addField(
            'deblend_patchedTemplate', type='Flag',
            doc=('This source was near an image edge and the deblender used '
                 '"patched" edge-handling.'))

        self.hasStrayFluxKey = schema.addField(
            'deblend_hasStrayFlux', type='Flag',
            doc=('This source was assigned some stray flux'))

        self.log.logdebug('Added keys to schema: %s' % ", ".join(str(x) for x in (
                    self.nChildKey, self.psfKey, self.psfCenterKey, self.psfFluxKey,
                    self.tooManyPeaksKey, self.tooBigKey)))

    @pipeBase.timeMethod
    def run(self, exposure, sources, psf):
        """!
        Run deblend().

        @param[in]     exposure Exposure to process
        @param[in,out] sources  SourceCatalog containing sources detected on this exposure.
        @param[in]     psf      PSF

        @return None
        """
        self.deblend(exposure, sources, psf)

    def _getPsfFwhm(self, psf, bbox):
        # It should be easier to get a PSF's fwhm;
        # https://dev.lsstcorp.org/trac/ticket/3030
        return psf.computeShape().getDeterminantRadius() * 2.35

    @pipeBase.timeMethod
    def deblend(self, exposure, srcs, psf):
        """!
        Deblend.

        @param[in]     exposure Exposure to process
        @param[in,out] srcs     SourceCatalog containing sources detected on this exposure.
        @param[in]     psf      PSF

        @return None
        """
        self.log.info("Deblending %d sources" % len(srcs))

        from lsst.meas.deblender.baseline import deblend

        # find the median stdev in the image...
        mi = exposure.getMaskedImage()
        statsCtrl = afwMath.StatisticsControl()
        statsCtrl.setAndMask(mi.getMask().getPlaneBitMask(self.config.maskPlanes))
        stats = afwMath.makeStatistics(mi.getVariance(), mi.getMask(), afwMath.MEDIAN, statsCtrl)
        sigma1 = math.sqrt(stats.getValue(afwMath.MEDIAN))
        self.log.logdebug('sigma1: %g' % sigma1)

        n0 = len(srcs)
        nparents = 0
        for i,src in enumerate(srcs):
            #t0 = time.clock()

            fp = src.getFootprint()
            pks = fp.getPeaks()

            # Since we use the first peak for the parent object, we should propagate its flags
            # to the parent source.
            src.assign(pks[0], self.peakSchemaMapper)

            if len(pks) < 2:
                continue

            if self.isLargeFootprint(fp):
                src.set(self.tooBigKey, True)
                self.skipParent(src, mi.getMask())
                self.log.logdebug('Parent %i: skipping large footprint' % (int(src.getId()),))
                continue
            if self.isMasked(fp, exposure.getMaskedImage().getMask()):
                src.set(self.maskedKey, True)
                self.skipParent(src, mi.getMask())
                self.log.logdebug('Parent %i: skipping masked footprint' % (int(src.getId()),))
                continue

            nparents += 1
            bb = fp.getBBox()
            psf_fwhm = self._getPsfFwhm(psf, bb)

            self.log.logdebug('Parent %i: deblending %i peaks' % (int(src.getId()), len(pks)))

            self.preSingleDeblendHook(exposure, srcs, i, fp, psf, psf_fwhm, sigma1)
            npre = len(srcs)

            # This should really be set in deblend, but deblend doesn't have access to the src
            src.set(self.tooManyPeaksKey, len(fp.getPeaks()) > self.config.maxNumberOfPeaks)

            try:
                res = deblend(
                    fp, mi, psf, psf_fwhm, sigma1=sigma1,
                    psfChisqCut1 = self.config.psfChisq1,
                    psfChisqCut2 = self.config.psfChisq2,
                    psfChisqCut2b= self.config.psfChisq2b,
                    maxNumberOfPeaks=self.config.maxNumberOfPeaks,
                    strayFluxToPointSources=self.config.strayFluxToPointSources,
                    assignStrayFlux=self.config.assignStrayFlux,
                    findStrayFlux=(self.config.assignStrayFlux or self.config.findStrayFlux),
                    strayFluxAssignment=self.config.strayFluxRule,
                    rampFluxAtEdge=(self.config.edgeHandling == 'ramp'),
                    patchEdges=(self.config.edgeHandling == 'noclip'),
                    tinyFootprintSize=self.config.tinyFootprintSize,
                    clipStrayFluxFraction=self.config.clipStrayFluxFraction,
                    )
                if self.config.catchFailures:
                    src.set(self.deblendFailedKey, False)
            except Exception as e:
                if self.config.catchFailures:
                    self.log.warn("Unable to deblend source %d: %s" % (src.getId(), e))
                    src.set(self.deblendFailedKey, True)
                    import traceback
                    traceback.print_exc()
                    continue
                else:
                    raise

            kids = []
            nchild = 0
            for j, peak in enumerate(res.peaks):
                heavy = peak.getFluxPortion()
                if heavy is None or peak.skip:
                    src.set(self.deblendSkippedKey, True)
                    if not self.config.propagateAllPeaks:
                        # Don't care
                        continue
                    # We need to preserve the peak: make sure we have enough info to create a minimal child src
                    self.log.logdebug("Peak at (%i,%i) failed.  Using minimal default info for child." %
                                      (pks[j].getIx(), pks[j].getIy()))
                    if heavy is None:
                        # copy the full footprint and strip out extra peaks
                        foot = afwDet.Footprint(src.getFootprint())
                        peakList = foot.getPeaks()
                        peakList.clear()
                        peakList.append(peak.peak)
                        zeroMimg = afwImage.MaskedImageF(foot.getBBox())
                        heavy = afwDet.makeHeavyFootprint(foot, zeroMimg)
                    if peak.deblendedAsPsf:
                        if peak.psfFitFlux is None:
                            peak.psfFitFlux = 0.0
                        if peak.psfFitCenter is None:
                            peak.psfFitCenter = (peak.peak.getIx(), peak.peak.getIy())

                assert(len(heavy.getPeaks()) == 1)

                src.set(self.deblendSkippedKey, False)
                child = srcs.addNew(); nchild += 1
                child.assign(heavy.getPeaks()[0], self.peakSchemaMapper)
                child.setParent(src.getId())
                child.setFootprint(heavy)
                child.set(self.psfKey, peak.deblendedAsPsf)
                child.set(self.hasStrayFluxKey, peak.strayFlux is not None)
                if peak.deblendedAsPsf:
                    (cx,cy) = peak.psfFitCenter
                    child.set(self.psfCenterKey, afwGeom.Point2D(cx, cy))
                    child.set(self.psfFluxKey, peak.psfFitFlux)
                child.set(self.deblendRampedTemplateKey, peak.hasRampedTemplate)
                child.set(self.deblendPatchedTemplateKey, peak.patched)
                kids.append(child)

            # Child footprints may extend beyond the full extent of their parent's which
            # results in a failure of the replace-by-noise code to reinstate these pixels
            # to their original values.  The following updates the parent footprint
            # in-place to ensure it contains the full union of itself and all of its
            # children's footprints.
            src.getFootprint().include([child.getFootprint() for child in kids])

            src.set(self.nChildKey, nchild)

            self.postSingleDeblendHook(exposure, srcs, i, npre, kids, fp, psf, psf_fwhm, sigma1, res)
            #print 'Deblending parent id', src.getId(), 'took', time.clock() - t0


        n1 = len(srcs)
        self.log.info('Deblended: of %i sources, %i were deblended, creating %i children, total %i sources'
                      % (n0, nparents, n1-n0, n1))

    def preSingleDeblendHook(self, exposure, srcs, i, fp, psf, psf_fwhm, sigma1):
        pass

    def postSingleDeblendHook(self, exposure, srcs, i, npre, kids, fp, psf, psf_fwhm, sigma1, res):
        pass

    def isLargeFootprint(self, footprint):
        """Returns whether a Footprint is large

        'Large' is defined by thresholds on the area, size and axis ratio.
        These may be disabled independently by configuring them to be non-positive.

        This is principally intended to get rid of satellite streaks, which the
        deblender or other downstream processing can have trouble dealing with
        (e.g., multiple large HeavyFootprints can chew up memory).
        """
        if self.config.maxFootprintArea > 0 and footprint.getArea() > self.config.maxFootprintArea:
            return True
        if self.config.maxFootprintSize > 0:
            bbox = footprint.getBBox()
            if max(bbox.getWidth(), bbox.getHeight()) > self.config.maxFootprintSize:
                return True
        if self.config.minFootprintAxisRatio > 0:
            axes = afwEll.Axes(footprint.getShape())
            if axes.getB() < self.config.minFootprintAxisRatio*axes.getA():
                return True
        return False

    def isMasked(self, footprint, mask):
        """Returns whether the footprint violates the mask limits"""
        size = float(footprint.getArea())
        for maskName, limit in self.config.maskLimits.iteritems():
            maskVal = mask.getPlaneBitMask(maskName)
            unmasked = afwDet.Footprint(footprint)
            unmasked.intersectMask(mask, maskVal) # footprint of unmasked pixels
            if (size - unmasked.getArea())/size > limit:
                return True
        return False

    def skipParent(self, source, mask):
        """Indicate that the parent source is not being deblended

        We set the appropriate flags and mask.

        @param source  The source to flag as skipped
        @param mask  The mask to update
        """
        fp = source.getFootprint()
        source.set(self.deblendSkippedKey, True)
        source.set(self.nChildKey, len(fp.getPeaks())) # It would have this many if we deblended them all
        if self.config.notDeblendedMask:
            mask.addMaskPlane(self.config.notDeblendedMask)
            afwDet.setMaskFromFootprint(mask, fp, mask.getPlaneBitMask(self.config.notDeblendedMask))
