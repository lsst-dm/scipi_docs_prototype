
#########################
SafeClipAssembleCoaddTask
#########################


Assemble a coadded image from a set of coadded temporary exposures, being careful to clip & flag areas with potential artifacts.

In more detail: Read the documentation for AssembleCoaddTask first since SafeClipAssembleCoaddTask subtasks that task. In AssembleCoaddTask, we compute the coadd as an clipped mean (i.e. we clip outliers). The problem with doing this is that when computing the coadd PSF at a given location, individual visit PSFs from visits with outlier pixels contribute to the coadd PSF and cannot be treated correctly.

In this task, we correct for this behavior by:

- First creating a new badMaskPlane 'CLIPPED'.

- We then populate this plane on the input coaddTempExps and the final coadd where:

  - difference imaging suggests that there is an outlier and
  - this outlier appears on only one or two images.

Such regions will not contribute to the final coadd. Furthermore, any routine to determine the coadd PSF can now be cognizant of clipped regions.

Note that the algorithm implemented by this task is preliminary and works correctly for HSC data. Parameter modifications and or considerable redesigning of the algorithm is likley required for other surveys.

SafeClipAssembleCoaddTask uses a clipDetection subtask and also sub-classes AssembleCoaddTask. You can retarget the clipDetection subtask if you wish.

SafeClipAssembleCoaddTask is implemented in the ``lsst.pipe.tasks`` module.
 

..
 See also
 =========

Configuration
=============

Flags  and utility variables
----------------------------

Subtasks
--------

Entrypoint
==========


Butler Inputs
=============

Butler Outputs
==============

Examples
========

This code is assembleCoadd.py [needs filling out]

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files. SafeClipAssembleCoaddTask has no debug variables of its own. The clipDetection subtasks may support debug variables.

Algorithm details
====================

	





