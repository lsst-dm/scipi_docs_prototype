
##############
ProcessCcdTask
##############

ProcessCcdTask (available as the `processCcd.py`_ `command line task <#>`_ ) executes the steps of how an image is processed from raw
uncorrected CCD-level data finally to science-grade images and
catalogs.

.. _processCcd.py: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/process_ccd_8py_source.html

In more detail, ProcessCcdTask executes the following steps:


1.  `Instrument Signature Removal` -- Implemented by the :doc:`IsrTask <isrtask>` subtask, this step removes CCD signatures (such as bias, dark current, flat-fielding, and cross-talk) and masks bad pixels.

2. `Image Characterization` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` subtask, this step repairs cosmic ray defects, estimates and subtracts a background, does object detection, and estimates a PSF.
  
3. `Image Calibration`  -- Implemented by the :doc:`CalibrateTask <calibimg>` subtask, this step measures faint sources, fits an astrometric WCS and extracts a photometric zero-point for the image.


ProcessCcdTask is implemented in the `lsst.pipe.tasks`_ module.

.. _lsst.pipe.tasks: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_tasks.html
    

Configuration
=============

Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	``isr``,   :doc:`IsrTask <isrtask>`, Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:	- assemble raw amplifier images into an exposure with image; variance and mask planes	- perform bias subtraction; flat fielding; etc.	- mask known bad pixels	- provide a preliminary WCS		
	``charImage``, :doc:`CharacterizeImageTask <charimg>`, Task to characterize a science exposure; the steps of image characterization are to:	- detect sources; usually at high S/N	- estimate the background; which is subtracted from the image and returned as field "background"	- estimate a PSF model; which is added to the exposure	- interpolate over defects and cosmic rays; updating the image; variance and mask planes
	``calibrate``,  :doc:`CalibrateTask <calibimg>`, Task to perform astrometric and photometric calibration; the steps are to:	- refine the WCS in the exposure	- refine the Calib photometric calibration object in the exposure	- detect sources; usually at low S/N

	
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

     ``doCalibrate`` ,`bool`, `True`, Perform calibration?

Python usage
============
 
Class initialization
--------------------
 
.. code-block:: python
 
   lsst.pipe.tasks.processCcd.ProcessCcdTask(
       butler = None,
    	 psfRefObjLoader = None,
    	 astromRefObjLoader = None,
    	 photoRefObjLoader = None,
    	 **kwargs)
 
Parameters
^^^^^^^^^^
 
``butler``
   The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.
 
``psfRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for image characterization. An example of when this would be used is when a CatalogStarSelector is used. May be None if the desired loader can be constructed from the butler argument or all steps requiring a catalog are disabled.
 
``astromRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
``photoRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
``**kwargs``
   Other keyword arguments for `lsst.pipe.base.CmdLineTask`_.

.. _`lsst.pipe.base.CmdLineTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html


Run method
----------
 
.. code-block:: python
 
   run(sensorRef)

   
Parameters
^^^^^^^^^^
 
``sensorRef``
   butler data reference for raw data.
 
Returns
^^^^^^^
 
``struct`` (``lsst.pipe.base.Struct``)
   ``lsst.pipe.base.Struct`` containing these fields:
 
   - ``charRes``: object returned by image characterization task; an ``lsst.pipe.base.Struct`` that will include "background" and "sourceCat" fields.
   - ``calibRes``: object returned by calibration task: an ``lsst.pipe.base.Struct`` that will include "background" and "sourceCat" fields
   - ``exposure``: final exposure (an ``lsst.afw.image.ExposureF``)
   - ``background``: final background model (an lsst.afw.math.BackgroundList)
 
Running from the Command Line
=============================

ProcessCcdTask has all command line arguments available to a general
``command line task``, which can be found on the CLTargs page.

*[Will include info on the `--id` argument here.]*




Butler Inputs
=============

The main method, `run`_, takes a single butler data reference for the ``raw`` input data.

.. _run: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1process_ccd_1_1_process_ccd_task.html#a82488db6374fb538db2ec4418419bdd4

Butler Outputs
==============

Examples
========

The ``obs_test`` package  models a simple camera with one CCD and includes a data repository containing a few raw images (simulating three visits, two with with the `g`-band filter, and one with the `r`-band one), and some associated calibration data. Its camera consists of a single CCD whose geometry matches a subregion of a single LSST CCD.

The following commands will process all raw data in obs_test's data repository. Note: be sure to specify an ``--output`` that does not already exist::

  setup obs_test
  setup pipe_tasks
  processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id

The data is read from the small repository in the ``obs_test`` package and output images and catalogs are written to subdirectories in: ``./processCcdOut`` (or whatever output name you specified).

Specifying ``--id`` with no values processes all data.

Add the option ``--help`` to see more options.


Debugging
=========

ProcessCcdTask has no debug output, but its several subtasks do.


Algorithm details
=================

ProcessCcdTask is essentially a wrapper around the three subtasks, see those for actual contentful algorithmic details.
