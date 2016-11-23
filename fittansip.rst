
FitTanSipWcsTask
================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1astrom_1_1fit_tan_sip_wcs_1_1_fit_tan_sip_wcs_task.html

Fit a TAN-SIP WCS given a list of reference object/source matches.

Fit a TAN-SIP WCS given a list of reference object/source matches. See CreateWithSip.h for information about the fitting algorithm.




How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

FitTanSipWcsTask does not support any debug variables.


Specific functions of class
+++++++++++++++++++++++++++


fitWcs
-------
Fit a TAN-SIP WCS from a list of reference object/source matches. More...
 
Returns an lsst.pipe.base.Struct with the following fields:

- wcs -- the fit WCS as an lsst.afw.image.Wcs

- scatterOnSky -- median on-sky separation between reference objects and sources in "matches", as an lsst.afw.geom.Angle

initialWcs
---------- 
Generate a guess Wcs from the astrometric matches

We create a Wcs anchored at the center of the matches, with the scale
of the input Wcs.  This is necessary because matching returns only
matches with no estimated Wcs, and the input Wcs is a wild guess.
We're using the best of each: positions from the matches, and scale
from the input Wcs.

rejectMatches
------------- 
Flag deviant matches

We return a boolean numpy array indicating whether the corresponding
match should be rejected.  The previous list of rejections is used
so we can calculate uncontaminated statistics.

plotFit
-------
Plot the fit

We create four plots, for all combinations of (dx, dy) against
(x, y).  Good points are black, while rejected points are red.

_fitWcs
-------
Fit a Wcs based on the matches and a guess Wcs



Examples
++++++++

FitTanSipWcsTask is a subtask of AstrometryTask, which is called by photoCalTask.py in $PIPE_TASKS_DIR.




What it returns
+++++++++++++++

