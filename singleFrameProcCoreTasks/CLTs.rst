:orphan: true

##################
Command Line Tasks
##################

Running a Command Line Task
===========================

We will fill information here similar to that currently at: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_base.html#pipeBase_argumentParser


.. _CLTbaseclass:

Command Line Task Base Class
============================

We will fill information here similar to that currently at: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html




.. _optionslink:

Command Line Task Options
=========================

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
