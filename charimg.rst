
################
CharacterizeTask
################

Given an exposure with defects repaired (masked and interpolated over,
e.g. as output by IsrTask), this task does the kinds of things
normally associated with e.g. SExtractor and PSFex.

Some of its primary functions are to:

  - Detect and measure bright sources

  - Repair cosmic rays

  - Measure and subtract background

  - Measure the PSF

In more detail: the first thing the entrypoint function
``lsst.pipe.tasks.characterizeImage.run`` does after checking if the
``doUnpersist`` flag is set is to simply unpack the exposure (passed
in as a `dataRef`) into `exposure`, `exposureIdInfo` and `background`
and then pass it to the characterize method to do the work.

Inside ``lsst.pipe.tasks.characterizeImage.characterize`` the code
checks to see if the exposure has a PSF, and if the
`config.doMeasurePsf` flag that tells the code whether to measure the
PSF is set `True`.  If *both* of these are false (i.e. it doesn't
currently have a PSF, and it is not supposed to measure a PSF either),
a run-time error is raised, because in this case, there would be no
PSF to analyze the image with subsequently, which would be a problem.

Next an initial background is estimated (by calling the
``lsst.meas.algorithms.estimateBackground`` function), since this will
be needed to make basic photometric measurements.

After this, the next step is to do a straight subtraction of this
background from the image itself, pixel by pixel, which is a necessary
prerequisite to extracting out the actual objects in the image.

Now a loop is executed a set number of times predetermined by a
configuration parameter (`psfIterations`), and inside of this the PSF
is determined iteratively (by calling the
``lsst.pipe.tasks.characterizeImage.detectMeasureAndEstimatePsf``
method, detailed below).  It's done this way so that every time it
passes through and detects cosmic rays or the number of sources better
than before, a better PSF is then determined.

This task is implemented in the ``lsst.pipe.tasks`` module.

Configuration
=============

Flags  and utility variables
----------------------------

- 	doDeblend - (`bool`) - defaults to `True` - Run deblender on input exposure?
 
- 	doApCorr - (`bool`) - defaults to `True` -  Run subtasks to measure and apply aperture corrections

-	doMeasurePsf - (`bool`) - defaults to `True` - Measure the PSF? If `False` then keep the existing PSF model (which must exist) and use that model for all operations."
 
-	doWrite - (`bool`) - defaults to `True` - Persist results?
 
-	doWriteExposure - (`bool`) - defaults to `True` - Write icExp and icExpBackground in addition to icSrc? Ignored if doWrite False.

-	useSimplePsf - (`bool`) - defaults to `True` - Replace the existing PSF model with a simplified version that has the same sigma at the start of each PSF determination iteration? Doing so makes PSF determination converge more robustly and quickly.

	
-	psfIterations - (`int`) - defaults to 2, min=1 -    Number of iterations of detect sources, measure sources, estimate PSF. If `useSimplePsf`='all_iter' then 2 should be plenty; otherwise more may be wanted.  ******** This seems to be an error, as `useSimplePsf` is described as a `bool` in the dox pages.

- 	checkUnitsParseStrict (`str`) - Strictness of Astropy unit compatibility check, can be 'raise', 'warn' or 'silent'

Subtasks
--------

-	background - target = SubtractBackgroundTask -    Configuration for initial background estimation
 
-	detection - target = SourceDetectionTask - Detect sources
 
-	deblend - target = SourceDeblendTask - Split blended source into their components
 
-	measurement - target = SingleFrameMeasurementTask - Measure sources
 
-	measureApCorr -  target = MeasureApCorrTask - Subtask to measure aperture corrections
 
-	applyApCorr - target = ApplyApCorrTask - Subtask to apply aperture corrections
 
-	catalogCalculation - target = CatalogCalculationTask - Subtask to run catalogCalculation plugins on catalog
 
-	installSimplePsf -  target = InstallGaussianPsfTask - Install a simple PSF model
 
-	refObjLoader -  target = LoadAstrometryNetObjectsTask - Reference object loader
 
-	astrometry - target = AstrometryTask - Task to load and match reference objects. Only used if `measurePsf` can use matches. Warning: matching will only work well if the initial WCS is accurate enough to give good matches (roughly: good to 3 arcsec across the CCD).

-	measurePsf - target = MeasurePsfTask - Measure PSF

 
-	repair -  target = RepairTask - Remove cosmic rays
 
------> [Where does the validate function go..?  And setDefaults?]


Entrypoint
==========

- ``lsst.pipe.tasks.characterizeImage.run`` 


Butler Inputs
=============

- A butler object is passed to the `refObjLoader` constructor in case it is needed to load catalogs. May be `None` if a catalog-based star selector is not used, if the reference object loader constructor does not require a butler, or if a reference object loader is passed directly via the `refObjLoader` argument.


Examples
========

Thi code is in `calibrateTask.py` (which calls `CharacterizeImageTask` before calling `CalibrateTask`) in the `$PIPE_TASKS/examples` directory, and can be run as, e.g.::

     python examples/calibrateTask.py --display



Debugging
=========

- frame = (`int`) - if specified, the frame of first debug image displayed (defaults to 1)

- repair_iter - (`bool`) -  if `True` display image after each repair in the measure PSF loop

- background_iter - (`bool`) -  if `True` display image after each background subtraction in the measure PSF loop

- measure_iter - (`bool`) -  if `True` display image and sources at the end of each iteration of the measure PSF loop See lsst.meas.astrom.displayAstrometry for the meaning of the various symbols.

- psf - (`bool`) -  if `True` display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true

- repair - (`bool`) -  if `True` display image and sources after final repair

- measure - (`bool`) -  if `True` display image and sources after final measurement



