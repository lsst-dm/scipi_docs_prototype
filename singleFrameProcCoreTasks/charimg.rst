
#####################
CharacterizeImageTask
#####################

Given an exposure with defects repaired (masked and interpolated over,
e.g. as output by :doc:`IsrTask <isrtask>`), this task does initial
source extraction and PSF estimation.


Its primary functions are to:

  - Detect and measure bright sources

  - Repair cosmic rays

  - Measure and subtract background

  - Measure the PSF


This task is implemented in the `lsst.pipe.tasks`_ module.

.. _`lsst.pipe.tasks`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_tasks.html

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.
    
Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	``background``,  SubtractBackgroundTask,    Configuration for initial background estimation
	``detection``,  SourceDetectionTask, Detect sources
	``deblend``,  SourceDeblendTask, Split blended source into their components
	``measurement``,  SingleFrameMeasurementTask, Measure sources
	``measureApCorr``,   MeasureApCorrTask, Subtask to measure aperture corrections
	``applyApCorr``,  ApplyApCorrTask, Subtask to apply aperture corrections
	``catalogCalculation``,  CatalogCalculationTask, Subtask to run catalogCalculation plugins on catalog
	``installSimplePsf``,   InstallGaussianPsfTask, Install a simple PSF model
	``refObjLoader``,   LoadAstrometryNetObjectsTask, Reference object loader
	``astrometry``,  AstrometryTask, Task to load and match reference objects. Only used if `measurePsf` can use matches. Warning: matching will only work well if the initial WCS is accurate enough to give good matches (roughly: good to 3 arcsec across the CCD).
	``measurePsf``,  MeasurePsfTask, Measure PSF
	``repair``,   RepairTask, Remove cosmic rays
 


Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   ``doDeblend``, (`bool`),  `True`, Run deblender on input exposure?
   ``doApCorr``, (`bool`),  `True`,  Run subtasks to measure and apply aperture corrections
   ``doMeasurePsf``, (`bool`),  `True`, Measure the PSF? If `False` then keep the existing PSF model (which must exist) and use that model for all operations."
   ``doWrite``, (`bool`),  `True`, Persist results?
   ``doWriteExposure``, (`bool`),  `True`, Write icExp and icExpBackground in addition to icSrc? Ignored if doWrite False.
   ``useSimplePsf``, (`bool`),  `True`, Replace the existing PSF model with a simplified version that has the same sigma at the start of each PSF determination iteration? Doing so makes PSF determination converge more robustly and quickly.
   ``psfIterations``, (`int`),  2; min=1,    Number of iterations of doing: detect sources; measure sources; estimate PSF. If `useSimplePsf = True` then 2 should be plenty; otherwise more may be wanted.
   ``checkUnitsParseStrict``,  (`str`), `raise`, Strictness of Astropy unit compatibility check.  Can be 'raise'; 'warn'; 'silent'

Entrypoint
==========

- `lsst.pipe.tasks.characterizeImage.CharacterizeImageTask.run`_

.. _`lsst.pipe.tasks.characterizeImage.CharacterizeImageTask.run`:   https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#a2db834efb17f00355c46daf26de7ceb5
  
If you want this task to unpersist inputs or persist outputs, then call the `run`_ method (which is a thin wrapper around the `characterize`_ method).

.. _`characterize`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#a4623ec66f58fc90b0ed09a019410ac46

.. _`run`:   https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#a2db834efb17f00355c46daf26de7ceb5

If you already have the inputs unpersisted and do not want to persist the output then it is more direct to call the `characterize`_ method directly.



Butler Inputs
=============

A butler object is passed to the `refObjLoader` constructor in case it
is needed to load catalogs. It may be `None` if a catalog-based star
selector is not used, if the reference object loader constructor does
not require a butler, or if a reference object loader is passed
directly via the `refObjLoader` argument.

Butler Outputs
==============

Output catalogs are of type ``icSrc``.

Examples
========

Note: running this example currently requires that over and above the DM Stack installation, `afwdata`_ is installed and set up (via the EUPS `setup <https://dev.lsstcorp.org/trac/wiki/EupsTutorial>`_ command).

.. _`afwdata`: https://github.com/lsst/afwdata

This example script is ``calibrateTask.py`` (which calls this function (``CharacterizeImageTask``) before calling :doc:`CalibrateTask <calibimg>`) in the ``$PIPE_TASKS/examples`` directory, and can be run from the command line as, e.g.:

.. code-block:: python
  
     python examples/calibrateTask.py -display

Where the `-display` flag tells the script to bring up the display tool to show the image files after each step.
     
The first thing the example does is import the task (there are some other standard imports as well that are not extracted out here):

.. code-block:: python
		
    from lsst.pipe.tasks.characterizeImage import CharacterizeImageTask

The script next processes the data. This occurs in two steps:

- Characterize the image: measure bright sources, fit a background and PSF, and repairs cosmic rays

.. code-block:: python
		
     exposure = loadData()
     exposureIdInfo = ExposureIdInfo(expId=1, expBits=5)
 
     # characterize the exposure to repair cosmic rays and fit a PSF model
     # display now because CalibrateTask modifies the exposure in place
     charRes = charImageTask.characterize(exposure=exposure, exposureIdInfo=exposureIdInfo)
     if display:
         displayFunc(charRes.exposure, charRes.sourceCat, frame=1)

- Calibrate the exposure: measure faint sources, fit an improved WCS and photometric zero-point
		
.. code-block:: python

   
    # calibrate the exposure
    calRes = calibrateTask.calibrate(exposure=charRes.exposure, exposureIdInfo=exposureIdInfo)
    if display:
        displayFunc(calRes.exposure, calRes.sourceCat, frame=2)

To round out this minimal description, the `displayFunc` that is called above in the blocks is defined as so:

.. code-block:: python
		
 def displayFunc(exposure, sourceCat, frame):
    display = afwDisplay.getDisplay(frame)
    display.mtv(exposure)

    with display.Buffering():
        for s in sourceCat:
            xy = s.getCentroid()
            display.dot('+', *xy, ctype=afwDisplay.CYAN if s.get("flags_negative") else afwDisplay.GREEN)
	
     

Debugging
=========

.. csv-table:: 
   :header: Parameter, Type, Description
   :widths: 10, 5, 50


        ``frame``, (`int`), if specified: the frame of first debug image displayed (defaults to 1)	    
        ``repair_iter``, (`bool`),  if `True` display image after each repair in the measure PSF loop
	``background_iter``, (`bool`),  if `True` display image after each background subtraction in the measure PSF loop
	``measure_iter``, (`bool`),  if `True` display image and sources at the end of each iteration of the measure PSF loop.  `lsst.meas.astrom.display.displayAstrometry`_  for the meaning of the various symbols.
	``psf``, (`bool`),  if `True` display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true
	``repair``, (`bool`),  if `True` display image and sources after final repair
	``measure``, (`bool`),  if `True` display image and sources after final measurement

.. _`lsst.meas.astrom.display.displayAstrometry`:  https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1meas_1_1astrom_1_1display.html#aba98ee54d502f211b69ff35db4d36f94

 


Algorithm details
=================

The way characterizeImage works is to estimate initial background
since this will be needed to make basic photometric measurements.

It then does a straight subtraction of this background from the image
itself, pixel by pixel, which is a necessary prerequisite to
extracting out the actual objects in the image.

Further, a PSF is determined iteratively, detecting and removing
defects like cosmic rays, and then using the increased number of
actual sources detected to better determine the PSF.


