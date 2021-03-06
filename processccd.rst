

##############
ProcessCcdTask
##############

ProcessCcd (which is a ``Cmd Line Task``, and thus can be run directly
by typing processCcd.py at a shell prompt) executes the steps of how
an image is processed from raw data to a science-grade images and catalogs that can
be used in analyses.

In more detail: ProcessCcd as a whole executes many of the functions
that are in multiple packages in other astronomy analysis frameworks.

- The initial step is to do ``Instrument Signature Removal`` through running :doc:`isrTask <isrtask>` to correct the images for all the issues involved in taking a raw image CCD through to a processed one (e.g. doing the bias and dark current corrections, flat-fielding, etc.).

- The second step is to do ``Image Characterization`` by running :doc:`characterizeImageTask <charimg>`), which includes for our purposes: object detection, repairing of cosmic ray defects, measuring and subtracting of sky background, and then finally measuring bright sources and using this to estimate background and PSF of an exposure.
  
- The last step is doing ``Image Calibration`` by running :doc:`calibrateTask <calibimg>`, which measures faint sources, does the astrometry by fitting an improved WCS to the image, and figures out the photometric zero-point for the image.

ProcessCcdTask is implemented in the ``lsst.pipe.tasks`` module.


See also
=========

(Anything to put here?)

Configuration
=============

Flags  and utility variables
----------------------------

-	``doCalibrate`` - (`bool`) - defaults to `True` - Perform calibration?
 

Subtasks
--------

-	``isr`` -  target=IsrTask - Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:

	- assemble raw amplifier images into an exposure with image, variance and mask planes
	- perform bias subtraction, flat fielding, etc.
	- mask known bad pixels
	- provide a preliminary WCS
		
-	``charImage`` - target=CharacterizeImageTask - Task to characterize a science exposure, the steps of image characterization are to:

	- detect sources, usually at high S/N
	- estimate the background, which is subtracted from the image and returned as field "background"
	- estimate a PSF model, which is added to the exposure
	- interpolate over defects and cosmic rays, updating the image, variance and mask planes
    
 
-	``calibrate`` - target=CalibrateTask - Task to perform astrometric and photometric calibration, the steps are to:

	- refine the WCS in the exposure
	- refine the Calib photometric calibration object in the exposure
	- detect sources, usually at low S/N
 

Entrypoint
==========

- ``lsst.pipe.tasks.processCcd.ProcessCcdTask.run`` 
  

Butler Inputs
=============

The main method, ``run``, takes a single butler data reference for the raw input data.

Examples
========

The following commands will process all raw data in obs_test's data repository. Note: be sure to specify an ``--output`` that does not already exist::

  setup obs_test
  setup pipe_tasks
  processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id

The data is read from the small repository in the ``obs_test`` package and written to: ``./processCcdOut`` (or whatever output you specified). Specifying ``--id`` with no values processes all data. Add the option ``--help`` to see more options.


Debugging
=========

ProcessCcdTask has no debug output, but its several subtasks do.

ArgParse
========

The makeArgumentParse method creates and returns an argument parser.

This override is used to delay making the data ref list until the dataset type is known; this is done in parseAndRun.

ButlerInitializedTaskRunner
===========================

