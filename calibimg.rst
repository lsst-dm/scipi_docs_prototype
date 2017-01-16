
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

Paramters
---------

-``doWrite``  (`bool`) - defaults to `True` - Save calibration results?
 
-``doWriteHeavyFootprintsInSources`` (`bool`) - defaults to `True` -
    Include HeavyFootprint data in source table? If false then heavy
    footprints are saved as normal footprints, which saves some space
 
-``doWriteMatches``  (`bool`) - defaults to `True` - Write reference matches? (ignored if doWrite `false`)
 
-``doAstrometry`` (`bool`) - defaults to `True` - Run subtask to apply aperture correction?
 
-``requireAstrometry`` (`bool`) - defaults to `True` - Raise an exception if astrometry fails? (ignored if doAstrometry `false`)
 
-``doPhotoCal`` (`bool`) - defaults to `True` - Perform photometric calibration?

	
-``requirePhotoCal``  (`bool`) - defaults to `True`- Raise an exception if photoCal fails? (ignored if doPhotoCal false)

-``icSourceFieldsToCopy`` (`str`) - defaults to ("calib_psfCandidate",
    "calib_psfUsed", "calib_psfReserved"), - Fields to copy from the
    icSource catalog to the output catalog for matching sources Any
    missing fields will trigger a RuntimeError exception.  Ignored if
    icSourceCat is not provided.

-``checkUnitsParseStrict`` (`str`) - Strictness of Astropy unit compatibility check, can be 'raise', 'warn' or 'silent'


-``doApCorr`` (`bool`) - defaults to `True`- Run subtask to apply aperture correction?


-``matchRadiusPix`` (`float`) - defaults to 3 - Match radius for matching icSourceCat objects to sourceCat objects (pixels)

-``doDeblend`` (`bool`) - defaults to `True` - Run deblender input exposure?
	


Subtasks
--------

- 	``refObjLoader`` - default target=LoadAstrometryNetObjectsTask -   reference object loader
 
- 	``astrometry`` - default target=AstrometryTask - Perform astrometric calibration to refine the WCS
  
- 	``photoCal`` - default target=PhotoCalTask - Perform photometric calibration
  
- 	``detection`` - default target=SourceDetectionTask - Detect sources
 
 
- 	``deblend`` - default target=SourceDeblendTask - Split blended sources into their components
 
- 	``measurement`` - default target=SingleFrameMeasurementTask - Measure sources
 
 
- 	``applyApCorr`` - default target=ApplyApCorrTask - Subtask to apply aperture corrections
 
- 	``catalogCalculation`` - default target=CatalogCalculationTask - Subtask to run catalogCalculation plugins on catalog



Entrypoint
==========

- ``lsst.pipe.tasks.calibrate.CalibrateTask.run`` 

Butler Inputs
=============

The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly (type: ``icSrc_schema``).

Butler Outputs
==============

Source catalog of type ``src``.

Examples
========

The example code is ``calibrateTask.py`` in the ``$PIPE_TASKS/examples`` directory, and can be run as, e.g.::

     python examples/calibrateTask.py --display
     

Debugging
=========

- ``calibrate`` -  (an `int`, set to :math:`\le 0` to not display) frame in which to display the exposure, sources and matches. See ``lsst.meas.astrom.displayAstrometry`` for the meaning of the various symbols.

 
Algorithm details
==================

..
  - [	``lsst.pipe.tasks.calibrate.getSchemaCatalogs`` -- -- Also an entrypoint..? ]
