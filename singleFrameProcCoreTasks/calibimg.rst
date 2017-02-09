#############
CalibrateTask
#############

Given a properly characterized exposure (which means one with a PSF
determined and shipped along with the image, commonly done previous to
running this Task by :doc:`CharacterizeImage <charimg>`), detect
sources, measure their positions, and do a photometric measurement on
them.


This task is implemented in the `lsst.pipe.tasks`_ module.

.. _`lsst.pipe.tasks`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_tasks.html

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.

    `API Usage <#>`_: *[To be filled in, like in charimg case]*

.. We will have a link to a separate page here called apiUsage_calibimg.rst
   
    
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
   `refObjLoader`, LoadAstrometryNetObjectsTask,   reference object loader
   `astrometry`, AstrometryTask, Perform astrometric calibration to refine the WCS

	
Parameters
----------
	
.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   `doWrite`,  `bool`,  `True`, Save calibration results?
   `doWriteMatches`,   `bool`,  `True`, Write reference matches? (ignored if `doWrite = false`)
   `doWriteHeavyFootprintsInSources`,  `bool` ,  `True`, Include HeavyFootprint data in source table? If false then heavy footprints are saved as normal footprints which saves some space
   `doAstrometry`,  `bool` ,  `True` , Run subtask to apply aperture correction?
   `requireAstrometry`,  `bool` ,  `True` , Raise an exception if astrometry fails? (ignored if `doAstrometry = false`)
   `doPhotoCal`,  `bool` ,  `True` , Perform photometric calibration?
   `requirePhotoCal`,`bool` ,  `True`, Raise an exception if photoCal fails? (ignored if `doPhotoCal = false`)
   `doApCorr`, `bool` ,  `True`, Run subtask to apply aperture correction?
   `matchRadiusPix`, `float` ,  3.0 , Match radius for matching icSourceCat objects to sourceCat objects (pixels)
   `doDeblend`, `bool` ,  `True` , Run deblender input exposure?
   `checkUnitsParseStrict`, `str` , `raise`, Strictness of Astropy unit compatibility check; can be: 'raise' ; 'warn' ; 'silent'




   
*Leaving this one out for now, not sure what to do with it, because the default is so long, it messes up the length of all the other entries in the table if included:*

   `icSourceFieldsToCopy`, `str` ,  ("calib_psfCandidate" ;    "calib_psfUsed"; "calib_psfReserved"),  Fields to copy from the    icSource catalog to the output catalog for matching sources. Any missing fields will trigger a RuntimeError exception.  Ignored if    icSourceCat is not provided.


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
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
`photoRefObjLoader`
  An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
`icSourceSchema`
  Schema for icSource catalog, or None. Schema values specified in config.icSourceFieldsToCopy will be taken from this schema. If set to None, no values will be propagated from the icSourceCatalog
`kwargs`
  Other keyword arguments for `lsst.pipe.base.CmdLineTask`_		

  
.. _`lsst.pipe.base.CmdLineTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html

Run method
----------
 
.. code-block:: python

  run(dataRef,
      exposure = None,
      background = None,
      icSourceCat = None,
      doUnpersist = True)		

The required input to the `run`_ method (which is a thin wrapper
around the `calibrate`_ method) is an already-characterized exposure
(produced by e.g. :doc:`CharacterizeImage <charimg>`), and there are
two optional inputs as well (which though are normally included at
this point): an initial model of the background which has already
subtracted from the exposure, and a source catalog, both provided by
e.g. :doc:`CharacterizeImage <charimg>`.
      
.. _`run`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1calibrate_1_1_calibrate_task.html#a067cbbb27a4f212aba05b419fcd17d28`

If you want this task to `unpersist <#>`_ inputs or `persist <#>`_ outputs, then call the `run`_ method, however, if you already have the inputs `unpersisted <#>`_ and do not want to `persist <#>`_ the output then it is more direct to call the `calibrate`_ method straight off.

.. As in charimg, we will link to pages that explain the persistence terms more technically
   
.. _`calibrate`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1calibrate_1_1_calibrate_task.html#a12bb075ab0bdf60d95ae30900688d9a4


Parameters
^^^^^^^^^^

`dataRef`
  `Butler <#>`_ data reference corresponding to a science image
`exposure`
  Characterized exposure (an `lsst.afw.image.ExposureF <#>`_ or similar), or `None` to unpersist existing `icExp <#>`_ and `icBackground <#>`_. See the `calibrate`_ method for details of what is read and written.
`background`
  Initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList <#>`_). May be `None` if no background has been subtracted, though that is unusual for calibration. A refined background model is output. Ignored if exposure is `None`.
`icSourceCat`
  Catalog from which to copy the fields specified by `icSourceKeys <#>`_, or `None`;
`doUnpersist`
  Unpersist data:
     - if `True`, exposure, `background` and `icSourceCat` are read from `dataRef` and those three arguments must all be `None`;
     - if `False` the exposure must be provided; `background` and `icSourceCat` are optional. `True` is intended for running as a command-line task, `False` for running as a subtask

.. Butler: we'll link to this in a glossary, minimally       
.. icexp and icbkgd: We want to eventually link the 2 types of exposures to a page with a descrip of the available types of them  
.. Should we use same link for lsst.afw.math.BackgroundList as in charimg?
.. Need a linked page to explain this icSourceKeys file 
.. icSourceCat etc.: Really, we want to link to pages where all these exposures and catalogs are explained more

Returns
^^^^^^^

Returns pipe_base Struct containing these fields:
 - exposure - calibrated science exposure with refined WCS and Calib
 - background - model of background subtracted from exposure (an `lsst.afw.math.BackgroundList <#>`_)
 - sourceCat - catalog of measured sources
 - astromMatches - list of source/refObj matches from the astrometry solver


Debugging
=========

- `calibrate` -  (an `int`, set to :math:`\le 0` to not display) frame in which to display the exposure, sources and matches. See `lsst.meas.astrom.display.displayAstrometry`_  for the meaning of the various symbols, and see `lsstDebug.info`_ for more on the debugging framework.

.. _`lsstDebug.info`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_debug_1_1_info.html
  
.. _`lsst.meas.astrom.display.displayAstrometry`:  https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1meas_1_1astrom_1_1display.html#aba98ee54d502f211b69ff35db4d36f94


Examples
========

This example script is `calibrateTask.py` (which calls :doc:`CharacterizeImageTask <charimg>` before calling this function (`CalibrateTask`) ) in the `$PIPE_TASKS/examples` directory, and the example is described already under `Examples` on :doc:`CharacterizeImageTask <charimg>`.


   
Algorithm details
==================

`CalibrateTask` initially runs functions analogously to :doc:`CharacterizeImageTask <charimg>`  (which is usually run before `CalibrateTask`)  to this time perform deep detection and measurement (using subtasks which default to `SourceDetectionTask`_  and `SingleFrameMeasurementTask`_).

.. _`SourceDetectionTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1algorithms_1_1detection_1_1_source_detection_task.html

.. _`SingleFrameMeasurementTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1base_1_1sfm_1_1_single_frame_measurement_task.html

If a flags are set for it to do so, it also optionally runs a deblender subtask (which defaults to `SourceDeblendTask`_), and an aperture correction subtask (which defaults to `ApplyApCorrTask`_)

.. _`SourceDeblendTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1deblender_1_1deblend_1_1_source_deblend_task.html

.. _`ApplyApCorrTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1base_1_1apply_ap_corr_1_1_apply_ap_corr_task.html

Some of its other primary functions are to do astrometric calibration on the exposure (using a subtask which defaults to `AstrometryTask`_), as well as photometric calibration on it (using a subtask which defaults to `PhotoCalTask`_).

.. _`AstrometryTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1astrom_1_1astrometry_1_1_astrometry_task.html

.. _`PhotoCalTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1photo_cal_1_1_photo_cal_task.html

*[Need specific input from developers on what to insert for algorithmic details here.]*
