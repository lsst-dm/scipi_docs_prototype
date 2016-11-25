
DecorrelateALKernelTask
========================


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1diffim_1_1image_decorrelation_1_1_decorrelate_a_l_kernel_task.html#DecorrelateALKernelTask_


Decorrelate the effect of convolution by Alard-Lupton matching kernel in image difference. 

Pipe-task that removes the neighboring-pixel covariance in an image
difference that are added when the template image is convolved with
the Alard-Lupton PSF matching kernel.

The image differencing pipeline task PSFMatchTask and PSFMatchConfigAL
uses the Alard and Lupton (1998) method for matching the PSFs of the
template and science exposures prior to subtraction. The Alard-Lupton
method identifies a matching kernel, which is then (typically)
convolved with the template image to perform PSF matching. This
convolution has the effect of adding covariance between neighboring
pixels in the template image, which is then added to the image
difference by subtraction.

The pixel covariance may be corrected by whitening the noise of the
image difference. This task performs such a decorrelation by computing
a decorrelation kernel (based upon the A&L matching kernel and
variances in the template and science images) and convolving the image
difference with it. This process is described in detail in DMTN-021.

Perform decorrelation of an image difference exposure. Decorrelates
the diffim due to the convolution of the templateExposure with the A&L
PSF matching kernel. Currently can accept a spatially varying matching
kernel but in this case it simply uses a static kernel from the center
of the exposure. The decorrelation is described in DMTN-021, Equation
1, where exposure is I_1; templateExposure is I_2; subtractedExposure
is D(k); psfMatchingKernel is kappa; and svar and tvar are their
respective variances.

How to call with options/flags
++++++++++++++++++++++++++++++


Debugging
+++++++++ 

This task has no debug variables


Specific functions of class
+++++++++++++++++++++++++++

computeDecorrelationKernel
---------------------------

Compute the Lupton/ZOGY post-convolution kernel for decorrelating an image difference, based on the PSF-matching kernel.


doConvolve
----------
Convolve an Exposure with a decorrelation convolution kernel.

fixEvenKernel
-------------
Take a kernel with even dimensions and make them odd, centered correctly.

fixOddKernel
------------
Take a kernel with odd dimensions and make them even for FFT.

computeCorrectedDiffimPsf
--------------------------

Compute the (decorrelated) difference image's new PSF.

$new_psf = psf(k) * sqrt((svar + tvar) / (svar + tvar * kappa_ft(k)**2))$

computeVarianceMean
--------------------



Examples
++++++++

This task has no standalone example, however it is applied as a subtask of ImageDifferenceTask .

What it returns
+++++++++++++++

A pipeBase.Struct containing:

- correctedExposure: the decorrelated diffim

- correctionKernel: the decorrelation correction kernel (which may be ignored)
