
#############
CalibrateTask
#############


Given a properly characterized exposure, detect sources, measure their
positions, and do a photometric measurement on them.

This task is implemented in the ``lsst.pipe.tasks`` module.

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

Configuration
=============

Flags and utility variables
---------------------------

- doWrite  (`bool`) - defaults to `True` - Save calibration results?
 
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

Subtasks
--------

- 	refObjLoader - target=LoadAstrometryNetObjectsTask -   reference object loader
 
- 	astrometry - target=AstrometryTask - Perform astrometric calibration to refine the WCS
  
- 	photoCal - target=PhotoCalTask - Perform photometric calibration
  
- 	detection - target=SourceDetectionTask - Detect sources
 
 
- 	deblend - target=SourceDeblendTask - Split blended sources into their components
 
- 	measurement - target=SingleFrameMeasurementTask - Measure sources
 
 
- 	applyApCorr - target=ApplyApCorrTask - Subtask to apply aperture corrections
 
- 	catalogCalculation - target=CatalogCalculationTask - Subtask to run catalogCalculation plugins on catalog



Entrypoint
==========

- ``lsst.pipe.tasks.calibrate.CalibrateTask.run`` 

Butler Inputs
=============

The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.

Butler Outputs
==============

Examples
========

The example code is ``calibrateTask.py`` in the ``$PIPE_TASKS/examples`` directory, and can be run as, e.g.::

     python examples/calibrateTask.py --display
     

Debugging
=========

- ``calibrate`` -  (an `int`, set to :math:`\le 0` to not display) frame in which to display the exposure, sources and matches. See ``lsst.meas.astrom.displayAstrometry`` for the meaning of the various symbols.


Algorithm details
====================

  In more detail: given an exposure with a good PSF model and aperture
correction map (e.g. as provided by ``CharacterizeImageTask``),
``CalibTask`` calls the entrypoint function,
``lsst.pipe.tasks.calibrate.run`` which will calibrate an exposure,
optionally unpersisting inputs and persisting outputs.  This is a
wrapper around the ``lsst.pipe.tasks.calibrate.calibrate`` method that
unpersists inputs (if ``doUnpersist`` `true`) and persists outputs (if
``config.doWrite`` `true`), and does the actual calibration of an
exposure (either a science image or a coadd).

In sequence, the following operations are then performed on the exposure:

    - ``lsst.pipe.tasks.detectAndMeasure`` is run to peform deep detection and measurement

    - At this point if the optional flags are set, ``lsst.pipe.tasks.calibrate.copyIcSourceFields`` will be run to match sources in icSourceCat and sourceCat and copy the specified fields.
	
    - ``lsst.meas.astrom.astrometry`` is run to fit an improved WCS

    -  ``lsst.pipe.tasks.photoCal`` is run to fit the exposure's photometric zero-point (and ``lsst.pipe.tasks.calibrate.setMetadata`` is run as part of this procedure to set task and exposure metadata and will log a warning and continue if needed data is missing).

If the outputs are to be persisted, ``lsst.pipe.tasks.calibrate.writeOutputs`` is called after all this in ``run`` to write output data to the output repository.
 


- [	``lsst.pipe.tasks.calibrate.getSchemaCatalogs`` -- -- Also an entrypoint..? ]
