
1/4

SnapCombineTask
=========================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1snap_combine_1_1_snap_combine_task.html#SnapCombineTask_

Combine snaps.

How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files.

The available variables in SnapCombineTask are:

- display -- A dictionary containing debug point names as keys with frame number as value. Valid keys are:

- repair0 -- Display the first snap after repairing.
- repair1 -- Display the second snap after repairing.

Specific functions of class
+++++++++++++++++++++++++++

__init__
---------


run
---------

Combine two snaps

- @param[in] snap0: snapshot exposure 0
- @param[in] snap1: snapshot exposure 1
- @defects[in] defect list (for repair task)
- @return a pipe_base Struct with fields:
  - exposure: snap-combined exposure
  - sources: detected sources, or None if detection not performed

  
addSnaps
---------
Add two snap exposures together, returning a new exposure

- @param[in] snap0 snap exposure 0
- @param[in] snap1 snap exposure 1
- @return combined exposure


fixMetadata
------------
Fix the metadata of the combined exposure (in place)

This implementation handles items specified by config.averageKeys and
config.sumKeys, which have data type restrictions. To handle other
data types (such as sexagesimal positions and ISO dates) you must
supplement this method with your own code.

- @param[in,out] combinedMetadata metadata of combined exposure;
    on input this is a deep copy of metadata0 (a PropertySet)
- @param[in] metadata0 metadata of snap0 (a PropertySet)
- @param[in] metadata1 metadata of snap1 (a PropertySet)

- @note --  the inputs are presently PropertySets due to ticket
#2542. However, in some sense they are just PropertyLists that are
missing some methods. In particular: comments and order are preserved
if you alter an existing value with set(key, value).

makeInitialPsf
---------------
Initialise the detection procedure by setting the PSF and WCS

- @param exposure -- Exposure to process
- @return -- PSF, WCS 



Examples
++++++++

None Given.

What it returns
+++++++++++++++

