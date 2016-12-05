
SnapPsfMatchTask
=========

This Task differs from ImagePsfMatchTask in that it matches two Exposures assuming that the images have been acquired very closely in time. Under this assumption, the astrometric misalignments and/or relative distortions should be within a pixel, and the Psf-shapes should be very similar. As a consequence, the default configurations for this class assume a very simple solution.

- The spatial variation in the kernel (SnapPsfMatchConfig.spatialKernelOrder) is assumed to be zero

- With no spatial variation, we turn of the spatial clipping loops (SnapPsfMatchConfig.spatialKernelClipping)

- The differential background is not fit for (SnapPsfMatchConfig.fitForBackground)

- The kernel is expected to be appx. a delta function, and has a small size (SnapPsfMatchConfig.kernelSize)

The sub-configurations for the Alard-Lupton (SnapPsfMatchConfigAL) and delta-function (SnapPsfMatchConfigDF) bases also are designed to generate a small, simple kernel.



How to call with options/flags
++++++++++++++++++++++++++++++

The Task is only configured to have a subtractExposures method, which in turn calls ImagePsfMatchTask.subtractExposures.


Debugging
+++++++++ 

The command line task interface supports a flag -d/–debug to import debug.py from your PYTHONPATH.

Specific functions of class
+++++++++++++++++++++++++++

subtractExposures
------------------

Not described..


Examples
++++++++

There is an example called snapPsfMatchTask.py in the examples directory of ipdiffim (described in detail on the doxygen page).  This prints a boatload of info to screen, and executes just fine, locally and on curstack.

What it returns
+++++++++++++++

