
#######
IsrTask 
#######

Instrument Signature Removal (ISR) is a sequence of steps taken to
'clean' images of various aspects of defects that any system of optics
and detectors will imprint on an image by default, and is generally
one of the very first procedures carried out on an exposure.

In more detail, though the process for correcting imaging data is very
similar from camera to camera, depending on the image, various of the
defects will be present and need to be removed, and thus the sequence
of steps taken will vary from image to image.  Generally these
corrections are done one CCD at a time, but on all the amplifier
sub-images at once for a CCD.  

IsrTask provides a generic vanilla implementation of doing these
corrections, including the ability to turn certain corrections off if
they are not needed.

This task is implemented in the `lsst.ip.isr`_ module.

.. _`lsst.ip.isr`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1ip_1_1isr.html

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.


Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	``assembleCcd`` , AssembleCcdTask ,  CCD assembly task
	``fringe`` ,  FringeTask , Fringe subtraction task
 
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   ``doBias``, `bool`,   `True`,  Apply bias frame correction?
   ``doDark``, `bool`,   `True`,  Apply dark frame correction?
   ``doFlat``, `bool`,   `True`,  Apply flat field correction?
   ``doFringe``, `bool`,   `True`,  Apply fringe correction?
   ``doWrite``, `bool`,   `True`,  Persist postISRCCD?
   ``gain``, `float`,   `float("NaN")`,  The gain to use if no Detector is present in the Exposure (ignored if NaN)
   ``readNoise``, `float`,   `0.0`,  The read noise to use if no Detector is present in the Exposure
   ``saturation``, `float`,   `float("NaN")`,  The saturation level to use if no Detector is present in the Exposure (ignored if NaN)
   ``fringeAfterFlat``, `bool`,   `True`,  Do fringe subtraction after flat   fielding?
   ``fwhm``, `float`,   `1.0`,  FWHM of PSF (arcsec)
   ``saturatedMaskName``, `str`,   `"SAT"`,  Name of mask plane to use in saturation detection and interpolation
   ``flatUserScale``, `float`,   `1.0`,  If flatScalingType is 'USER' then scale flat by this amount; ignored otherwise
   ``overscanOrder``, `int`,   `1`,  Order of polynomial or to fit if overscan fit type is a polynomial
   ``overscanRej``, `float`,   `3.0`,  Rejection threshold (sigma) for collapsing overscan before fit
   ``growSaturationFootprintSize``, `int`,   `1`,  Number of pixels by which to grow the saturation footprints
   ``fluxMag0T1``, `float`,   `1e10`,  The approximate flux of a zero   magnitude object in a one-second exposure
   ``setGainAssembledCcd``, `bool`,   `True`,  update exposure metadata in the assembled ccd to reflect the effective gain of the assembled chip
   ``doAssembleIsrExposures``, `bool`,   `False`,  Assemble amp-level calibration exposures into ccd-level exposure?
   ``doAssembleCcd``, `bool`,   `True`,  Assemble amp-level exposures into a ccd-level exposure?
   ``doBrighterFatter``, `bool`,   `False`,  Apply the brighter fatter correction
   ``brighterFatterKernelFile``, `str`,   `empty string`,  Kernel file used for the brighter fatter correction
   ``brighterFatterMaxIter``, `int`,   `18`,  Maximum number of iterations for the brighter fatter correction
   ``brighterFatterThreshold``, `float`,   `1000`,  Threshold used to stop iterating the brighter fatter correction.  It is the absolute value of the difference between the current corrected image and the one from the previous iteration summed over all the pixels.
   ``brighterFatterApplyGain``, `bool`,   `True`,  Should the gain be applied when applying the brighter fatter correction?
   ``datasetType``, `str`,   `"raw"`,  Dataset type for input data; users will typically leave this alone
   ``fallbackFilterName``, `str`,  no default,  Fallback default filter name for calibrations
   ``suspectMaskName``, `str`,  "SUSPECT", Name of mask plane to use for suspect pixels
   ``flatScalingType``, `str`, default to 'USER', The method for scaling the flat on the fly; allowed values:	- "USER": "Scale by flatUserScale"	-          "MEAN": "Scale by the inverse of the mean"        -           "MEDIAN": "Scale by the inverse of the median" 
   ``keysToRemoveFromAssembledCcd``, `str`,   empty list, Fields to remove from the metadata of the assembled ccd
   ``doLinearize``, `str`,  `True`, Correct for nonlinearity of the detector's response?
   ``fallbackFilterName``, `str`, no default, Fallback default filter name for calibrations
   ``overscanFitType``, `str`,  'MEDIAN', The method for fitting the overscan bias level; allowed values:	- "POLY": "Fit ordinary polynomial to the longest axis of the overscan region"	-        "CHEB": "Fit Chebyshev polynomial to the longest axis of the overscan region"	-  "LEG": "Fit Legendre polynomial to the longest axis of the overscan region"        -    "NATURAL_SPLINE": "Fit natural spline to the longest axis of the overscan region"        -   "CUBIC_SPLINE": "Fit cubic spline to the longest axis of the overscan region"        -  "AKIMA_SPLINE": "Fit Akima spline to the longest axis of the overscan region"        -  "MEAN": "Correct using the mean of the overscan region"        -  "MEDIAN": "Correct using the median of the overscan region"
     


Entrypoint
==========

- `lsst.ip.isr.isrTask.IsrTask.run`_

.. _`lsst.ip.isr.isrTask.IsrTask.run`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#aab476cefa23d730451f39119e04875d5  


Butler Inputs
=============

`dataRef` – a ``daf.persistence.butlerSubset.ButlerDataRef`` of the
detector data to be processed

The inputs to the entrypoint method are the exposure to be corrected
(which will be of ``datasetType`` ``raw``) and the calibration data products. The raw input
is a single chip-sized mosaic of all amps including overscans and
other non-science pixels.

Butler Outputs
==============

Exposure of ``datasetType`` ``postISRCCD``.

Examples
========

If you want to see an example of the ISR algorithm in action, run the
example while in the ``$IP_ISR_DIR/examples`` as follows::

  python  examples/runIsrTask.py ,write --ds9

The `write` flag tells the code to write the post-ISR image file to disk.  In this example code, this output file is called:: 

   postISRCCD.fits

The `ds9` flag tells it to bring up the ds9 image viewer (if installed) and show the post-ISR image.

	    
In slightly more detail, what this example does is after setting up
the parameter configuration, the code makes several calibration
exposures that will be used to create the final corrected output
exposure.  Finally, the output is produced by using the `run`_
function, after ingesting the raw exposure and the calibration
exposures and processing them.

.. _`run`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#aab476cefa23d730451f39119e04875d5

Debugging
=========

- ``display`` - A dictionary containing debug point names as keys with frame number as value.  The only valid key is:

  ``postISRCCD`` (to display exposure after ISR has been applied)


Algorithm details
====================

IsrTask performs instrument signature removal on an exposure in varying ways depending on which corrections need to be applied to the raw image, but generally some combination of the following is done:

- Finding out which pixels have charge which overfills their potential wells

- Bias subtraction: removing the pedestal introduced by the instrument for a zero-second exposure (may use the overscan correction function)

-   Dark correction: i.e. removing the dark current, which is the residual current seen even when no light is falling on the sensors

-   Flat-fielding: i.e. correcting for the different responsivity of the current coming from pixels to the same amount of light falling on them

- Apply brighter fatter correction: i.e. accounting for the distortion of the electric field lines at the bottom of pixels when bright objects liberate many charges that get trapped at the bottom of the potential wells

- Mask known bad pixels, defects, saturated pixels and all NaNs and interpolate over them

[Extra reference: Section 4 of LSST DATA CHALLENGE HANDBOOK (2011) [https://project.lsst.org/sciencewiki/images/DC_Handbook_v1.1.pdf] , and http://hsca.ipmu.jp/public/index.html ]

  
