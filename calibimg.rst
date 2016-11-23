
..
 measure faint sources, fit an improved WCS and get the photometric zero-point


CalibrateTask
=====================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1calibrate_1_1_calibrate_task.html#CalibrateTask_
   
Overall:


    Given an exposure with a good PSF model and aperture correction
    map (e.g. as provided by *CharacterizeImageTask*), we next will
    perform the following operations on it with *CalibTask*:
    
    - Run *detectAndMeasure* subtask to peform deep detection and measurement
      
    - Run astrometry subtask to fit an improved WCS

    - Run photoCal subtask to fit the exposure's photometric zero-point


      
How to call with options/flags
++++++++++++++++++++++++++++++


Debugging
+++++++++

The command line task interface supports a flag --debug to import
debug.py from your $PYTHONPATH; see `Using lsstDebug to control
debugging output`_ for more about debug.py.

..  _Using lsstDebug to control debugging output: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/base_debug.html
   
CalibrateTask has a debug dictionary containing one key:

- calibrate

frame (an int; <= 0 to not display) in which to display the exposure, sources and matches. See lsst.meas.astrom.displayAstrometry for the meaning of the various symbols.




Specific functions of CalibImg
+++++++++++++++++++++++++++++++

Primary functions:

- Calibrate

- WriteOutputs

Calibrate (*calibrate*)
------------------------

The detectAndMeasure routine is run again, yielding another version of
the source catalog, and the background.  We do it to go much deeper in
the image, this time.

Next astrometry is done against a known catalog, and all matches are
returned in a different catalog.  Then photometric calibration is done
by matching to known sources, determining a photometric zero-point and
returning the result.

These are of course the fundamental quantities required in any source
catalog, and with the running of this function, the first pass over
the image resulting in the basic catalogs LSST will produce, is done.

.. This is the first and primary
   astrometry routine.




Persisting the outputs (*writeOutputs*)
-----------------------------------------

This routine writes output data to the output repository, if the
appropriate flag (*sourceWriteFlags*) is set.  It is called by *calibrate* above.


*getSchemaCatalogs*
-------------------

Return a dict of empty catalogs for each catalog dataset produced by this task.. but never called within this class otherwise.


*setMetadata*
--------------

This function sets task and exposure metadata, and is called by *calibrate* and other functions in this class. This is because we need a function to persist all the metadata to a place when required.

*copyIcSourceFields*
--------------------

Match sources in icSourceCat (which is a source catalog from the *CharacterizeImageTask*)  and some other sourceCat and copy the specified fields.  We of course have various kinds of sourceCats, so a function to match the original sourceCat, icSourceCat, and another, and copy relevant quantities is certainly necessary and will be often used.



Examples
++++++++

This code is in calibrateTask.py in the $PIPE_TASKS/examples directory, and can be run as, e.g.:

     python examples/calibrateTask.py --display

    
What it returns
+++++++++++++++
