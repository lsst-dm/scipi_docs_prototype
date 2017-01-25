
#############
CalibrateTask
#############

Given a properly characterized exposure (which means one with a PSF
determined and shipped along with the image, commonly done previous to
running this Task by :doc:`CharacterizeImage <charimg>`), detect
sources, measure their positions, and do a photometric measurement on
them.

This task is implemented in the ``lsst.pipe.tasks`` module.

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

Configuration
=============

Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

   ``refObjLoader``, LoadAstrometryNetObjectsTask, Reference object loader
   ``astrometry``,   AstrometryTask, Perform astrometric calibration to refine the WCS
   ``photoCal``, PhotoCalTask, Perform photometric calibration  
   ``detection``,  SourceDetectionTask, Detect sources
   ``deblend``, SourceDeblendTask, Split blended sources into their components
   ``measurement``, SingleFrameMeasurementTask, Measure sources
   ``photoCal``, PhotoCalTask, Perform photometric calibration
   ``detection``, SourceDetectionTask, Detect sources
   ``deblend``, SourceDeblendTask, Split blended sources into their components
   ``measurement``, SingleFrameMeasurementTask, Measure sources
   ``applyApCorr``, ApplyApCorrTask, Subtask to apply aperture corrections
   ``catalogCalculation``, CatalogCalculationTask, Subtask to run catalogCalculation plugins on catalog
   ``refObjLoader``, LoadAstrometryNetObjectsTask,   reference object loader
   ``astrometry``, AstrometryTask, Perform astrometric calibration to refine the WCS

	
Parameters
----------
	
.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   ``doWrite``,  `bool`,  `True`, Save calibration results?
   ``doWriteMatches``,   `bool`,  `True`, Write reference matches? (ignored if ``doWrite`` = `false`)
   ``doWriteHeavyFootprintsInSources``,  `bool` ,  `True`, Include HeavyFootprint data in source table? If false then heavy footprints are saved as normal footprints which saves some space
   ``doAstrometry``,  `bool` ,  `True` , Run subtask to apply aperture correction?
   ``requireAstrometry``,  `bool` ,  `True` , Raise an exception if astrometry fails? (ignored if ``doAstrometry`` = `false`)
   ``doPhotoCal``,  `bool` ,  `True` , Perform photometric calibration?
   ``requirePhotoCal``,`bool` ,  `True`, Raise an exception if photoCal fails? (ignored if ``doPhotoCal`` = `false`)
   ``doApCorr``, `bool` ,  `True`, Run subtask to apply aperture correction?
   ``matchRadiusPix``, `float` ,  3.0 , Match radius for matching icSourceCat objects to sourceCat objects (pixels)
   ``doDeblend``, `bool` ,  `True` , Run deblender input exposure?
   ``checkUnitsParseStrict``, `str` , `raise`, Strictness of Astropy unit compatibility check; can be: 'raise' ; 'warn' ; 'silent'




   
Leaving this one out for now, not sure what to do with it, because the default is so long, it messes up the length of all the other entries in the table if included:

   ``icSourceFieldsToCopy``, `str` ,  ("calib_psfCandidate" ;    "calib_psfUsed"; "calib_psfReserved"),  Fields to copy from the    icSource catalog to the output catalog for matching sources. Any missing fields will trigger a RuntimeError exception.  Ignored if    icSourceCat is not provided.





	


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
     
Running this example currently requires that over and above the DM Stack installation, ``afwdata`` is installed and set up (via the EUPS ``setup`` command).

Debugging
=========

- ``calibrate`` -  (an `int`, set to :math:`\le 0` to not display) frame in which to display the exposure, sources and matches. See ``lsst.meas.astrom.displayAstrometry`` for the meaning of the various symbols.

 
Algorithm details
==================

..
  - [	``lsst.pipe.tasks.calibrate.getSchemaCatalogs`` -- -- Also an entrypoint..? ]
