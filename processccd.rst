

##############
ProcessCcdTask
##############

ProcessCcd (which is a ``CL task``) executes the steps of how an image
is processed from raw data to a science-grade image that can be used
in analyses.

In more detail: ProcessCcd as a whole executes many of the functions
that are in multiple packages in other astronomy analysis frameworks.

The initial step is to run isrTask to correct the images for all the
issues involved in taking a raw image CCD through to a processed one
(e.g. doing the bias and dark current corrections, flat-fielding,
etc.) by first doing everything that astronomers have used a medley of
customized codes typically for each telescope before (like IRAF, UNIX
shellscripts, IDL scripts etc.).  These tasks are usually grouped
together under the general term 'Instrumental Signature Removal.'

The second step groups together several functions as 'Image
Characterization', which includes for our purposes: object detection
(very commonly done by Source Extractor), repairing of cosmic ray
defects, measuring and subtracting of sky background, and then finally
measuring bright sources and using this to estimate background and PSF
of an exposure (which is often done currently by astronomers using the
PSFex code).

The last primary grouping of tasks is what we will call 'Image
Calibration', which measures faint sources, does the astrometry by
fitting an improved WCS to the image (often done currently by
astronomers using by using the SCAMP and SWARP codes, 'pinning' the
image on the positions of known stars), and figures out the
photometric zero-point for the image.

Module membership
=================

This task is implemented in the ``lsst.pipe.tasks`` module.

See also
=========


Configuration
=============

Flags  and utility variables
----------------------------

-	doCalibrate - (`bool`) - defaults to `True` - Perform calibration?
 

Subtasks
--------

-	isr -  target=IsrTask - Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:

	- assemble raw amplifier images into an exposure with image, variance and mask planes
	- perform bias subtraction, flat fielding, etc.
	- mask known bad pixels
	- provide a preliminary WCS
		
-	charImage - target=CharacterizeImageTask - Task to characterize a science exposure, the steps of image characterization are to:

	- detect sources, usually at high S/N
	- estimate the background, which is subtracted from the image and returned as field "background"
	- estimate a PSF model, which is added to the exposure
	- interpolate over defects and cosmic rays, updating the image, variance and mask planes
    
 
-	calibrate - target=CalibrateTask - Task to perform astrometric and photometric calibration, the steps are to:

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
