Ingesting
=========


>>>> This is actually not on the Doxygen Task list page.

The first thing a user needs to do to process any image is ingest data files on disk.

The LSST DM Stack uses EUPS to manage the software packages and versions to be used, so we first take care of those commands.

Execute the correct EUPS setups, as so::

  cd  $LSSTSW/ci_hsc
  setup lsst_apps -t TagNumberYouInstalledWith
  setup   -r $LSSTSW/obs_subaru -t TagNumberYouInstalledWith
  setup   -k -r $LSSTSW/ci_hsc -t TagNumberYouInstalledWith

After this, we will ingest FITS files using the ingestImages Task as
so::

 python $PIPE_TASKS_DIR/bin/ingestImages.py $LSSTSW/ci_hsc/DATA $LSSTSW/ci_hsc/raw/*.fits  --mode=link -c clobber=True register.ignore=True --doraise  

This will write out a registry.sqlite3 in your DATA subdir and make
links to the science and calibration exposures, so you can start the
processing commands on them.
