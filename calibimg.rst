
#############
CalibrateTask
#############


Given a properly characterized exposure, detect sources, measure their
positions, and do a photometric measurement on them.

More precisely: given an exposure with a good PSF model and aperture
correction map (e.g. as provided by ``CharacterizeImageTask``),
``CalibTask`` performs the following operations on it:

    - Runs ``lsst.pipe.tasks.detectAndMeasure`` to peform deep detection and measurement
      
    - Runs ``lsst.meas.astrom.astrometry`` to fit an improved WCS

    - Runs ``lsst.pipe.tasks.photoCal`` to fit the exposure's photometric zero-point


Configuration
=============

- 	doWrite  (`bool`) - defaults to `True` - Save calibration results?
 
-   doWriteHeavyFootprintsInSources (`bool`) - defaults to `True` -
    Include HeavyFootprint data in source table? If false then heavy
    footprints are saved as normal footprints, which saves some space
 
- 	doWriteMatches  (`bool`) - defaults to `True` - Write reference matches? (ignored if doWrite `false`)
 
- 	doAstrometry (`bool`) - defaults to `True` - Run subtask to apply aperture correction?
 
- 	requireAstrometry (`bool`) - defaults to `True` - Raise an exception if astrometry fails? (ignored if doAstrometry `false`)
 
- 	doPhotoCal (`bool`) - defaults to `True` - Perform phometric calibration?

	
- 	requirePhotoCal  (`bool`) - defaults to `True`- Raise an exception if photoCal fails? (ignored if doPhotoCal false)

-   icSourceFieldsToCopy (`str`) - defaults to ("calib_psfCandidate",
    "calib_psfUsed", "calib_psfReserved"), - Fields to copy from the
    icSource catalog to the output catalog for matching sources Any
    missing fields will trigger a RuntimeError exception.  Ignored if
    icSourceCat is not provided.

- 	checkUnitsParseStrict (`str`) - Strictness of Astropy unit compatibility check, can be 'raise', 'warn' or 'silent'


- 	doApCorr (`bool`) - defaults to `True`- Run subtask to apply aperture correction?


-    matchRadiusPix (`float`) - defaults to 3 - Match radius for matching icSourceCat objects to sourceCat objects (pixels)

- 	doDeblend (`bool`) - defaults to `True` - Run deblender input exposure?
	
-----------

- 	refObjLoader - target=LoadAstrometryNetObjectsTask -   reference object loader
 
- 	astrometry - target=AstrometryTask - Perform astrometric calibration to refine the WCS
  
- 	photoCal - target=PhotoCalTask - Perform photometric calibration
  
- 	detection - target=SourceDetectionTask - Detect sources
 
 
- 	deblend - target=SourceDeblendTask - Split blended sources into their components
 
- 	measurement - target=SingleFrameMeasurementTask - Measure sources
 
 
- 	applyApCorr - target=ApplyApCorrTask - Subtask to apply aperture corrections
 
- 	catalogCalculation - target=CatalogCalculationTask - Subtask to run catalogCalculation plugins on catalog

Methods
=======

-  ``lsst.pipe.tasks.calibrate.run`` - 	Calibrate an exposure, optionally unpersisting inputs and persisting outputs.  This is a wrapper around the ``calibrate`` method that unpersists inputs (if ``doUnpersist`` `true`) and persists outputs (if ``config.doWrite`` `true`).


 
- 	``lsst.pipe.tasks.calibrate.calibrate`` - 	Calibrate an exposure (science image or coadd) 
 
- 	``lsst.pipe.tasks.calibrate.writeOutputs`` - Write output data to the output repository
 
- 	``lsst.pipe.tasks.calibrate.getSchemaCatalogs``
 
- 	``lsst.pipe.tasks.calibrate.setMetadata`` -	Set task and exposure metadata.  Logs a warning and continues if needed data is missing.

 
- 	``lsst.pipe.tasks.calibrate.copyIcSourceFields`` - Match sources in icSourceCat and sourceCat and copy the specified fields.



Entrypoint
==========

- ``lsst.pipe.tasks.calibrate.run`` 

Butler Inputs
=============

The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.

Examples
========

The example code is ``calibrateTask.py`` in the ``$PIPE_TASKS/examples`` directory, and can be run as, e.g.::

     python examples/calibrateTask.py --display
     

Debugging
=========

- ``calibrate`` - frame (an int; :math:`\le 0` to not display) in which to display the exposure, sources and matches. See ``lsst.meas.astrom.displayAstrometry`` for the meaning of the various symbols.

