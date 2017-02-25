#######
IsrTask 
#######

Instrument Signature Removal (ISR) is a sequence of steps taken to
correct the effects imprinted on the counts coming out of the readout
by the physical characteristics of the detector and the electronics of
the readout chain.  It is generally the very first procedure carried
out on the pixel-level data of an exposure.

In more detail, though the process for correcting imaging data is very
similar from camera to camera, it will vary to some degree depending
on which of the various effects are present and need to be corrected
for.  Generally these corrections are done one CCD at a time, but on
all the amplifier sub-images at once for a CCD.  `IsrTask` provides a
generic implementation of doing these corrections, including the
ability to turn certain corrections off.

Further, `IsrTask` optionally calls a subtask to trim and assemble the
amplifier subimages into a single full CCD image ready for the next
steps of image characterization and calibration.

This task is implemented in the `lsst.ip.isr <taskModules.html#ipisr>`_ module.


.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

    API Usage: See :doc:`IsrTask API <apiUsage_isrtask>`


Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	`assembleCcd` , `AssembleCcdTask <taskModules.html#assembleccd>`_ ,  CCD assembly task
	`fringe` ,  `FringeTask <taskModules.html#fringetask>`_ , Fringe subtraction task
 
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doBias`, `bool`,   ``True``,  Apply bias frame correction?
   `doDark`, `bool`,   ``True``,  Apply dark frame correction?
   `doFlat`, `bool`,   ``True``,  Apply flat field correction?
   `doFringe`, `bool`,   ``True``,  Apply fringe correction?
   `doWrite`, `bool`,   ``True``,  Persist `postISRCCD`_?
   `gain`, `float`,   ``float("NaN")``,  The gain to use if no Detector is present in the Exposure (ignored if NaN)
   `readNoise`, `float`,   ``0.0``,  The read noise to use if no Detector is present in the Exposure
   `saturation`, `float`,   ``float("NaN")``,  The saturation level to use if no Detector is present in the Exposure (ignored if NaN)
   `fringeAfterFlat`, `bool`,   ``True``,  Do fringe subtraction after flat   fielding?
   `fwhm`, `float`,   ``1.0``,  FWHM of PSF (arcsec)
   `saturatedMaskName`, `str`,   ``"SAT"``,  Name of mask plane to use in saturation detection and interpolation
   `flatUserScale`, `float`,   ``1.0``,  If flatScalingType is 'USER' then scale flat by this amount; ignored otherwise
   `overscanOrder`, `int`,   ``1``,  Order of polynomial or to fit if overscan fit type is a polynomial
   `overscanRej`, `float`,   ``3.0``,  Rejection threshold (sigma) for collapsing overscan before fit
   `growSaturationFootprintSize`, `int`,   ``1``,  Number of pixels by which to grow the saturation footprints
   `fluxMag0T1`, `float`,   ``1.0e10``,  The approximate flux of a zero   magnitude object in a one-second exposure
   `setGainAssembledCcd`, `bool`,   ``True``,  update exposure metadata in the assembled ccd to reflect the effective gain of the assembled chip
   `doAssembleIsrExposures`, `bool`,   ``False``,  Assemble amp-level calibration exposures into ccd-level exposure?
   `doAssembleCcd`, `bool`,   ``True``,  Assemble amp-level exposures into a ccd-level exposure?
   `doBrighterFatter`, `bool`,   ``False``,  Apply the brighter fatter correction
   `brighterFatterKernelFile`, `str`,   ``empty string``,  Kernel file used for the brighter fatter correction
   `brighterFatterMaxIter`, `int`,   ``18``,  Maximum number of iterations for the brighter fatter correction
   `brighterFatterThreshold`, `float`,   ``1000.0``,  Threshold used to stop iterating the brighter fatter correction.  It is the absolute value of the difference between the current corrected image and the one from the previous iteration summed over all the pixels.
   `brighterFatterApplyGain`, `bool`,   ``True``,  Should the gain be applied when applying the brighter fatter correction?
   `datasetType`, `str`,   ``"raw"``,  Dataset type for input data; users will typically leave this alone
   `fallbackFilterName`, `str`,  no default,  Fallback default filter name for calibrations
   `suspectMaskName`, `str`,  ``"SUSPECT"``, Name of mask plane to use for suspect pixels
   `keysToRemoveFromAssembledCcd`, `str`,   ``empty list``, Fields to remove from the metadata of the assembled ccd
   `doLinearize`, `str`,  ``True``, Correct for nonlinearity of the detector's response?
   `fallbackFilterName`, `str`, no default, Fallback default filter name for calibrations



.. raw:: html
	 
  <table border="1" class="colwidth-given docutils">
     <colgroup>
       <col width="31%">
       <col width="9%">
       <col width="15%">
       <col width="46%">
     </colgroup>
     <tbody valign="top">
       <tr class="row-even">
         <td>
           <code class="xref py py-obj docutils literal">flatScalingType</code>
         </td>
         <td>
           <b>  <a href="https://docs.python.org/2/library/functions.html#str">str</a></b>
         </td>
         <td>
        	 <code> "USER" </code>
	 </td>
        <td>
	<p> The method for scaling the flat on the fly; allowed values:
	</p> 
          <ul>
            <li> <code>  "USER"  </code> : Scale by flatUserScale
	    <li> <code>  "MEAN" </code>: Scale by the inverse of the mean
	    <li> <code>  "MEDIAN" </code>: Scale by the inverse of the median
	  </ul>
         </td>
       </tr>
       <tr class="row-odd">
         <td>
           <code class="xref py py-obj docutils literal">overscanFitType</code>
         </td>
         <td>
          <b>  <a href="https://docs.python.org/2/library/functions.html#str">str</a> </b>
         </td>
         <td>
        	 <code> "MEDIAN" </code>
	 </td>
         <td>
	 <p>
	  The method for fitting the overscan bias level; allowed values:
	 </p>
	 <ul>
	   <li>  <code>"POLY"</code>: Fit ordinary polynomial to the longest axis of the overscan region
	   <li>  <code>"CHEB"</code>: Fit Chebyshev polynomial to the longest axis of the overscan region
	   <li>  <code>"LEG"</code>: Fit Legendre polynomial to the longest axis of the overscan region
	   <li>  <code>"NATURAL_SPLINE"</code>: Fit natural spline to the longest axis of the overscan region
	   <li>  <code>"CUBIC_SPLINE"</code>: Fit cubic spline to the longest axis of the overscan region
	   <li>  <code>"AKIMA_SPLINE"</code>: Fit Akima spline to the longest axis of the overscan region
	   <li>  <code>"MEAN"</code>: Correct using the mean of the overscan region
	   <li>  <code>"MEDIAN"</code>: Correct using the median of the overscan region
	  </ul>
     </tbody>
   </table>



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
  A dictionary of keyword arguments passed on to the Task constructor. Call the `lsst.pipe.base.task.Task.__init__ <taskModules.html#pipebaseinit>`_ method, then setup the assembly and fringe correction subtasks.


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
(which will be of `datasetType`  `raw <LSSTglossary.html#raw`_) and the calibration
data products. The raw input is a single chip-sized mosaic of all amps
including overscans and other non-science pixels.

.. We want to eventually link these to pages explaining the different kinds datatypes available
   	
(More information can be found at `run <apiUsage_isrtask.html#run>`_)




Parameters
^^^^^^^^^^

`ccdExposure` -  `lsst.afw.image.exposure <LSSTglossary.html#exposure>`_ of detector data

`bias` -  Exposure of bias frame
  
`linearizer` -  Linearizing functor; a subclass of `lsst.ip.isr.LinearizeBase <taskModules.html#linbase>`_

`dark` -  Exposure of dark frame

`flat` -  Exposure of flatfield
  
`defects` -  List of detects
  
`fringes` -  A pipeBase.Struct with field fringes containing exposure of fringe frame or list of fringe exposure
  
`bfKernel`	- Kernel for brighter-fatter correction


Returns
^^^^^^^

``struct`` -   `lsst.pipe.base.Struct <objectClasses.html#structlink>`_ with field: `exposure` (i.e. `lsst.afw.image.exposure`_  specifically of type `postISRCCD <LSSTglossary.html#postisrccd>`_.)


Debugging
=========

- `display` - A dictionary containing debug point names as keys with frame number as value.  The only valid key is:

  `postISRCCD`_ (to display exposure after ISR has been applied)

See `lsstDebug.info <taskModules.html#info>`_ for more on the debugging framework.


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
output is produced by using the `run`_ function of `IsrTask` ,
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
and overscan dimensions. If requesting images from the `Butler <LSSTglossary.html#butlerlink>`_,
Exposures will automatically have detector information. If running
`IsrTask` on arbitrary images from a camera without an `obs_` package, a
`lsst.afw.cameraGeom.Detector` can be generated using
`lsst.afw.cameraGeom.fitsUtils.DetectorBuilder` and set by calling::

     rawExposure.setDetector(myDetectorObject)

See `lsst.afw.cameraGeom.fitsUtils.DetectorBuilder <taskModules.html#detbuild>`_ for more details.



Finally, the output is produced with the line::

       output = isrTask.run(rawExposure, dark=darkExposure, flat=flatExposure)

And returned at the end of the function.

(The `main` function of runIsrTask simply calls this `run` function,
and as noted earlier, also brings up ds9 to view the final output
exposure if that flag is set on, and writes the image to diskif that
flag is set.)
	    

Algorithm details
====================

We'll describe one effect as an example of the algorithms in the IsrTask corrections.

Brighter-Fatter Correction
--------------------------

Apply brighter fatter correction in place for the image

This correction takes a kernel that has been derived from flat field images to
redistribute the charge.  The gradient of the kernel is the deflection
field due to the accumulated charge.

Given the original image I(x) and the kernel K(x) we can compute the corrected image  Ic(x)
using the following equation:

:math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]`

To evaluate the derivative term we just use the product rule to expand it as follows:

:math:`{d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right] = {1 \over 2} \left[ \left( {d \over dx} I(x) \right) {d \over dx} \int (K(x-y) I(y) dy) + I(x) {d^2 \over dx^2} \int  K(x-y) I(y) dy \right]`

Because we use the measured counts instead of the incident counts we
apply the correction iteratively to reconstruct the original counts
and the correction.  We stop iterating when the summed difference
between the current corrected image and the one from the previous
iteration is below the threshold.  We do not require convergence
because the number of iterations is too large a computational cost.
How we define the threshold still needs to be evaluated, the current
default was shown to work reasonably well on a small set of images.

The edges as defined by the kernel are not corrected because they have spurious values
due to the convolution.

For more information on the method see a currently internal report by
Coulton, Lupton, Smith and Spergel from 4-14-2015 (DocuShare
Document-19407) and references listed therein.

  
*[Need specific input from developers on what to insert for algorithmic details here.]*

[Extra reference: Section 4 of LSST DATA CHALLENGE HANDBOOK (2011) [https://project.lsst.org/sciencewiki/images/DC_Handbook_v1.1.pdf] , and http://hsca.ipmu.jp/public/index.html ]
