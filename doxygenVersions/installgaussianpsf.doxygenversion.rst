
InstallGaussianPsfTask.doxversion
=========================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1algorithms_1_1install_gaussian_psf_1_1_install_gaussian_psf_task.html#InstallGaussianPsfTask_

Install a Gaussian PSF model in an exposure. If the exposure already has a PSF model then the new model has the same sigma and size (width and height in pixels) of the existing model. If the exposure does not have a PSF model then the PSF sigma and size are taken from the config.

At present the produced model is always circularly symmetric, but it is planned to change this to an elliptical PSF model (only for the case that the exposure already has a PSF model), once the necessary PSF object is available.

A variant of this task may someday exist to estimate the PSF from the pixel data if no PSF model is present.


How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

This task has no debug display.


Specific functions of class
+++++++++++++++++++++++++++

run
---

Set exposure's PSF to a simple PSF model.

The sigma and width of the new simple PSF model matches the sigma and width of the current model, if any, else the config parameters are used.

Parameters:
- [in,out]	exposure --	exposure to which to replace or add the PSF model

Examples
++++++++

The whole example is simply spelled out in detail on the doxygen page.  It's brief.
 
What it returns
+++++++++++++++

