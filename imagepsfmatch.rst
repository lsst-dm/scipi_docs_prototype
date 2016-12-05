
ImagePsfMatchTask
==================

Psf-match two MaskedImages or Exposures using the sources in the images.

Build a Psf-matching kernel using two input images, either as MaskedImages (in which case they need to be astrometrically aligned) or Exposures (in which case astrometric alignment will happen by default but may be turned off). This requires a list of input Sources which may be provided by the calling Task; if not, the Task will perform a coarse source detection and selection for this purpose. Sources are vetted for signal-to-noise and masked pixels (in both the template and science image), and substamps around each acceptable source are extracted and used to create an instance of KernelCandidate. Each KernelCandidate is then placed within a lsst.afw.math.SpatialCellSet, which is used by an ensemble of lsst.afw.math.CandidateVisitor instances to build the Psf-matching kernel. These visitors include, in the order that they are called: BuildSingleKernelVisitor, KernelSumVisitor, BuildSpatialKernelVisitor, and AssessSpatialKernelVisitor.

Sigma clipping of KernelCandidates is performed as follows:


- BuildSingleKernelVisitor, using the substamp diffim residuals from the per-source kernel fit, if PsfMatchConfig.singleKernelClipping is True

- KernelSumVisitor, using the mean and standard deviation of the kernel sum from all candidates, if PsfMatchConfig.kernelSumClipping is True

- AssessSpatialKernelVisitor, using the substamp diffim residuals from the spatial kernel fit, if PsfMatchConfig.spatialKernelClipping is True

  The actual solving for the kernel (and differential background model) happens in lsst.ip.diffim.PsfMatchTask._solve. This involves a loop over the SpatialCellSet that first builds the per-candidate matching kernel for the requested number of KernelCandidates per cell (PsfMatchConfig.nStarPerCell). The quality of this initial per-candidate difference image is examined, using moments of the pixel residuals in the difference image normalized by the square root of the variance (i.e. sigma); ideally this should follow a normal (0, 1) distribution, but the rejection thresholds are set by the config (PsfMatchConfig.candidateResidualMeanMax and PsfMatchConfig.candidateResidualStdMax). All candidates that pass this initial build are then examined en masse to find the mean/stdev of the kernel sums across all candidates. Objects that are significantly above or below the mean, typically due to variability or sources that are saturated in one image but not the other, are also rejected. This threshold is defined by PsfMatchConfig.maxKsumSigma. Finally, a spatial model is built using all currently-acceptable candidates, and the spatial model used to derive a second set of (spatial) residuals which are again used to reject bad candidates, using the same thresholds as above.



How to call with options/flags
++++++++++++++++++++++++++++++

There is no run() method for this Task. Instead there are 4 methods that may be used to invoke the Psf-matching. These are matchMaskedImages, subtractMaskedImages, matchExposures, and subtractExposures.

Debugging
+++++++++ 

The command line task interface supports a flag -d/–debug to import debug.py from your PYTHONPATH.

Specific functions of class
+++++++++++++++++++++++++++

getFwhmPix
----------
Return the FWHM in pixels of a Psf. 
 
matchExposures
----------------
Warp and PSF-match an exposure to the reference.
 
matchMaskedImages
------------------
PSF-match a MaskedImage (templateMaskedImage) to a reference MaskedImage (scienceMaskedImage)
 

subtractExposures
------------------
Register, Psf-match and subtract two Exposures. 
 
subtractMaskedImages
--------------------
Psf-match and subtract two MaskedImages. 
 

getSelectSources
------------------
Get sources to use for Psf-matching. 
 

makeCandidateList
-----------------
Make a list of acceptable KernelCandidates. 

	

Examples
++++++++

This code is imagePsfMatchTask.py in the examples directory of $IP_DIFFIM_DIR (described in detail on the doxygen page).  Works perfectly locally and on curstack, giving steady printing info to the screen as it goes.

What it returns
+++++++++++++++

