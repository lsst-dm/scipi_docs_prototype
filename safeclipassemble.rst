
SafeClipAssembleCoaddTask
=========


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1assemble_coadd_1_1_safe_clip_assemble_coadd_task.html#SafeClipAssembleCoaddTask_


Assemble a coadded image from a set of coadded temporary exposures, being careful to clip & flag areas with potential artifacts.

Read the documentation for AssembleCoaddTask first since SafeClipAssembleCoaddTask subtasks that task. In AssembleCoaddTask, we compute the coadd as an clipped mean (i.e. we clip outliers). The problem with doing this is that when computing the coadd PSF at a given location, individual visit PSFs from visits with outlier pixels contribute to the coadd PSF and cannot be treated correctly. In this task, we correct for this behavior by creating a new badMaskPlane 'CLIPPED'. We populate this plane on the input coaddTempExps and the final coadd where i. difference imaging suggests that there is an outlier and ii. this outlier appears on only one or two images. Such regions will not contribute to the final coadd. Furthermore, any routine to determine the coadd PSF can now be cognizant of clipped regions. Note that the algorithm implemented by this task is preliminary and works correctly for HSC data. Parameter modifications and or considerable redesigning of the algorithm is likley required for other surveys.

SafeClipAssembleCoaddTask uses a clipDetection subtask and also sub-classes AssembleCoaddTask. You can retarget the clipDetection subtask if you wish.


How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files. SafeClipAssembleCoaddTask has no debug variables of its own. The clipDetection subtasks may support debug variables.

Specific functions of class
+++++++++++++++++++++++++++

assemble
---------

Assemble the coadd for a region.
	
buildDifferenceImage
---------------------

Return an exposure that contains the difference between and unclipped and clipped coadds.

detectClip
----------

Detect clipped regions on an exposure and set the mask on the individual tempExp masks.

Detect footprints in the difference image after smoothing the difference image with a Gaussian kernal. Identify footprints that overlap with one or two input coaddTempExps by comparing the computed overlap fraction to thresholds set in the config. A different threshold is applied depending on the number of overlapping visits (restricted to one or two). If the overlap exceeds the thresholds, the footprint is considered "CLIPPED" and is marked as such on the coaddTempExp. Return a struct with the clipped footprints, the indices of the coaddTempExps that end up overlapping with the clipped footprints and a list of new masks for the coaddTempExps.

Returns struct containing:

- clippedFootprints: list of clipped footprints
- clippedIndices: indices for each clippedFootprint in tempExpRefList
- tempExpClipList: list of new masks for tempExp


detectClipBig
-------------

Find footprints from individual tempExp footprints for large footprints,
	
Examples
++++++++

This code is assembleCoadd.py in the examples directory (described in detail on the doxygen page).

What it returns
+++++++++++++++



