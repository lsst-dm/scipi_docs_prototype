from lsst.afw.image import ExposureF
from lsst.meas.algorithms.installGaussianPsf import InstallGaussianPsfTask, FwhmPerSigma

exposure = ExposureF(100, 100)
task = InstallGaussianPsfTask()
task.run(exposure=exposure)

# This particular exposure had no PSF model to begin with, so the new PSF model
# uses the config's FWHM. However, measured FWHM is based on the truncated
# PSF image, so it does not exactly match the input
measFwhm = exposure.getPsf().computeShape().getDeterminantRadius() * FwhmPerSigma
assert abs(measFwhm - task.config.fwhm) < 1e-3
