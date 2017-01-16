

##############
ProcessCcdTask
##############

ProcessCcdTask (available as the ``processCcd.py`` ``command line
task``) executes the steps of how an image is processed from raw data
(taking as input to its ``run`` method a single butler data reference
for ``raw`` data), finally to science-grade images (``FITS files``) and
catalogs (``FITS tables``) that can be used in further analyses.

In more detail, ProcessCcdTask executes the following steps:


- 1.  ``Instrument Signature Removal`` -- Implemented by the :doc:`IsrTask <isrtask>` sub-task (isr configuration), this step removes CCD signatures (such as bias, dark current, flat-fielding, and cross-talk) and masks bad pixels.

- 2. ``Image Characterization`` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` sub-task (charImage configuration), this step repairs cosmic ray defects, estimates and subtracts a background, does object detection, and estimates a PSF.
  
- 3. ``Image Calibration``  -- Implemented by the :doc:`CalibrateTask <calibimg>` sub-task (calibrate configuration), this step measures faint sources, fits an astrometric WCS and extracts a photometric zero-point for the image.


ProcessCcdTask is implemented in the ``lsst.pipe.tasks`` module.



Configuration
=============

Parameters
----------

-	``doCalibrate`` - (`bool`) - defaults to `True` - Perform calibration?
 

Subtasks
--------

-	``isr`` -  default target=IsrTask - Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:

	- assemble raw amplifier images into an exposure with image, variance and mask planes
	- perform bias subtraction, flat fielding, etc.
	- mask known bad pixels
	- provide a preliminary WCS
		
-	``charImage`` - default target=CharacterizeImageTask - Task to characterize a science exposure, the steps of image characterization are to:

	- detect sources, usually at high S/N
	- estimate the background, which is subtracted from the image and returned as field "background"
	- estimate a PSF model, which is added to the exposure
	- interpolate over defects and cosmic rays, updating the image, variance and mask planes
    
 
-	``calibrate`` - default target=CalibrateTask - Task to perform astrometric and photometric calibration, the steps are to:

	- refine the WCS in the exposure
	- refine the Calib photometric calibration object in the exposure
	- detect sources, usually at low S/N
 

Entrypoint
==========

- ``lsst.pipe.tasks.processCcd.ProcessCcdTask.run`` 
  

Butler Inputs
=============

The main method, ``run``, takes a single butler data reference for the ``raw`` input data.

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

Command Line Arguments
======================


positional arguments:
  input                 path to input data repository, relative to
                        $PIPE_INPUT_ROOT

optional arguments:
  -h, --help            show this help message and exit
  --calib RAWCALIB      path to input calibration repository, relative to
                        $PIPE_CALIB_ROOT
  --output RAWOUTPUT    path to output data repository (need not exist),
                        relative to $PIPE_OUTPUT_ROOT
  --rerun [INPUT:]OUTPUT
                        rerun name: sets OUTPUT to ROOT/rerun/OUTPUT;
                        optionally sets ROOT to ROOT/rerun/INPUT
  -c [NAME=VALUE [NAME=VALUE ...]], --config [NAME=VALUE [NAME=VALUE ...]]
                        config override(s), e.g. -c foo=newfoo bar.baz=3
  -C [CONFIGFILE [CONFIGFILE ...]], --configfile [CONFIGFILE [CONFIGFILE ...]]
                        config override file(s)
  -L [LEVEL|COMPONENT=LEVEL [LEVEL|COMPONENT=LEVEL ...]], --loglevel [LEVEL|COMPONENT=LEVEL [LEVEL|COMPONENT=LEVEL ...]]
                        logging level; supported levels are
                        [trace|debug|info|warn|error|fatal]
  --longlog             use a more verbose format for the logging
  --debug               enable debugging output?
  --doraise             raise an exception on error (else log a message and
                        continue)?
  --profile PROFILE     Dump cProfile statistics to filename
  --show SHOW [SHOW ...]
                        display the specified information to stdout and quit
                        (unless run is specified).
  -j PROCESSES, --processes PROCESSES
                        Number of processes to use
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout for multiprocessing; maximum wall time (sec)
  --clobber-output      remove and re-create the output directory if it
                        already exists (safe with -j, but not all other forms
                        of parallel execution)
  --clobber-config      backup and then overwrite existing config files
                        instead of checking them (safe with -j, but not all
                        other forms of parallel execution)
  --no-backup-config    Don't copy config to file~N backup.
  --clobber-versions    backup and then overwrite existing package versions

                         instead of checkingthem (safe with -j, but not all
                        other forms of parallel execution)
  --no-versions         don't check package versions; useful for development
  --id [KEY=VALUE1[^VALUE2[^VALUE3...] [KEY=VALUE1[^VALUE2[^VALUE3...] ...]]
                        data IDs, e.g. --id visit=12345 ccd=1,2^0,3

Notes:
            * --config, --configfile, --id, --loglevel and @file may appear multiple times;
                all values are used, in order left to right
            * @file reads command-line options from the specified file:
                * data may be distributed among multiple lines (e.g. one option per line)
                * data after # is treated as a comment and ignored
                * blank lines and lines starting with # are ignored
            * To specify multiple values for an option, do not use = after the option name:
                * right: --configfile foo bar
                * wrong: --configfile=foo bar



