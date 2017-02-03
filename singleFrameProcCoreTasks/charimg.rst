
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

    API Usage: See :doc:`CharacterizeImageTask API <apiUsage_charimg>`

Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	`background`,  SubtractBackgroundTask,    Configuration for initial background estimation
	`detection`,  SourceDetectionTask, Detect sources
	`deblend`,  SourceDeblendTask, Split blended source into their components
	`measurement`,  SingleFrameMeasurementTask, Measure sources
	`measureApCorr`,   MeasureApCorrTask, Subtask to measure aperture corrections
	`applyApCorr`,  ApplyApCorrTask, Subtask to apply aperture corrections
	`catalogCalculation`,  CatalogCalculationTask, Subtask to run catalogCalculation plugins on catalog
	`installSimplePsf`,   InstallGaussianPsfTask, Install a simple PSF model
	`refObjLoader`,   LoadAstrometryNetObjectsTask, Reference object loader
	`astrometry`,  AstrometryTask, Task to load and match reference objects. Only used if `measurePsf` can use matches. Warning: matching will only work well if the initial WCS is accurate enough to give good matches (roughly: good to 3 arcsec across the CCD).
	`measurePsf`,  MeasurePsfTask, Measure PSF
	`repair`,   RepairTask, Remove cosmic rays
 


Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doDeblend`, `bool`,  `True`, Run deblender on input exposure?
   `doApCorr`, `bool`,  `True`,  Run subtasks to measure and apply aperture corrections
   `doMeasurePsf`, `bool`,  `True`, Measure the PSF? If `False` then keep the existing PSF model (which must exist) and use that model for all operations."
   `doWrite`, `bool`,  `True`, Persist results?
   `doWriteExposure`, `bool`,  `True`, Write icExp and icExpBackground in addition to icSrc? Ignored if doWrite False.
   `useSimplePsf`, `bool`,  `True`, Replace the existing PSF model with a simplified version that has the same sigma at the start of each PSF determination iteration? Doing so makes PSF determination converge more robustly and quickly.
   `psfIterations`, `int`,  2 ,    Number of iterations of doing: detect sources; measure sources; estimate PSF. If `useSimplePsf = True` then 2 should be plenty; otherwise more may be wanted. `Min=1`.
   `checkUnitsParseStrict`,  `str`, `raise`, Strictness of Astropy unit compatibility check.  Can be 'raise'; 'warn'; 'silent'


Python usage
============
 
Class initialization
--------------------

.. code-block:: python

   lsst.pipe.tasks.characterizeImage.CharacterizeImageTask(
 	butler = None,
 	refObjLoader = None,
 	schema = None,
 	**kwargs)

Parameters
^^^^^^^^^^

`butler`
  A butler object is passed to the refObjLoader constructor in case it is needed to load catalogs. May be None if a catalog-based star selector is not used, if the reference object loader constructor does not require a butler, or if a reference object loader is passed directly via the refObjLoader argument.
`refObjLoader`
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog to a catalog-based star selector. May be None if a catalog star selector is not used or the loader can be constructed from the butler argument.
`schema`
  Initial schema (an `lsst.afw.table.SourceTable <#>`_), or None
`kwargs`
  Other keyword arguments for `lsst.pipe.base.CmdLineTask`_

.. _`lsst.pipe.base.CmdLineTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html

.. sourcetable above: We want to eventually link this to a descrip of what the afw.table.SourceTable obj is

Run method
----------
 
.. code-block:: python

  run(dataRef,
      exposure = None,
      background = None,
      doUnpersist = True )		

The required input to the `run` method is the exposure to be characterized, and an optional input is an initial model of background which has already subtracted from exposure.


Parameters
^^^^^^^^^^


`dataRef`
  Butler data reference for science exposure

`exposure`
  Exposure to characterize (an `lsst.afw.image.ExposureF`_ or similar). If None then unpersist from "postISRCCD". The following changes are made, depending on the config:

.. _`lsst.afw.image.ExposureF`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1afw_1_1image.html

  - set psf to the measured PSF

  - set `apCorrMap` to the measured aperture correction
    
  - subtract background

  - interpolate over cosmic rays

  - update detection and cosmic ray mask planes

`background`
  Initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList`_). May be `None` if no background has been subtracted, which is typical for image characterization. A refined background model is output.

.. _`lsst.afw.math.BackgroundList`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1afw_1_1math.html

.. There is not an exact BackgroundList obj in lsst.afw.math, but several similar type objs (?)

`doUnpersist`
  If `True` the exposure is read from the repository and the exposure and background arguments must be None; if `False` the exposure must be provided. `True` is intended for running as a command-line task, `False` for running as a subtask

Returns
^^^^^^^

A pipe_base Struct containing these fields, all from the final iteration of :doc:`detectMeasureAndEstimatePsf <apiUsage_charimg>`:

`exposure`: characterized exposure; image is repaired by interpolating over cosmic rays, mask is updated accordingly, and the PSF model is set

`sourceCat`: detected sources (an `lsst.afw.table.SourceCatalog <#>`_)

.. We want to eventually link this to a descrip of the available types of catalogs in afw.table
.. Does it matter at this point to user that output catalogs are of type `icSrc <#>` ?
.. We want to eventually link this to a page with a descrip of the available types of catalogs
   
`background`: model of background subtracted from exposure (an `lsst.afw.math.BackgroundList`_)

`psfCellSet`: spatial cells of PSF candidates (an `lsst.afw.math.SpatialCellSet`_)

.. _`lsst.afw.math.SpatialCellSet`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1afw_1_1math_1_1_spatial_cell_set.html

Entrypoint
==========

- `lsst.pipe.tasks.characterizeImage.CharacterizeImageTask.run`_

.. _`lsst.pipe.tasks.characterizeImage.CharacterizeImageTask.run`:   https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#a2db834efb17f00355c46daf26de7ceb5
  
If you want this task to `unpersist <#>`_ inputs or `persist <#>`_ outputs, then call the `run`_ method (which is a thin wrapper around the :doc:`characterize <apiUsage_charimg>` method).
.. We will link to pages that explain these terms more technically
.. _`run`:   https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#a2db834efb17f00355c46daf26de7ceb5

If you already have the inputs `unpersisted <#>`_ and do not want to `persist <#>`_ the output then it is more direct to call the :doc:`characterize <apiUsage_charimg>` method directly.






Debugging
=========

.. csv-table:: 
   :header: Parameter, Type, Description
   :widths: 10, 5, 50


        `frame`, `int`, if specified: the frame of first debug image displayed (defaults to 1)	    
        `repair_iter`, `bool`,  if `True` display image after each repair in the measure PSF loop
	`background_iter`, `bool`,  if `True` display image after each background subtraction in the measure PSF loop
	`measure_iter`, `bool`,  if `True` display image and sources at the end of each iteration of the measure PSF loop.  See `lsst.meas.astrom.display.displayAstrometry`_  for the meaning of the various symbols.
	`psf`, `bool`,  if `True` display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true
	`repair`, `bool`,  if `True` display image and sources after final repair
	`measure`, `bool`,  if `True` display image and sources after final measurement

.. _`lsst.meas.astrom.display.displayAstrometry`:  https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1meas_1_1astrom_1_1display.html#aba98ee54d502f211b69ff35db4d36f94

See `lsstDebug.info`_ for more on the debugging framework.

.. _`lsstDebug.info`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_debug_1_1_info.html 



Examples
========

Note: running this example currently requires that over and above the DM Stack installation, `afwdata`_ is installed and set up (via the EUPS `setup <https://dev.lsstcorp.org/trac/wiki/EupsTutorial>`_ command).
.. This is a general link to the EUPS tutorial, but setup is explained in there
.. _`afwdata`: https://github.com/lsst/afwdata

This example script is `calibrateTask.py` (which calls this function `CharacterizeImageTask`) before calling :doc:`CalibrateTask <calibimg>` in the `$PIPE_TASKS/examples` directory, and can be run from the command line as, e.g.:

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


*[Need specific input from developers on what to insert for algorithmic details here.]*
