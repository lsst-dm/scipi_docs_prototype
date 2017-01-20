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
