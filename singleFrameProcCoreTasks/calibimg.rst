#############
CalibrateTask
#############

Given a background subtracted image, a PSF for it, and an initial
astrometric solution (all commonly provided to this task by
:doc:`CharacterizeImage <charimg>`), this task will detect sources,
measure their positions, and do a photometric calibration on them.


This task is implemented in the `lsst.pipe.tasks <taskModules.html#pipetasks>`_ module.


.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

    `API Usage`: See :doc:`CharacterizeImageTask API <apiUsage_calib>`

   
    
Configuration
=============

Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

   `refObjLoader`, LoadAstrometryNetObjectsTask, Reference object loader
   `astrometry`,   AstrometryTask, Perform astrometric calibration to refine the WCS
   `photoCal`, PhotoCalTask, Perform photometric calibration  
   `detection`,  SourceDetectionTask, Detect sources
   `deblend`, SourceDeblendTask, Split blended sources into their components
   `measurement`, SingleFrameMeasurementTask, Measure sources
   `photoCal`, PhotoCalTask, Perform photometric calibration
   `detection`, SourceDetectionTask, Detect sources
   `deblend`, SourceDeblendTask, Split blended sources into their components
   `measurement`, SingleFrameMeasurementTask, Measure sources
   `applyApCorr`, ApplyApCorrTask, Subtask to apply aperture corrections
   `catalogCalculation`, CatalogCalculationTask, Subtask to run catalogCalculation plugins on catalog
   `refObjLoader`, LoadAstrometryNetObjectsTask,   Reference object loader
   `astrometry`, AstrometryTask, Perform astrometric calibration to refine the WCS

	
Parameters
----------
	
.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doWrite`,  `bool`,  ``True``, Save calibration results?
   `doWriteMatches`,   `bool`,  ``True``, Write reference matches? (ignored if ``doWrite = False``)
   `doWriteHeavyFootprintsInSources`,  `bool` ,  ``True``, Include HeavyFootprint data in source table? If ``False`` then heavy footprints are saved as normal footprints which saves some space
   `doAstrometry`,  `bool` ,  ``True`` , Run subtask to apply aperture correction?
   `requireAstrometry`,  `bool` ,  ``True`` , Raise an exception if astrometry fails? (ignored if ``doAstrometry = False``)
   `doPhotoCal`,  `bool` ,  ``True`` , Perform photometric calibration?
   `requirePhotoCal`, `bool` ,  ``True``, Raise an exception if photoCal fails? (ignored if ``doPhotoCal = False``)
   `doApCorr`, `bool` ,  ``True``, Run subtask to apply aperture correction?
   `matchRadiusPix`, `float` ,  ``3.0`` , Match radius for matching icSourceCat objects to sourceCat objects (pixels)
   `doDeblend`, `bool` ,  ``True`` , Run deblender input exposure?
   `checkUnitsParseStrict`, `str` , ``"raise"``, Strictness of `Astropy`_ unit compatibility check; can be: ``"raise"`` ``"warn"`` or ``"silent"`` 

.. .. _`Astropy`: http://www.astropy.org/

.. Above link is curious: it won't properly work without the second two ".." (or any other comment-like content), unlike other usual links.  Hm.  (2/12/2017)

   
*Leaving this one out for now, not sure what to do with it, because the default is so long, it messes up the length of all the other entries in the table if included:*

   `icSourceFieldsToCopy`, `str` ,  ("calib_psfCandidate" ;    "calib_psfUsed"; "calib_psfReserved"),  Fields to copy from the    icSource catalog to the output catalog for matching sources. Any missing fields will trigger a RuntimeError exception.  Ignored if icSourceCat is not provided.


Python usage
============
 
Class initialization
--------------------

.. code-block:: python

  lsst.pipe.tasks.calibrate.CalibrateTask(
 	butler = None,
 	astromRefObjLoader = None,
 	photoRefObjLoader = None,
 	icSourceSchema = None,
 	**kwargs  )		


Parameters
^^^^^^^^^^


`butler`
  The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.
`astromRefObjLoader`
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be ``None`` if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
`photoRefObjLoader`
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be ``None`` if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
`icSourceSchema`
  Schema for icSource catalog, or ``None``. Schema values specified in config.icSourceFieldsToCopy will be taken from this schema. If set to ``None``, no values will be propagated from the icSourceCatalog
`kwargs`
  Other keyword arguments for `lsst.pipe.base.CmdLineTask <CLTs.html#CLTbaseclass>`_		

 
Run method
----------
 
.. code-block:: python

  run(dataRef,
      exposure = None,
      background = None,
      icSourceCat = None,
      doUnpersist = True)		

The required input to the `run` method (which is a thin wrapper around
the `calibrate <apiUsage_calib.html#calibrate>`_ method) is an
already-characterized exposure (produced by
e.g. :doc:`CharacterizeImage <charimg>`), and there are two optional
inputs as well (which though are normally included at this point): an
initial model of the background which has already subtracted from the
exposure, and a source catalog, both provided by
e.g. :doc:`CharacterizeImage <charimg>`.
      


If you want this task to `unpersist` inputs or `persist` outputs, then call the `run` method, however, if you already have the inputs `unpersisted` and do not want to `persist` the output then it is more direct to call the `calibrate`_ method straight off.

.. As in charimg, we will link to pages that explain the persistence terms more technically


Parameters
^^^^^^^^^^

`dataRef`
  `Butler <LSSTglossary.html#butlerlink>`_ data reference corresponding to a science image
`exposure`
  Characterized exposure (an `lsst.afw.image.ExposureF` or similar), or ``None`` to unpersist existing `icExp` and `icBackground`. See the `calibrate`_ method for details of what is read and written.
`background`
  Initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList <LSSTglossary.html#bkgdlist>`_). May be ``None`` if no background has been subtracted, though that is unusual for calibration. A refined background model is output. Ignored if exposure is ``None``.
`icSourceCat`
  Catalog from which to copy the fields specified by `icSourceKeys`, or ``None``;
`doUnpersist`
  Unpersist data:
     - if ``True``, exposure, `background` and `icSourceCat` are read from `dataRef` and those three arguments must all be ``None``;
     - if ``False`` the exposure must be provided; `background` and `icSourceCat` are optional. ``True`` is intended for running as a command-line task, ``False`` for running as a subtask


.. icexp and icbkgd: We want to eventually link the 2 types of exposures to a page with a descrip of the available types of them  
.. Need a linked page to explain this icSourceKeys file 
.. icSourceCat etc.: Really, we want to link to pages where all these exposures and catalogs are explained more

Returns
^^^^^^^

Returns pipe_base Struct containing these fields:
 - exposure - calibrated science exposure with refined WCS and Calib
 - background - model of background subtracted from exposure (an `lsst.afw.math.BackgroundList`_)
 - sourceCat - catalog of measured sources
 - astromMatches - list of source/refObj matches from the astrometry solver


Debugging
=========

- `calibrate` -  (an `int`, set to :math:`\le 0` to not display) frame in which to display the exposure, sources and matches. See `lsst.meas.astrom.display.displayAstrometry <taskModules.html#dispastrom>`_  for the meaning of the various symbols, and see `lsstDebug.info <taskModules.html#info>`_ for more on the debugging framework.


Examples
========

This example script is `calibrateTask.py` (which calls :doc:`CharacterizeImageTask <charimg>` before calling this function (`CalibrateTask`) ) in the `$PIPE_TASKS/examples` directory, and the example is described already under `Examples` on :doc:`CharacterizeImageTask <charimg>`.

.. This example is not working in the current stack (see https://jira.lsstcorp.org/browse/DM-9142)  and has been removed from it --- 2/9/2017

   
   
Algorithm details
==================

`CalibrateTask` initially runs functions analogously to
:doc:`CharacterizeImageTask <charimg>` (which is usually run before
`CalibrateTask`) to this time perform deep detection and
measurement (using subtasks which default to `SourceDetectionTask <taskModules.html#srcdet>`_
and `SingleFrameMeasurementTask <taskModules.html#sfmtask>`_) down to a configurable
signal-to-noise threshold (the point sources are the ones optimally
detected at this stage).  If a flags are set for it to do so, it also
optionally runs a deblender subtask (which defaults to
`SourceDeblendTask <taskModules.html#srcdeblend>`_), and an aperture correction subtask (which
defaults to `ApplyApCorrTask <taskModules.html#apcorr>`_) Some of its other primary functions
are to do astrometric calibration on the exposure (using a subtask
which defaults to `AstrometryTask <taskModules.html#astrom>`_), as well as photometric
calibration on it (using a subtask which defaults to `PhotoCalTask <taskModules.html#photocal>`_).






*[Need specific input from developers on what to insert for algorithmic details here.]*
