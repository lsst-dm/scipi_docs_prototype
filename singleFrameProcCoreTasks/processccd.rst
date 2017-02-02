
##############
ProcessCcdTask
##############

ProcessCcdTask is a `command line task`_ which executes through its
subtasks the steps of how an image is processed from raw uncorrected
CCD-level data finally to science-grade images and catalogs.

.. _`command line task`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html

In more detail, ProcessCcdTask executes the following steps:


1.  `Instrument Signature Removal` -- Implemented by the :doc:`IsrTask <isrtask>` subtask, this step removes CCD signatures (such as bias, dark current, flat-fielding, and cross-talk) and masks bad pixels.

2. `Image Characterization` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` subtask, this step repairs cosmic ray defects, estimates and subtracts a background, does object detection, and estimates a PSF.
  
3. `Image Calibration`  -- Implemented by the :doc:`CalibrateTask <calibimg>` subtask, this step measures faint sources, fits an astrometric WCS and extracts a photometric zero-point for the image.


This task is implemented in the `lsst.pipe.tasks`_ module.

.. _lsst.pipe.tasks: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_tasks.html
    

Configuration
=============

Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	`isr`,   :doc:`IsrTask <isrtask>`, Task to perform instrumental signature removal or load a post-ISR image; the steps in ISR are to:	- assemble raw amplifier images into an exposure with image; variance and mask planes	- perform bias subtraction; flat fielding; etc.	- mask known bad pixels	- provide a preliminary WCS		
	`charImage`, :doc:`CharacterizeImageTask <charimg>`, Task to characterize a science exposure; the steps of image characterization are to:	- detect sources; usually at high S/N	- estimate the background; which is subtracted from the image and returned as field "background"	- estimate a PSF model; which is added to the exposure	- interpolate over defects and cosmic rays; updating the image; variance and mask planes
	`calibrate`,  :doc:`CalibrateTask <calibimg>`, Task to perform astrometric and photometric calibration; the steps are to:	- refine the WCS in the exposure	- refine the Calib photometric calibration object in the exposure	- detect sources; usually at low S/N

	
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

     `doCalibrate` ,`bool`, `True`, Perform calibration?

Command Line Usage
==================

ProcessCcdTask is available as the `processCcd.py`_ `command_line_task`_ and is executable directly from the command line as so::

  processCcd.py path/to/input_data [options]

.. _processCcd.py: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/process_ccd_8py_source.html

Where the path to the input data is required, but all other arguments are optional.

In addition to the table below, many more details on some of the flag arguments are available on the page describing the `pipebase task package`_ , particularly on the `--id`, `--show`, and `--config` flags.  

.. _`pipebase task package`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_base.html#pipeBase_argumentParser



Options:

.. csv-table:: 
   :header: Flag, Description
   :widths: 20, 40
	    
   -h ; --help ,           Show help message and exit
   --id, The values for this are in the format: [KEY=VALUE1[^VALUE2[^VALUE3...] [KEY=VALUE1[^VALUE2[^VALUE3...] ...]]. These are data IDs e.g. --id visit=12345 

   --calib RAWCALIB ,      Path to input calibration repository relative to $PIPE_CALIB_ROOT
   --output RAWOUTPUT,    Path to output data repository (need not yet exist) relative to $PIPE_OUTPUT_ROOT
   --rerun [INPUT:]OUTPUT,  Rerun name: sets OUTPUT to ROOT/rerun/OUTPUT; optionally sets ROOT to ROOT/rerun/INPUT
   -c [NAME=VALUE [NAME=VALUE ...]], Config override(s) ; e.g. -c foo=newfoo bar.baz=3
   --config [NAME=VALUE [NAME=VALUE ...]] , Same as -c
   -C [CONFIGFILE [CONFIGFILE ...]],   Config override file(s)
   --configfile [CONFIGFILE [CONFIGFILE ...]], Same as -C
   -L [LEVEL|COMPONENT=LEVEL],  Logging level; supported levels are [trace|debug|info|warn|error|fatal]
   --loglevel [LEVEL|COMPONENT=LEVEL], Same as -C
   --longlog,             Use a more verbose format for the logging
   --debug,               Enable debugging output?
   --doraise,             Raise an exception on error? (else log a message and continue)
			
   --profile PROFILE,     Dump cProfile statistics to filename
   --show SHOW [SHOW ...],  Display the specified information to stdout and quit (unless `run` is specified)
    -j PROCESSES,            Number of processes to use
    --processes PROCESSES, Same as -j
    -t TIMEOUT,             Timeout for multiprocessing; maximum wall time (sec)
    --timeout TIMEOUT,  Same as -t    
    --clobber-output,      Remove and re-create the output directory if it already exists (safe with -j but not all other forms of parallel execution)
    --clobber-config,      Backup and then overwrite existing config files instead of checking them (safe with -j but not all other forms of parallel execution)
    --no-backup-config,    Don't copy config to file~N backup.
    --clobber-versions,    Backup and then overwrite existing package versions instead of checking them  (safe with -j but not all other forms of parallel execution)
    --no-versions,         Don't check package versions; useful for development

     
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
 
`butler`
   The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.
 
`psfRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for image characterization. An example of when this would be used is when a CatalogStarSelector is used. May be None if the desired loader can be constructed from the butler argument or all steps requiring a catalog are disabled.
 
`astromRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`photoRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`**kwargs`
   Other keyword arguments for `lsst.pipe.base.CmdLineTask`_.

.. _`lsst.pipe.base.CmdLineTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html


Run method
----------
 
.. code-block:: python
 
   run(sensorRef)

(More info can be found at `run`_)

.. _run: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1process_ccd_1_1_process_ccd_task.html#a82488db6374fb538db2ec4418419bdd4
   
Parameters
^^^^^^^^^^
 
`sensorRef`
   Butler data reference for raw data.
 
Returns
^^^^^^^
 
`struct` - a `lsst.pipe.base.Struct`_ containing these fields:

.. _`lsst.pipe.base.Struct`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1struct_1_1_struct.html

   - `charRes`: object returned by image characterization task; an `lsst.pipe.base.Struct`_ that will include "background" and "sourceCat" fields.
   - `calibRes`: object returned by calibration task: an `lsst.pipe.base.Struct`_ that will include "background" and "sourceCat" fields
   - `exposure`: final exposure (an `lsst.afw.image.ExposureF <#>`_)
   - `background`: final background model (an lsst.afw.math.BackgroundList)
 


Examples
========

The `obs_test`_ package  models a simple camera with one CCD and includes a data repository containing a few raw images (simulating three visits, two with with the `g`-band filter, and one with the `r`-band one), and some associated calibration data. Its camera consists of a single CCD whose geometry matches a subregion of a single LSST CCD.

.. _`obs_test`: https://github.com/LSST/obs_test

The following commands will process all raw data in `obs_test`_'s data
repository. Be sure to specify a `--output` directory that does not
already exist::

  setup obs_test
  setup pipe_tasks
  processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id

The data is read from the small repository in the `obs_test`_ package and output images and catalogs are written to subdirectories in `processCcdOut` (or whatever output name you specified).

Specifying `--id` with no values processes all data.

Add the option `--help` to see more options.


Debugging
=========

ProcessCcdTask has no debug output, but its several subtasks do.


Algorithm details
=================

ProcessCcdTask is essentially a wrapper around the three subtasks, see those for actual contentful algorithmic details.
