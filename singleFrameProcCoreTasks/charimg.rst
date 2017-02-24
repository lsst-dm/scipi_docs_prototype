#####################
CharacterizeImageTask
#####################

Given an exposure that has been fully corrected for instrumental effects (e.g. as output by :doc:`IsrTask <isrtask>`), this task does initial
source extraction and an iterative algorithm to converge to the best possible PSF estimate across the image.

Its primary sub-function steps in the iterative effort to achieve the above are to:

  - Detect and measure bright sources

  - Repair cosmic rays

  - Measure and subtract background

  - Measure the PSF


This task is implemented in the `lsst.pipe.tasks <taskModules.html#pipetasks>`_ module.



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
	`astrometry`,  AstrometryTask, Task to load and match reference objects. Only used if `measurePsf` can use matches. *Warning*: matching will only work well if the initial WCS is accurate enough to give good matches (roughly: good to 3 arcsec across the CCD).
	`measurePsf`,  MeasurePsfTask, Measure PSF
	`repair`,   RepairTask, Remove cosmic rays
 


Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doDeblend`, `bool`,  ``True``, Run deblender on input exposure?
   `doApCorr`, `bool`,  ``True``,  Run subtasks to measure and apply aperture corrections
   `doMeasurePsf`, `bool`,  ``True``, Measure the PSF? If ``False`` then keep the existing PSF model (which must exist) and use that model for all operations.
   `doWrite`, `bool`,  ``True``, Persist results?
   `doWriteExposure`, `bool`,  ``True``, Write icExp and icExpBackground in addition to `icSrc <LSSTglossary.html#catalogs>`_? Ignored if doWrite is ``False``.
   `useSimplePsf`, `bool`,  ``True``, Replace the existing PSF model with a simplified version that has the same sigma at the start of each PSF determination iteration? Doing so makes PSF determination converge more robustly and quickly.
   `psfIterations`, `int`,  ``2`` ,    Number of iterations of doing: detect sources; measure sources; estimate PSF. If ``useSimplePsf = True`` then 2 should be plenty; otherwise more may be wanted. ``Min=1``.
   `checkUnitsParseStrict`,  `str`, ``"raise"``, Strictness of Astropy unit compatibility check.  Can be ``"raise"`` ``"warn"`` or ``"silent"``



   


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
  A butler object is passed to the refObjLoader constructor in case it is needed to load catalogs. May be ``None`` if a catalog-based star selector is not used, if the reference object loader constructor does not require a butler, or if a reference object loader is passed directly via the refObjLoader argument.
`refObjLoader`
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog to a catalog-based star selector. May be ``None`` if a catalog star selector is not used or the loader can be constructed from the butler argument.
`schema`
  Initial schema (an `lsst.afw.table.SourceTable <objectClasses.html#srctable>`_), or ``None``
`kwargs`
  Other keyword arguments for `lsst.pipe.base.CmdLineTask <CLTs.html#CLTbaseclass>`_



Run method
----------
 
.. code-block:: python

  run(dataRef,
      exposure = None,
      background = None,
      doUnpersist = True )		

The required input to the `run` method  (which is a thin wrapper around the :doc:`characterize <apiUsage_charimg>` method) is the exposure to be characterized, and an optional input is an initial model of background which has already subtracted from exposure.

If you want this task to `unpersist` inputs or `persist` outputs, then call the `run` method, however, if you already have the inputs `unpersisted` and do not want to `persist` the output then it is more direct to call the :doc:`characterize <apiUsage_charimg>` method straight off.

.. We will link to pages that explain the persistence terms more technically



Parameters
^^^^^^^^^^


`dataRef`
  `Butler <LSSTglossary.html#butlerlink>`_ data reference for science exposure


`exposure`
  Exposure to characterize (an `lsst.afw.image.ExposureF <LSSTglossary.html#exposureF>`_ or similar). If ``None`` then unpersist from `postISRCCD<LSSTglossary.html#postisrccd>`_. The following changes are made, depending on the config:

  - set psf to the measured PSF

  - set `apCorrMap` to the measured aperture correction
    
  - subtract background

  - interpolate over cosmic rays

  - update detection and cosmic ray mask planes

`background`
  Initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList <LSSTglossary.html#bkgdlist>`_). May be ``None`` if no background has been subtracted, which is typical for image characterization. A refined background model is output.

`doUnpersist`
  If ``True`` the exposure is read from the repository and the exposure and background arguments must be ``None``; if ``False`` the exposure must be provided. ``True`` is intended for running as a command-line task, ``False`` for running as a subtask

Returns
^^^^^^^

A pipe_base Struct containing these fields, all from the final iteration of `detectMeasureAndEstimatePsf <apiUsage_charimg.html#detlink>`:

`exposure`: characterized exposure; image is repaired by interpolating over cosmic rays, mask is updated accordingly, and the PSF model is set

`sourceCat`: detected sources (an `lsst.afw.table.SourceCatalog`)

.. We want to eventually link this to a descrip of the available types of catalogs in afw.table
.. Does it matter at this point to user that output catalogs are of type `icSrc` ?

   
`background`: model of background subtracted from exposure (an `lsst.afw.math.BackgroundList`_)

`psfCellSet`: spatial cells of PSF candidates (an `lsst.afw.math.SpatialCellSet`_)



Debugging
=========

.. csv-table:: 
   :header: Parameter, Type, Description
   :widths: 10, 5, 50


        `frame`, `int`, if specified: the frame of first debug image displayed (defaults to 1)	    
        `repair_iter`, `bool`,  if ``True`` display image after each repair in the measure PSF loop
	`background_iter`, `bool`,  if ``True`` display image after each background subtraction in the measure PSF loop
	`measure_iter`, `bool`,  if ``True`` display image and sources at the end of each iteration of the measure PSF loop.  See `lsst.meas.astrom.display.displayAstrometry <taskModules.html#dispastrom>`_  for the meaning of the various symbols.
	`psf`, `bool`,  if ``True`` display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true
	`repair`, `bool`,  if ``True`` display image and sources after final repair
	`measure`, `bool`,  if ``True`` display image and sources after final measurement

See `lsstDebug.info <taskModules.html#info>`_ for more on the debugging framework.



Examples
========

.. This example is not working in the current stack (see https://jira.lsstcorp.org/browse/DM-9142), and has been removed from it for now  --- 2/9/2017
   

Note: running this example currently requires that over and above the DM Stack installation, `afwdata`_ is installed and set up (via the EUPS `setup <taskModules.html#eups>`_ command).

.. _`afwdata`: https://github.com/lsst/afwdata
.. This is a general link to the EUPS tutorial, but setup is explained in there
   
This example script is `calibrateTask.py` (which calls :doc:`CharacterizeImageTask <apiUsage_charimg>`) before calling :doc:`CalibrateTask <calibimg>` in the `$PIPE_TASKS/examples` directory, and can be run from the command line as, e.g.:


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

The PSF is iteratively arrived at by repeatedly interpolating over
cosmic rays (using a subtask which defaults to `RepairTask <taskModules.html#repair>`_),
estimating and subtracting the background (using a subtask which
defaults to `SubtractBackgroundTask <taskModules.html#subbkgd>`_), detecting sources (using a
subtask which defaults to `SourceDetectionTask <taskModules.html#srcdet>`_ ), optionally
deblending them (using a task which defaults to `SourceDeblendTask <taskModules.html#srcdeblend>`_),
and then measuring them (using a subtask which defaults to
`SingleFrameMeasurementTask <taskModules.html#sfmtask>`_), and using those sources to estimate
the PSF (using a subtask which defaults to `MeasurePsfTask <taskModules.html#measpsf>`_). This is
repeated ``psfIterations`` times, gradually refining the PSF
model. After the ultimate PSF has been so derived, it is used in final
repair and measurement steps which produce the source catalog returned
to the caller.


*[Need more specific input from developers on what to insert for algorithmic details here.]*
