
2/4

ProcessCCD
================


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1process_ccd_1_1_process_ccd_task.html#ProcessCcdTask_


Next, we will look at the actual steps of how an image is processed
from raw data to a science-grade image that can be used in analyses.

Let’s do this by looking inside the primary function which does this
in the stack -- processCcd.py, which can be executed as so::

  processCcd.py pathTo/DATA --VariousFlags

(Writing the cmd as ' processCcd.py' directly on the cmd line works
because processCcd.py is actually an executable which will be in your
path when it has been set up correctly, which happens as part of the
DM Stack install.)
	
Real example version from the ci_hsc dir to be tried::

  processCcd.py $LSSTSW/ci_hsc/DATA --rerun ci_hsc --id visit=903986 ccd=23 --doraise

This uses a ‘dataId’, which is a unique identifier for a specific data
input. This can come in different formats, the one shown here (after the '--id' flag) uses the
‘visit’ , ‘ccd’ identifiers used to refer to a specific CCD in a
specific exposure (called a ‘visit’).

The term 'rerun' originated in SDSS. It simply refers to a single
processing run, performed with a specified version of the reduction
code, and with a specific set of configuration parameters. The
assumption is that within a given rerun, the data have been handled
in a homogeneous way.

Setting the 'doRaise' flag will raise an exception on error (or else it
would log a message and continue).
			

Overview of what ProcessCcd.py Does
+++++++++++++++++++++++++++++++++++

ProcessCcd as a whole executes many of the functions that are in
multiple packages in other astronomy analysis frameworks.

The initial step is to correct the images for all the issues involved
in taking a raw image CCD through to a processed one (e.g. doing the
bias and dark current corrections, flat-fielding, etc.) by first doing
everything that astronomers have used a medley of customized codes
typically for each telescope before (like IRAF, UNIX shellscripts, IDL
scripts etc.).  These tasks are usually grouped together under the
general term 'Instrumental Signature Removal.'

The second step groups together several functions as 'Image
Characterization', which includes for our purposes: object detection
(very commonly done by Source Extractor), repairing of cosmic ray
defects, measuring and subtracting of sky background, and then finally
measuring bright sources and using this to estimate background and PSF
of an exposure (which is often done currently by astronomers using the
PSFex code).

The last primary grouping of taks is what we will call 'Image
Calibration', which measures faint sources, does the astrometry by
fitting an improved WCS to the image (often done currently by
astronomers using by using the SCAMP and SWARP codes, 'pinning' the
image on the positions of known stars), and figures out the
photometric zero-point for the image.


How to use the ProcessCcd Task
++++++++++++++++++++++++++++++

This task is primarily designed to be run from the command line.  The
main method is 'run', which takes a single (butler) data reference for the
raw input data (i.e. the directory in which all the raw data files are
stored, and where all the processed data files are to be written).

..
 Preparing the data for ProcessCcd 
 ---------------------------------




Configuration parameters
------------------------

The Task has several Configurable Fields (functions of the pexConfig class):

  - isr, which has as its target IsrTask

  - charImage, which has as its target CharacterizeImageTask

  - calibrate, which has as its target CalibrateTask

    
Debugging
----------

ProcessCcdTask has no debug output, but its several subtasks do.

Brief Outline with Subtask Code Names
++++++++++++++++++++++++++++++++++++++

Now the most general outline of the steps processCcd takes:

1. Does the Instrumental Signature Removal (ISR): it calls IsrTask.py to
   process the raw data and assemble it into a post-ISR exposure.
   
2. Characterizes the image to estimate PSF and background: Calls
   CharacterizeImageTask.py charImage which subtracts the background,
   fits a PSF model, repairs cosmic rays, detects and measures bright
   sources, and measures the aperture correction.
   
3. Calibrate astrometry and photometry: Calls calibrateTask to perform deep
   detection, deblending and single-frame measurement, refine the WCS
   and fit the photometric zero-points.

Examples
---------

The one listed on the doxygen page works all the way straight through on tiger.
