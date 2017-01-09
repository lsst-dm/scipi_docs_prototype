
PsfMatchTask.doxversion
=============

Base class for Psf Matching; should not be called directly.

PsfMatchTask is a base class that implements the core functionality for matching the Psfs of two images using a spatially varying Psf-matching lsst.afw.math.LinearCombinationKernel. The Task requires the user to provide an instance of an lsst.afw.math.SpatialCellSet, filled with lsst.ip.diffim.KernelCandidate instances, and an lsst.afw.math.KernelList of basis shapes that will be used for the decomposition. If requested, the Task also performs background matching and returns the differential background model as an lsst.afw.math.Kernel.SpatialFunction.


How to call with options/flags
++++++++++++++++++++++++++++++


As a base class, this Task is not directly invoked. However, run() methods that are implemented on derived classes will make use of the core _solve() functionality, which defines a sequence of lsst.afw.math.CandidateVisitor classes that iterate through the KernelCandidates, first building up a per-candidate solution and then building up a spatial model from the ensemble of candidates. Sigma clipping is performed using the mean and standard deviation of all kernel sums (to reject variable objects), on the per-candidate substamp diffim residuals (to indicate a bad choice of kernel basis shapes for that particular object), and on the substamp diffim residuals using the spatial kernel fit (to indicate a bad choice of spatial kernel order, or poor constraints on the spatial model). The _diagnostic() method logs information on the quality of the spatial fit, and also modifies the Task metadata.


Debugging
+++++++++ 

Specific functions of class
+++++++++++++++++++++++++++

createPcaBasis
--------------

Creates Principal Component basis.  If a principal component analysis is requested, typically when using a delta function basis, perform the PCA here and return a new basis list containing the new principal components.

Returns:

- nRejectedPca: number of KernelCandidates rejected during PCA loop
- spatialBasisList: basis list containing the principal shapes as Kernels

buildCellSet
------------

diagnostic
----------
Provide logging diagnostics on quality of spatial kernel fit.


displayDebug
------------

Provide visualization of the inputs and ouputs to the Psf-matching code.

solve
------

Solves for the PSF matching kernel.

Returns:

- psfMatchingKernel: PSF matching kernel
- backgroundModel: differential background model



Examples
++++++++

As a base class, there is no example code for PsfMatchTask. However, see ImagePsfMatchTask, SnapPsfMatchTask, and ModelPsfMatchTask.


What it returns
+++++++++++++++

