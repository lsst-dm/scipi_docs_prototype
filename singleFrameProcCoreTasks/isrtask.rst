
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

`IsrTask <#>`_ provides a generic vanilla implementation of doing these
corrections, including the ability to turn certain corrections off if
they are not needed.

.. `IsrTask <#>`_ will link to the API page when it's made

This task is implemented in the `lsst.ip.isr`_ module.

.. _`lsst.ip.isr`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1ip_1_1isr.html

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

    `API Usage <#>`_: *[To be filled in, like in charimg case]*

.. We will have a link to a separate page here called apiUsage_isrtask.rst

Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	`assembleCcd` , AssembleCcdTask ,  CCD assembly task
	`fringe` ,  FringeTask , Fringe subtraction task
 
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doBias`, `bool`,   `True`,  Apply bias frame correction?
   `doDark`, `bool`,   `True`,  Apply dark frame correction?
   `doFlat`, `bool`,   `True`,  Apply flat field correction?
   `doFringe`, `bool`,   `True`,  Apply fringe correction?
   `doWrite`, `bool`,   `True`,  Persist postISRCCD?
   `gain`, `float`,   ``float("NaN")``,  The gain to use if no Detector is present in the Exposure (ignored if NaN)
   `readNoise`, `float`,   ``0.0``,  The read noise to use if no Detector is present in the Exposure
   `saturation`, `float`,   ``float("NaN")``,  The saturation level to use if no Detector is present in the Exposure (ignored if NaN)
   `fringeAfterFlat`, `bool`,   `True`,  Do fringe subtraction after flat   fielding?
   `fwhm`, `float`,   ``1.0``,  FWHM of PSF (arcsec)
   `saturatedMaskName`, `str`,   ``"SAT"``,  Name of mask plane to use in saturation detection and interpolation
   `flatUserScale`, `float`,   ``1.0``,  If flatScalingType is 'USER' then scale flat by this amount; ignored otherwise
   `overscanOrder`, `int`,   ``1``,  Order of polynomial or to fit if overscan fit type is a polynomial
   `overscanRej`, `float`,   ``3.0``,  Rejection threshold (sigma) for collapsing overscan before fit
   `growSaturationFootprintSize`, `int`,   ``1``,  Number of pixels by which to grow the saturation footprints
   `fluxMag0T1`, `float`,   ``1.0e10``,  The approximate flux of a zero   magnitude object in a one-second exposure
   `setGainAssembledCcd`, `bool`,   `True`,  update exposure metadata in the assembled ccd to reflect the effective gain of the assembled chip
   `doAssembleIsrExposures`, `bool`,   `False`,  Assemble amp-level calibration exposures into ccd-level exposure?
   `doAssembleCcd`, `bool`,   `True`,  Assemble amp-level exposures into a ccd-level exposure?
   `doBrighterFatter`, `bool`,   `False`,  Apply the brighter fatter correction
   `brighterFatterKernelFile`, `str`,   ``empty string``,  Kernel file used for the brighter fatter correction
   `brighterFatterMaxIter`, `int`,   ``18``,  Maximum number of iterations for the brighter fatter correction
   `brighterFatterThreshold`, `float`,   ``1000.0``,  Threshold used to stop iterating the brighter fatter correction.  It is the absolute value of the difference between the current corrected image and the one from the previous iteration summed over all the pixels.
   `brighterFatterApplyGain`, `bool`,   `True`,  Should the gain be applied when applying the brighter fatter correction?
   `datasetType`, `str`,   ``"raw"``,  Dataset type for input data; users will typically leave this alone
   `fallbackFilterName`, `str`,  no default,  Fallback default filter name for calibrations
   `suspectMaskName`, `str`,  ``"SUSPECT"``, Name of mask plane to use for suspect pixels
   `flatScalingType`, `str`,  ``"USER"``, The method for scaling the flat on the fly; allowed values:	- "USER": "Scale by flatUserScale"	-          "MEAN": "Scale by the inverse of the mean"        -           "MEDIAN": "Scale by the inverse of the median" 
   `keysToRemoveFromAssembledCcd`, `str`,   ``empty list``, Fields to remove from the metadata of the assembled ccd
   `doLinearize`, `str`,  `True`, Correct for nonlinearity of the detector's response?
   `fallbackFilterName`, `str`, no default, Fallback default filter name for calibrations
   `overscanFitType`, `str`,  ``"MEDIAN"``, The method for fitting the overscan bias level; allowed values:	- ``"POLY"``: Fit ordinary polynomial to the longest axis of the overscan region	-        ``"CHEB"``: Fit Chebyshev polynomial to the longest axis of the overscan region	-  ``"LEG"``: Fit Legendre polynomial to the longest axis of the overscan region        -    ``"NATURAL_SPLINE"``: Fit natural spline to the longest axis of the overscan region        -   ``"CUBIC_SPLINE"``: Fit cubic spline to the longest axis of the overscan region        -  ``"AKIMA_SPLINE"``: Fit Akima spline to the longest axis of the overscan region        -  ``"MEAN"``: Correct using the mean of the overscan region        -  ``"MEDIAN"``: Correct using the median of the overscan region

Python usage
============
 
Class initialization
--------------------

.. code-block:: python
		
  lsst.ip.isr.isrTask.IsrTask(
 	*args,
 	**kwargs)
   
Parameters
^^^^^^^^^^

`*args`
  A list of positional arguments passed on to the Task constructor
`**kwargs`
  A dictionary of keyword arguments passed on to the Task constructor. Call the `lsst.pipe.base.task.Task.__init__`_ method, then setup the assembly and fringe correction subtasks.

.. _`lsst.pipe.base.task.Task.__init__`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1task_1_1_task.html#a1773a024121ed2ce7294509b3e8b40e8

Run method
----------
 
.. code-block:: python
  
	run(self,
 	ccdExposure,
 	bias = None,
 	linearizer = None,
 	dark = None,
 	flat = None,
 	defects = None,
 	fringes = None,
 	bfKernel = None)

The required inputs to the `run`_ method are the exposure to be corrected
(which will be of `datasetType <#>`_  `raw <#>`_) and the calibration
data products. The raw input is a single chip-sized mosaic of all amps
including overscans and other non-science pixels.

.. We want to eventually link these to pages explaining the different kinds datatypes available
   	
(More information can be found at `run`_, and at `this Confluence page`_)

.. _`run`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#aab476cefa23d730451f39119e04875d5  

.. _`this Confluence page`: https://confluence.lsstcorp.org/pages/viewpage.action?spaceKey=~hchiang2&title=Notes+on+existing+pipeline+components

Parameters
^^^^^^^^^^

`ccdExposure` -  `lsst.afw.image.exposure <#>`_ of detector data

.. We want to eventually link this to a page explaining the different kinds of exposures accessible in the afw.image pkg
   
`bias` -  Exposure of bias frame
  
`linearizer` -  Linearizing functor; a subclass of `lsst.ip.isr.LinearizeBase`_

.. _`lsst.ip.isr.LinearizeBase`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1linearize_1_1_linearize_base.html

`dark` -  Exposure of dark frame

`flat` -  Exposure of flatfield
  
`defects` -  List of detects
  
`fringes` -  A pipeBase.Struct with field fringes containing exposure of fringe frame or list of fringe exposure
  
`bfKernel`	- Kernel for brighter-fatter correction


Returns
^^^^^^^

``struct`` -   `lsst.pipe.base.Struct`_ with field: `exposure` (i.e. `lsst.afw.image.exposure <#>`_  specifically of type `postISRCCD <#>`_.)

.. We want to eventually link this to a page explaining the different kinds of exposures accessible in the afw.image pkg, and the different kinds datatypes available   

.. _`lsst.pipe.base.Struct`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1struct_1_1_struct.html


Debugging
=========

- `display` - A dictionary containing debug point names as keys with frame number as value.  The only valid key is:

  `postISRCCD` (to display exposure after ISR has been applied)

See `lsstDebug.info`_ for more on the debugging framework.

.. _`lsstDebug.info`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_debug_1_1_info.html

Examples
========

.. This example is not working in the current stack (see https://jira.lsstcorp.org/browse/DM-9197)  --- 2/9/2017
   

To see an example of the ISR algorithm in action, run the
example in the `$IP_ISR_DIR/examples` as follows:

.. code-block:: python
		
  python  runIsrTask.py --write --ds9

The optional `--write` flag tells the code to write the post-ISR image
file to disk.  In this example code, this output file is called::

   postISRCCD.fits

The optional `--ds9` flag tells it to bring up the ds9 image viewer (if installed) and show the post-ISR image.

As an overview: what this example does after setting up the parameter
configuration, is to make several calibration exposures that will be
used to create the final corrected output exposure.  Finally, the
output is produced by using the `run`_ function of `IsrTask <#>`_ ,
after ingesting the raw exposure and the calibration exposures and
processing them.


Stepping through the example:

First the task is imported along with `exampleUtils.py`, a local
modification of `utils.py` which will provide some needed utility
functions:

.. code-block:: python
		
  from lsst.ip.isr import IsrTask
  import exampleUtils

Next, a function `runIsr` is defined which sets several config parameters as so:

.. code-block:: python
		
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

Next, several parameters that will be used to make the raw, flat and
dark exposures are defined, using knowledge of our camera and exposures::

    DARKVAL = 2.0      # Number of electrons per sec
    OSCAN = 1000.      # DN = Data Number, same as the standard ADU
    GRADIENT = 0.10
    EXPTIME = 15       # Seconds for the science exposure
    DARKEXPTIME = 40.0 # Seconds for the dark exposure

Next, the 3 calibration exposures that we will be using in this
example to create the final corrected output exposure are created
using the functions in the extra included utility file::

    darkExposure = exampleUtils.makeDark(DARKVAL, DARKEXPTIME)
    flatExposure = exampleUtils.makeFlat(GRADIENT)
    rawExposure = exampleUtils.makeRaw(DARKVAL, OSCAN, GRADIENT, EXPTIME)

In order to perform overscanCorrection `IsrTask.run()` requires
`Exposures` which have a `lsst.afw.cameraGeom.Detector`. Detector objects
describe details such as data dimensions, number of amps, orientation
and overscan dimensions. If requesting images from the `Butler <#>`_,
Exposures will automatically have detector information. If running
`IsrTask <#>`_ on arbitrary images from a camera without an `obs_` package, a
`lsst.afw.cameraGeom.Detector` can be generated using
`lsst.afw.cameraGeom.fitsUtils.DetectorBuilder` and set by calling::

     rawExposure.setDetector(myDetectorObject)

.. Butler: we'll link to this in a glossary, minimally
     
See `lsst.afw.cameraGeom.fitsUtils.DetectorBuilder`_ for more details.

.. _`lsst.afw.cameraGeom.fitsUtils.DetectorBuilder`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1afw_1_1camera_geom_1_1fits_utils_1_1_detector_builder.html

Finally, the output is produced with the line::

       output = isrTask.run(rawExposure, dark=darkExposure, flat=flatExposure)

And returned at the end of the function.

(The `main` function of runIsrTask simply calls this `run` function,
and as noted earlier, also brings up ds9 to view the final output
exposure if that flag is set on, and writes the image to diskif that
flag is set.)
	    

Algorithm details
====================

`IsrTask <#>`_ performs instrument signature removal on an exposure in
varying ways depending on which corrections need to be applied to the
raw image, but generally some combination of at least the following is
done:

`Bias subtraction`: removing the pedestal introduced by the instrument
for a zero-second exposure.  The bias correction is applied to remove
the additive electronic bias that is present in the signal chain. To
first approximation, the bias is a constant pedestal, but it has
low-amplitude structure that is related to its electronic stability
during read-out of the detector segment. The processing pipeline
removes the bias contribution in a two-step process. In the first
step, the median value of non-flagged pixels in the overscan region is
subtracted from the image. In the second step, the reference bias
image is subtracted from the science image to remove the higher-order
structure.  Following the bias correction, the pixels are scaled by
the gain factor for the appropriate CCD. The brightness units are
electrons (or equivalently for unit gain, detected photons) for
calibrated images.


`Dark correction`: this is done by subtracting a reference
dark calibration frame that has been scaled to the exposure time of
the visit image.


`Linearity Correction`: The response of the CCD detectors to radiation
is highly linear for pixels that are not near saturation, to typically
better than 0.1% for most recent cameras.  Thus, currently, no
linearity correction is applied in the DM pipelines. Were a correction
necessary it would likely be implemented with a look-up table, and
executed following the dark correction but prior to fringe correction.

`Flat-fielding`: Flat-fielding corrects approximately for vignetting
across the CCD (i.e. the variation in the amount of light that hits
the detector due to angle of incidence into the aperture at the top of
the telescope tube, and the resultant shadow from one side). The
flat-field correction is performed by dividing each science frame by a
normalized, reference flat-field image for the corresponding filter.

`Brighter fatter correction`: i.e. accounting for the distortion of
the electric field lines at the bottom of pixels when bright objects
liberate many charges that get trapped at the bottom of the potential
wells.  The Brighter-Fatter Correction is the standard name given to
the correction because a pixel tower 'fills up' with electrons at the
bottom of the silicon layer when many photons hit the top of the
detector, altering the normal electric field lines set up to trap all
the electrons liberated from normal photon hits in that tower, and
forcing some of the resultant electrons into neighboring pixels.  This
requires careful treatment to correct for, and the currently
implemented model is a fairly advanced one that takes a kernel that
has been derived from flat field images to redistribute the charge.
(The default DMS method in particular is described in substantial
detail `here`_, and also even further in a currently internal report
by Coulton, Lupton, Smith and Spergel from 4-14-2015 and in references
listed therein.)

.. Need to be able to at least give the internal link for theier report, and ultimately want to somehow make this report public so anyone can get to it.
   
.. _`here`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1isr_task_1_1_isr_task.html#abcef49896d412c901f42e960dce9e280


`Saturation Correction`: At the start of pipeline processing the pixel
values are examined to detect saturation (which will naturally also
identify bleed trails near saturated targets, and the strongest cosmic
rays). These values, along with pixels that are identified in the list
of static bad pixels, are flagged in the data quality mask of the
science image.  All pixels in the science array identified as “bad” in
this sense are interpolated over, in order to avoid problems with
source detection and with code optimization for other downstream
pipeline processing.  Interpolation is performed with a linear
predictive code, as was done for the Sloan Digital Sky Survey
(SDSS). The PSF is taken to be a Gaussian with sigma width equal to
one pixel when deriving the coefficients. For interpolating over most
defects the interpolation is only done in the x-direction, extending 2
pixels on each side of the defect. This is done both for simplicity
and to ameliorate the way that saturation trails interact with bad
columns.

  
  
*[Need specific input from developers on what to insert for algorithmic details here.]*

[Extra reference: Section 4 of LSST DATA CHALLENGE HANDBOOK (2011) [https://project.lsst.org/sciencewiki/images/DC_Handbook_v1.1.pdf] , and http://hsca.ipmu.jp/public/index.html ]

  
