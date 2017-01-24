

##############
ProcessCcdTask
##############

ProcessCcdTask (available as the ``processCcd.py`` ``command line
task``) executes the steps of how an image is processed from raw
uncorrected CCD-level data finally to science-grade images and
catalogs.

It takes as input to its ``run`` method a single butler data reference
for ``raw`` data and then outputs cleaned images (as a
``lsst.afw.image.ExposureF`` field of a ``lsst.pipe.base.Struct``) and
catalogs (``background`` and ``sourceCat`` fields of a
``lsst.pipe.base.Struct``) to be used by later steps.

In more detail, ProcessCcdTask executes the following steps:


1.  ``Instrument Signature Removal`` -- Implemented by the :doc:`IsrTask <isrtask>` sub-task (isr configuration), this step removes CCD signatures (such as bias, dark current, flat-fielding, and cross-talk) and masks bad pixels.

2. ``Image Characterization`` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` sub-task (charImage configuration), this step repairs cosmic ray defects, estimates and subtracts a background, does object detection, and estimates a PSF.
  
3. ``Image Calibration``  -- Implemented by the :doc:`CalibrateTask <calibimg>` sub-task (calibrate configuration), this step measures faint sources, fits an astrometric WCS and extracts a photometric zero-point for the image.


ProcessCcdTask is implemented in the ``lsst.pipe.tasks`` module.



Configuration
=============

Retargetable Subtasks
---------------------

-	``isr`` -  default=IsrTask - Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:

	- assemble raw amplifier images into an exposure with image, variance and mask planes
	- perform bias subtraction, flat fielding, etc.
	- mask known bad pixels
	- provide a preliminary WCS
		
-	``charImage`` - default=CharacterizeImageTask - Task to characterize a science exposure, the steps of image characterization are to:

	- detect sources, usually at high S/N
	- estimate the background, which is subtracted from the image and returned as field "background"
	- estimate a PSF model, which is added to the exposure
	- interpolate over defects and cosmic rays, updating the image, variance and mask planes
    
 
-	``calibrate`` - default=CalibrateTask - Task to perform astrometric and photometric calibration, the steps are to:

	- refine the WCS in the exposure
	- refine the Calib photometric calibration object in the exposure
	- detect sources, usually at low S/N

Parameters
----------

-	``doCalibrate`` - (`bool`) - defaults to `True` - Perform calibration?
 



Entrypoint
==========

- ``lsst.pipe.tasks.processCcd.ProcessCcdTask.run`` 
  

Butler Inputs
=============

The main method, ``run``, takes a single butler data reference for the ``raw`` input data.

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

Command Line Arguments 
======================

ProcessCcdTask has all command line arguments available to a general
``command line task``, which can be found on the CLTargs page.
