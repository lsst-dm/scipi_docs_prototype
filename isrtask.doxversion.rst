
2/4

IsrTask.doxygenVersion
=========================================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#IsrTask_


Instrumental Signature Removal (ISR) is a sequence of steps taken to
'clean' images of various aspects of defects that any system of optics
and detectors will imprint on an image by default.  Though the process
for correcting imaging data is very similar from camera to camera,
depending on the image, various of the defects will be present and
need to be removed, and thus the sequence of steps taken will vary
from image to image.  Generally these corrections are done one CCD at
a time, but with all the amplifiers at once for a CCD.  This is how
the DM code ingests and processes the information.

The ISR code is at::
   
     $IP_ISR_DIR/python/lsst/ip/isr/isrTask.py.

IsrTask provides a generic vanilla implementation of doing these
corrections, including the ability to turn certain corrections off if
they are not needed.

The inputs to the primary method, 'run', are a raw exposure to be
corrected and the calibration data products. The raw input is a single
chip-sized mosaic of all amps including overscans and other
non-science pixels.

IsrTask performs instrument signature removal on an exposure following these overall steps:

- Detects saturation: finding out which pixels have current which overfills their potential wells

- Does bias subtraction: removing the pedestal introduced by the instrument for a zero-second exposure (may use the overscan correction function)

- Does dark correction: i.e. removing the dark current, which is the residual current seen even when no light is falling on the sensors

- Does flat-fielding: i.e. correcting for the different responsivity of the current coming from pixels to the same amount of light falling on them

- Does the brighter fatter correction: i.e. accounting for the distortion of the electric field lines at the bottom of pixels when bright objects liberate many charges that get trapped at the bottom of the potential wells


- Performs CCD assembly

- Masks known bad pixels

- Interpolates over defects, saturated pixels and all NaNs

- Provides a preliminary WCS

List of IsrTask Functions
+++++++++++++++++++++++++

Functions the code is capable of handling, though not all are used,
depending on an image (in alphabetical order), with the links here going to the actual code:

- `Bias`_
.. _Bias: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#aa6ccdf9dcf1735c5ed90c2c23e496725
- `Brighter fatter correction`_
.. _Brighter fatter correction: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#abcef49896d412c901f42e960dce9e280
- `Dark`_
.. _Dark: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#ab41dc49d2b1df5388fe3f653bfadcfd6 
- `Flat-fielding`_
.. _Flat-fielding: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#ae6918c99805e1f902687842a7b09cf56

- Fringing

- `Gain`_
.. _Gain: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#ae1a9c9352c1c1064957726788209362a
- `Linearization`_ 
.. _Linearization: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#aea4a28fc61394c45adbb104248828e60
- `Mask defects, and interpolate over them`_ 
.. _Mask defects, and interpolate over them: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#ac938896ee62ee77619f07fb85de47350
- `Mask NaNs`_  
.. _Mask NaNs: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a5ae0dffccdb1be2188a1538baed45412
- `Overscan`_ 
.. _Overscan: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a5e5c48656c428d20fb981a6858ee98cb
- `Saturation detection`_ 
.. _Saturation detection: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a853d9470afa9e178fb42bb050e6fc3a4
- `Saturation interpln`_ 
.. _Saturation interpln: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a7d6b3e4ec6233d1da18a514be8d82f63
- `Suspect pixel detection`_ 
.. _Suspect pixel detection: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a0fd004b4c3ec4dfd9e8779421a806c4a
- `Update variance plane`_ 
.. _Update variance plane: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#a8f5afe71d7d8b7bc824fd15f63257b8f

If you want to see an example of the ISR algorithm in action, run the example while in the $IP_ISR_DIR as follows::

  python  examples/runIsrTask.py  --write --ds9

The ‘write’ flag tells the code to write the post-ISR image file to disk.  In this example code, this output file is called:: 

   postISRCCD.fits

The ‘ds9’ flag tells it to bring up ds9 (if installed) and show the post-ISR FITS image.

  
.. ISR does the following:
            - assemble raw amplifier images into an exposure with image, variance and mask planes
    
	    
Specific functions of IsrTask via example
+++++++++++++++++++++++++++++++++++++++++

To use a concrete example, we will follow the simple steps in
runIsrTask to trace how a specific code would do ISR processing -- it
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

(The 'main' function of runIsrTask simply calls this runIsr function, and also brings
up ds9 to view the final output exposure if that flag is set on, and
writes the img to disk if that flag is set.)

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
that IsrTask can also take correct for, leading to final corrected
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

This is accounting for how many electrons correspond to each ADU coming out of the sensors. 


Linearity Correction
--------------------

The response of the CCD detectors to radiation is highly linear for
pixels that are not near saturation, to typically better than 0.1% for
most recent cameras.

Currently, no linearity correction is applied in the DM pipelines.

Were a correction necessary it would likely be implemented with a
look-up table, and executed following the dark correction but prior to
fringe correction.

..
 Mask defects
 ------------

 How to find the pixels that have problems 

 Masked pixel interpolation
 ----------------------------

 Mask NaNs
 ------------

 Masked NaN interpolation
 ----------------------------


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

..
 Suspect pixel detection
 ------------------------

 This seems to be part of the overscan correction in isr.py

..
 Update variance plane
 -----------------------

____


[Reference: Doxygen comments in code, and Section 4 of LSST DATA CHALLENGE HANDBOOK (2011), and http://hsca.ipmu.jp/public/index.html ]

Examples
++++++++





