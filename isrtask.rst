
#######
IsrTask 
#######

Instrument Signature Removal (ISR) is a sequence of steps taken to
'clean' images of various aspects of defects that any system of optics
and detectors will imprint on an image by default, and is generally
one of the very first procedures carried out on an exposure.

In more detail: though the process for correcting imaging data is very
similar from camera to camera, depending on the image, various of the
defects will be present and need to be removed, and thus the sequence
of steps taken will vary from image to image.  Generally these
corrections are done one CCD at a time, but on all the amplifier
sub-images at once for a CCD.  This is how the framework code ingests
and processes the information.

IsrTask provides a generic vanilla implementation of doing these
corrections, including the ability to turn certain corrections off if
they are not needed.

This task is implemented in the ``lsst.ip.isr`` module.

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.


Configuration
=============

Flags  and utility variables
----------------------------

-``doBias`` -- ( `bool` ) --  defaults to `True` - Apply bias frame correction?

-``doDark`` -- ( `bool` ) --  defaults to `True` - Apply dark frame correction?

-``doFlat`` -- ( `bool` ) --  defaults to `True` - Apply flat field correction?

-``doFringe`` -- ( `bool` ) --  defaults to `True` - Apply fringe correction?

-``doWrite`` -- ( `bool` ) --  defaults to `True` - Persist postISRCCD?

-``gain`` -- ( `float` ) --  defaults to `float("NaN")` - The gain to use if no Detector is present in the Exposure (ignored if NaN)

-``readNoise`` -- ( `float` ) --  defaults to `0.0` - The read noise to use if no Detector is present in the Exposure

-``saturation`` -- ( `float` ) --  defaults to `float("NaN")` - The saturation level to use if no Detector is present in the Exposure (ignored if NaN)

-``fringeAfterFlat`` -- ( `bool` ) --  defaults to `True` - Do fringe subtraction after flat-fielding?

-``fwhm`` -- ( `float` ) --  defaults to `1.0` - FWHM of PSF (arcsec)

-``saturatedMaskName`` -- ( `str` ) --  defaults to `"SAT"` - Name of mask plane to use in saturation detection and interpolation

-``flatUserScale`` -- ( `float` ) --  defaults to `1.0` - If flatScalingType is 'USER' then scale flat by this amount; ignored otherwise

-``overscanOrder`` -- ( `int` ) --  defaults to `1` - Order of polynomial or to fit if overscan fit type is a polynomial

-``overscanRej`` -- ( `float` ) --  defaults to `3.0` - Rejection threshold (sigma) for collapsing overscan before fit

-``growSaturationFootprintSize`` -- ( `int` ) --  defaults to `1` - Number of pixels by which to grow the saturation footprints

-``fluxMag0T1`` -- ( `float` ) --  defaults to `1e10` - The approximate flux of a zero-magnitude object in a one-second exposure

-``setGainAssembledCcd`` -- ( `bool` ) --  defaults to `True` - update exposure metadata in the assembled ccd to reflect the effective gain of the assembled chip

-``doAssembleIsrExposures`` -- ( `bool` ) --  defaults to `False` - Assemble amp-level calibration exposures into ccd-level exposure?

-``doAssembleCcd`` -- ( `bool` ) --  defaults to `True` - Assemble amp-level exposures into a ccd-level exposure?

-``doBrighterFatter`` -- ( `bool` ) --  defaults to `False` - Apply the brighter fatter correction

-``brighterFatterKernelFile`` -- ( `str` ) --  defaults to `empty string` - Kernel file used for the brighter fatter correction

-``brighterFatterMaxIter`` -- ( `int` ) --  defaults to `18` - Maximum number of iterations for the brighter fatter correction

-``brighterFatterThreshold`` -- ( `float` ) --  defaults to `1000` - Threshold used to stop iterating the brighter fatter correction.  It is the absolute value of the difference between the current corrected image and the one from the previous iteration summed over all the pixels.

-``brighterFatterApplyGain`` -- ( `bool` ) --  defaults to `True` - Should the gain be applied when applying the brighter fatter correction?

-``datasetType`` -- ( `str` ) --  defaults to `"raw"` - Dataset type for input data; users will typically leave this alone

-``fallbackFilterName`` -- ( `str` ) --  no default - Fallback default filter name for calibrations


-``suspectMaskName`` -- ( `str` ) -- defaults to "SUSPECT" -- Name of mask plane to use for suspect pixels
	
-``flatScalingType`` -- ( `str` ) -- default to 'USER' -- The method for scaling the flat on the fly, allowed values:

	- "USER": "Scale by flatUserScale"
	-          "MEAN": "Scale by the inverse of the mean"
        -          "MEDIAN": "Scale by the inverse of the median"
     
 
-``overscanFitType`` -- ( `str` ) -- defaults to 'MEDIAN' -- The method for fitting the overscan bias level, allowed values:

	- "POLY": "Fit ordinary polynomial to the longest axis of the overscan region",
	-        "CHEB": "Fit Chebyshev polynomial to the longest axis of the overscan region",
	-  "LEG": "Fit Legendre polynomial to the longest axis of the overscan region",
        -   "NATURAL_SPLINE": "Fit natural spline to the longest axis of the overscan region",
        -  "CUBIC_SPLINE": "Fit cubic spline to the longest axis of the overscan region",
        -  "AKIMA_SPLINE": "Fit Akima spline to the longest axis of the overscan region",
        -  "MEAN": "Correct using the mean of the overscan region",
        -  "MEDIAN": "Correct using the median of the overscan region"
     
 
-``keysToRemoveFromAssembledCcd`` -- ( `str` ) --  defaults to empty list -- Fields to remove from the metadata of the assembled ccd

 
-``doLinearize`` -- ( `str` ) -- defaults to `True` -- Correct for nonlinearity of the detector's response?
 
-``fallbackFilterName`` -- ( `str` ) -- no default -- Fallback default filter name for calibrations

Subtasks
--------

-	``assembleCcd`` -- target=AssembleCcdTask -  CCD assembly task

-	``fringe`` --  target=FringeTask - Fringe subtraction task
 

Entrypoint
==========

- ``lsst.ip.isr.isrTask.IsrTask.run``


Butler Inputs
=============

`dataRef` – a ``daf.persistence.butlerSubset.ButlerDataRef`` of the
detector data to be processed

The inputs to the entrypoint method are the raw exposure to be
corrected and the calibration data products. The raw input is a single
chip-sized mosaic of all amps including overscans and other
non-science pixels.

Butler Outputs
==============

Examples
========

If you want to see an example of the ISR algorithm in action, run the
example while in the ``$IP_ISR_DIR/examples`` as follows::

  python  examples/runIsrTask.py  --write --ds9

The `write` flag tells the code to write the post-ISR image file to disk.  In this example code, this output file is called:: 

   postISRCCD.fits

The `ds9` flag tells it to bring up the ds9 image viewer (if installed) and show the post-ISR FITS image.

	    
To explain this example in more detail: after setting up the flag and utility variable configuration the code 
makes several calibration exposures that will be used to create the final corrected output exposure.  Finally, the output is produced by using the ``run`` function, inputting the raw exposure and the calibration exposures.


Details on some of the corrections available in IsrTask
=======================================================

Bias correction
----------------

The bias correction is applied to remove the additive electronic
bias that is present in the signal chain. To first
approximation, the bias is a constant pedestal, but it has low-amplitude structure
that is related to its electronic stability during
read-out of the detector segment. The processing pipeline removes the
bias contribution in a two-step process. In the first step, the median
value of non-flagged pixels in the overscan region is subtracted from
the image. In the second step, the reference bias image is subtracted
from the science image to remove the higher-order structure.

Following the bias correction, the pixels are scaled by the gain
factor for the appropriate CCD. The brightness units are electrons (or
equivalently for unit gain, detected photons) for calibrated images.

More specifically, the IsrTask biasCorrection method takes as
arguments the science exposure and the bias exposure, and first checks
if they have the same exact footprint (i.e. if the 4 corners are all
at the same locations), and if not, it raises a RuntimeError saying
that they’re not the same size.

If they are the same size, it takes the masked science exposure and
simply does a straight subtraction (pixel by pixel) of the bias
exposure, and returns this.

Brighter-Fatter Correction
--------------------------

The Brighter-Fatter Correction is the standard name now given to the
correction that has to be done in the era of 'precision astronomy'
(though it has always been present in images at some level) because a
pixel tower 'fills up' with electrons at the bottom of the silicon
layer when many photons hit the top of the detector, altering the
normal electric field lines set up to trap all the electrons liberated
from normal photon hits in that tower, and forcing some of the
resultant electrons into neighboring pixels.  This requires careful
treatment to correct for that is the subject of ongoing research, but
the currently implemented model is a fairly advanced one that takes a
kernel that has been derived from flat field images to redistribute
the charge.

(This method in particular is described in substantial detail in the
docstring currently in the code.)


Cross-Talk Correction
----------------------

Cross-talk introduces a small fraction of the signal from one CCD into
the signal chain of the CCD that shares the same electronics,
resulting in “ghosts” of bright objects appearing in the
paired CCD. This is an additive effect, and is most noticeable for
sources that are very bright, at or near saturation.

(Not clear if LSST CCDs will need this correction, so the pipeline has
a placeholder for it, should it be necessary, but no cross-talk
correction is implemented at this time.)

Dark correction
---------------

The dark current is the signal introduced by thermal electrons in the
silicon of the detectors with the camera shutter closed. Dark
correction is done by subtracting a reference Dark calibration
frame that has been scaled to the exposure time of the visit image.

Flat fielding
-------------

The flat-field correction (often called "flat fielding") removes the
variations in the pixel-to-pixel response of the detectors. The
flat-field is derived for each filter in several ways, depending on
the telescope: from images of the twilight sky ("twilight flats");
from a screen within the dome ("dome flats"); or from a simulated
continuum source. In all cases the flat-field corrects approximately
for vignetting across the CCD (i.e. the variation in the amount of
light that hits the detector due to angle of incidence into the
aperture at the top of the telescope tube, and the resultant shadow
from one side) . The flat-field correction is performed by dividing
each science frame by a normalized, reference flat-field image for the
corresponding filter.

Fringe Pattern Correction
-------------------------

A fringe pattern is present in many detectors in particularly the reddest
filters: the i-, z-, and y-bands. The pattern occurs because of
interference between the incident, nearly monochromatic light from
night sky emission lines (both from air glow from particular
components of the atmosphere, and from reflected city
lights) and the layers of the CCD substrate. The details of the fringe
pattern depend mostly upon the spatial variation in thickness of the
top layer of the substrate, but also depend upon a number of other
factors including the wavelength(s) of the incident emission lines,
the composition of the substrate, the temperature of the CCD, and the
focal ratio of the incident beam. The amplitude of the fringe pattern
background varies with time and telescope pointing.


Gain
----

This is accounting for how many electrons correspond to each ADU
coming out of the sensors.


Linearity Correction
--------------------

The response of the CCD detectors to radiation is highly linear for
pixels that are not near saturation, to typically better than 0.1% for
most recent cameras.

Currently, no linearity correction is applied in the DM pipelines.

Were a correction necessary it would likely be implemented with a
look-up table, and executed following the dark correction but prior to
fringe correction.



Overscan Correction
-------------------

This is similar in structure to bias etc. -- except the function
overscanCorrection in isr.py is quite long and extensive, and has
several interpln choices etc.


Saturation detection
---------------------

This one is fairly straightforward -- it is finding the pixels that
are saturated (have their potential wells full of charge).

Most of the work is done in makeThresholdMask i


Saturation Correction
---------------------

At the start of pipeline processing the pixel values are examined to
detect saturation (which will naturally also identify bleed trails
near saturated targets, and the strongest cosmic rays). These values,
along with pixels that are identified in the list of static bad
pixels, are flagged in the data quality mask of the science image.
All pixels in the science array identified as “bad” in this sense are
interpolated over, in order to avoid problems with source detection
and with code optimization for other downstream pipeline processing.

Interpolation is performed with a linear predictive code, as was done
for the Sloan Digital Sky Survey (SDSS). The PSF is taken to be a
Gaussian with sigma width equal to one pixel when deriving the
coefficients. For interpolating over most defects the interpolation is
only done in the x-direction, extending 2 pixels on each side of the
defect. This is done both for simplicity and to ameliorate the way
that saturation trails interact with bad columns.


Debugging
=========

- ``display`` - A dictionary containing debug point names as keys with frame number as value.  The only valid key is:

  ``postISRCCD`` (to display exposure after ISR has been applied)


Algorithm details
====================

-------------
  
  [Reference: Section 4 of LSST DATA CHALLENGE HANDBOOK (2011), and http://hsca.ipmu.jp/public/index.html ]

  
