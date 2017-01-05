
#######
IsrTask 
#######


Instrumental Signature Removal (ISR) is a sequence of steps taken to
'clean' images of various aspects of defects that any system of optics
and detectors will imprint on an image by default, and is generally
one of the very first procedures carried out on an exposure.

In more detail: though the process for correcting imaging data is very
similar from camera to camera, depending on the image, various of the
defects will be present and need to be removed, and thus the sequence
of steps taken will vary from image to image.  Generally these
corrections are done one CCD at a time, but with all the amplifiers at
once for a CCD.  This is how the framework code ingests and processes
the information.

IsrTask provides a generic vanilla implementation of doing these
corrections, including the ability to turn certain corrections off if
they are not needed.


Module membership
=================

This task is implemented in the ``lsst.ip.isr`` module.

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.


Configuration
=============

Flags  and utility variables
----------------------------

-	doBias
 
-	doDark
 
-	doFlat
 
-	doFringe
 
-	doWrite
 
-	gain
 
-	readNoise
 
-	saturation
 
-	fringeAfterFlat
 
-	fwhm
 
-	saturatedMaskName
 
-	suspectMaskName
 
-	flatScalingType
 
-	flatUserScale
 
-	overscanFitType
 
-	overscanOrder
 
-	overscanRej
 
-	growSaturationFootprintSize
 
-	fluxMag0T1
 
-	setGainAssembledCcd
 
-	keysToRemoveFromAssembledCcd
 
-	doAssembleIsrExposures
 
-	doAssembleCcd
 
-	doLinearize
 
-	doBrighterFatter
 
-	brighterFatterKernelFile
 
-	brighterFatterMaxIter
 
-	brighterFatterThreshold
 
-	brighterFatterApplyGain
 
-	datasetType
 
-	fallbackFilterName

Subtasks
--------

-	assembleCcd -- target=AssembleCcdTask -  CCD assembly task

-	fringe --  target=FringeTask - Fringe subtraction task
 



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

The `ds9` flag tells it to bring up ds9 (if installed) and show the post-ISR FITS image.



	    
Specific functions of IsrTask via example
+++++++++++++++++++++++++++++++++++++++++

To use a concrete example, we will follow the simple steps in
``runIsrTask`` to trace how a specific code would do ISR processing -- it
will be different for every camera and exposure.

The first several lines of runIsrTask (after imports) define a
function runIsr that has the following in it::

    #Create the isr task with modified config
    isrConfig = IsrTask.ConfigClass()
    isrConfig.doBias = False #We didn't make a zero frame
    isrConfig.doDark = True
    isrConfig.doFlat = True
    isrConfig.doFringe = False #There is no fringe frame for this example

The first line indicates this is a section about setting up the
configuration that the code will be run with.  The next several set up
specific flags, indicating that we will not do bias or fringing
corrections in this code, but will do the dark and flat corrections.

It then defines parameters that it will use to make the raw, flat and
dark exposures, using knowledge of our camera and exposures::
  
    DARKVAL = 2.      # Number of electrons per sec
    OSCAN = 1000.     # DN = Data Number, same as the standard ADU
    GRADIENT = .10
    EXPTIME = 15      # Seconds for the science exposure
    DARKEXPTIME = 40. # Seconds for the dark exposure

Next, it makes the 3 exposures that we will be using in this example to create the final corrected output exposure::
  
    darkExposure = exampleUtils.makeDark(DARKVAL, DARKEXPTIME)
    flatExposure = exampleUtils.makeFlat(GRADIENT)
    rawExposure = exampleUtils.makeRaw(DARKVAL, OSCAN, GRADIENT, EXPTIME)

(We are using functions defined in exampleUtils, also in the examples
subdir inside $IP_ISR_DIR, these are modified versions of the standard
functions which sit inside other pkgs normally.)


Finally, the output is produced with the line::

       output = isrTask.run(rawExposure, dark=darkExposure, flat=flatExposure)

And returned at the end of the function.

(The ``main`` function of runIsrTask simply calls this runIsr function,
and also brings up ds9 to view the final output exposure if that flag
is set on, and writes the img to disk if that flag is set.)

Next, let's look at the two specific functions that the example uses.

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


Other ISR steps
+++++++++++++++

Now we describe corrections that are not in the example, but
that IsrTask can also correct for, leading to final corrected
images.

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





List of IsrTask Functions
=========================

Functions the code is capable of handling, though not all are used,
depending on an image (in alphabetical order).


- `Bias`

- `Brighter fatter correction`

- `Dark`

- `Flat-fielding`

- `Fringing`

- `Gain`

- `Linearization`

- `Mask defects, and interpolate over them`
  
- `Mask NaNs`
  
- `Overscan`
  
- `Saturation detection`
  
- `Saturation interpln`
  
- `Suspect pixel detection`
  
- `Update variance plane`


Algorithm details
====================

  IsrTask performs instrument signature removal on an exposure following
these overall steps:

- ``lsst.pipe.tasks.isrTask.IsrTask.saturationDetection`` - Detects saturation: finding out which pixels have current which overfills their potential wells

- ``lsst.ip.isr.isrTask.IsrTask.biasCorrection`` - Does bias subtraction: removing the pedestal introduced by the instrument for a zero-second exposure (may use the overscan correction function)

- ``lsst.ip.isr.isrTask.IsrTask.darkCorrection`` - Does dark correction: i.e. removing the dark current, which is the residual current seen even when no light is falling on the sensors

- ``lsst.ip.isr.isrTask.IsrTask.flatCorrection`` - Does flat-fielding: i.e. correcting for the different responsivity of the current coming from pixels to the same amount of light falling on them

- ``lsst.ip.isr.isrTask.IsrTask.brighterFatterCorrection`` - Does the brighter fatter correction: i.e. accounting for the distortion of the electric field lines at the bottom of pixels when bright objects liberate many charges that get trapped at the bottom of the potential wells


- [Performs CCD assembly  ----> is this a funct of isrTask..?]

- ``lsst.ip.isr.isrTask.IsrTask.maskAndInterpDefect`` , and ``lsst.ip.isr.isrTask.IsrTask.maskAndInterpNan`` - Mask known bad pixels, defects, saturated pixels and all NaNs and interpolate over them

- [Provides a preliminary WCS ----> don't see this show up anywhere.]


-------------
  
  [Reference: Doxygen comments in code, and Section 4 of LSST DATA CHALLENGE HANDBOOK (2011), and http://hsca.ipmu.jp/public/index.html ]

  
