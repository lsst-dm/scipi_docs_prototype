
2/4

CharacterizeTask.doxygenVersion
================


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1characterize_image_1_1_characterize_image_task.html#CharacterizeImageTask_

Given an exposure with defects repaired (masked and interpolated over,
e.g. as output by IsrTask), this task does the kinds of things
normally associated with e.g. SExtractor and PSFex.

Some of its primary functions are to:

  - Detect and measure bright sources

  - Repair cosmic rays

  - Measure and subtract background

  - Measure the PSF



Debugging
+++++++++

The command line task interface for charImg supports a flag '--debug'
to import debug.py from your $PYTHONPATH; see `Using lsstDebug to
control debugging output`_ for more about debug.py.

.. _Using lsstDebug to control debugging output: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/base_debug.html

CharacterizeImageTask has a debug dictionary with the following keys:

- frame
int: if specified, the frame of first debug image displayed (defaults to 1)

- repair_iter
bool; if True display image after each repair in the measure PSF loop

- background_iter
bool; if True display image after each background subtraction in the measure PSF loop

- measure_iter
bool; if True display image and sources at the end of each iteration of the measure PSF loop See lsst.meas.astrom.displayAstrometry for the meaning of the various symbols.

- psf
bool; if True display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true

-repair
bool; if True display image and sources after final repair

-measure
bool; if True display image and sources after final measurement



Specific functions of CharImg
+++++++++++++++++++++++++++++++++++++++++

Overall: Once the exposures are processed initially minimally by IsrTask, it is passed here to CharImg.

The primary workhorse functions are:

   - Characterize the image: measure bright sources, fit a background and initial PSF, and repair cosmic rays
     
   - Detect and Measure the PSF: 

Characterize (*characterize*)
------------------------------

The first thing this function does is check to see if the exposure has
a PSF, and if a specific flag that tells the code whether to measure
the PSF (config.doMeasurePsf flag) is set true.  If *both* of these
are false (i.e. it doesn't currently have a PSF, and it is not
supposed to measure a PSF either), a run-time error is raised, because
in this case, there would be no PSF to analyze the image with
subsequently, which would be a problem.


Next an initial background is estimated (by calling the 
`estimateBackground`_ function), since this will be needed to make
basic photometric measurements.

.. _estimateBackground: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/estimate_background_8py-example.html

After this, the next step is to do a straight subtraction of this
background from the image itself, which is a necessary prerequisite to
extracting out the actual objects in the image.

Now a loop is executed a set number of times predetermined by a
configuration parameter (*psfIterations*), and inside of this the PSF
is determined iteratively (by calling the
*detectMeasureAndEstimatePsf* method of charImg itself, detailed
below).  It's done this way so that every time it passes through and
detects cosmic rays or the number of sources better than before, a
better PSF is then determined.

..
  a certain number. Constructs a PSF by calling the detectMeasureAndEstimatePsf function of this same class.

  This detect and measures sources and estimates the PSF.

  Perform final measurement with final PSF, including measuring and applying aperture correction (...?)

Once the loop is exited and the final PSF has been determined, then
actual interpolation over cosmic rays is done and they are fully
removed from the image permanently -- this is the optimal point to do
this, as you are no longer then trying to optimize anything about the
PSF or source catalog at this point.

(If desired, various displays to the screen of the screen and CR
interpolation are done, for debugging purposes.)

Now with the CR's interpolated over, sources extracted, and PSF and
background determined, a function is called to do the final
determination of the sources catalog and the actual image exposure
(the *measure* function of *detectAndMeasure.py*, in pipe_tasks.)

(And again, if desired, displays to the screen of the results of
*measure*, for debugging purposes.)


Detect, Measure, and Estimate Psf (*detectMeasureAndEstimatePsf*) 
-----------------------------------------------------------------

This function does not stand on its own, but is called by
*characterize* above.  The first thing done here is to install a
simple PSF model (replacing the existing one, if need be, using the
function *installSimplePsf* which points by default to
`InstallGaussianPsfTask`_ ).  Next run is the CR repair function
(which calls `RepairTask`_), to detect where the CR's are, but at this
point interpolation over cosmic rays is not done (we do that in
*characterize*, once we have the final PSF model).  We do want to know
where the CR's are at this point though in order to properly do source
detection, which is indeed the next step (through the *run* function
of *detectAndMeasure.py*).  A deblender is also run at this point, to
separate the overlapping sources.  Further, a version of the PSF in a
*cellSet* format, is created here, based on the source catalog.

.. _InstallGaussianPsfTask: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1algorithms_1_1install_gaussian_psf_1_1_install_gaussian_psf_task.html#InstallGaussianPsfTask_

.. _RepairTask: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1repair_1_1_repair_task.html#RepairTask_


At the end, a source catalog, background, and PSF model are returned
to the calling function (i.e. *characterize*).

..
 Cosmic Ray Repair (done within *characterize*)
 -------------------------------------------------

 CharImg first detects CR's using the function *RepairTask*, whose
 purpose is to initially detect the CR streaks, and then to
 interpolate smoothly over them so that they are entirely masked out.


..
  467         - interpolate over cosmic rays with keepCRs=True
  468         - estimate background and subtract it from the exposure
  469         - detect, deblend and measure sources, and subtract a refined background model;
  470         - if config.doMeasurePsf:

Examples
---------

See calibImg.
