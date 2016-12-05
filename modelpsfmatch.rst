
ModelPsfMatchTask
==================

Matching of two model Psfs, and application of the Psf-matching kernel to an input Exposure

This Task differs from ImagePsfMatchTask in that it matches two Psf models, by realizing them in an Exposure-sized SpatialCellSet and then inserting each Psf-image pair into KernelCandidates. Because none of the pairs of sources that are to be matched should be invalid, all sigma clipping is turned off in ModelPsfMatchConfig. And because there is no tracked variance in the Psf images, the debugging and logging QA info should be interpreted with caution.

One item of note is that the sizes of Psf models are fixed (e.g. its defined as a 21x21 matrix). When the Psf-matching kernel is being solved for, the Psf "image" is convolved with each kernel basis function, leading to a loss of information around the borders. This pixel loss will be problematic for the numerical stability of the kernel solution if the size of the convolution kernel (set by ModelPsfMatchConfig.kernelSize) is much bigger than: psfSize/2. Thus the sizes of Psf-model matching kernels are typically smaller than their image-matching counterparts. If the size of the kernel is too small, the convolved stars will look "boxy"; if the kernel is too large, the kernel solution will be "noisy". This is a trade-off that needs careful attention for a given dataset.

The primary use case for this Task is in matching an Exposure to a constant-across-the-sky Psf model for the purposes of image coaddition. It is important to note that in the code, the "template" Psf is the Psf that the science image gets matched to. In this sense the order of template and science image are reversed, compared to ImagePsfMatchTask, which operates on the template image.


How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d/–debug to import debug.py from your PYTHONPATH.

Specific functions of class
+++++++++++++++++++++++++++

diagnostic
----------

Print diagnostic information on spatial kernel and background fit.

Build a SpatialCellSet for use with the solve method. 

buildCellSet
-------------
Build a SpatialCellSet for use with the solve method.




Examples
++++++++

This code is modelPsfMatchTask.py in the examples directory of ipdiffim (described in detail on the doxygen page).  Works perfectly locally and on curstack, with a few lines of printout to screen.

What it returns
+++++++++++++++

Returns

- psfMatchedExposure: the Psf-matched Exposure. This has the same parent bbox, Wcs, Calib and Filter as the input Exposure but no Psf. In theory the Psf should equal referencePsfModel but the match is likely not exact.

- psfMatchingKernel: the spatially varying Psf-matching kernel

- kernelCellSet: SpatialCellSet used to solve for the Psf-matching kernel
