
SubtractBackgroundTask
=========================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1algorithms_1_1subtract_background_1_1_subtract_background_task.html#SubtractBackgroundTask_

Fit a model of the background of an exposure and subtract it.



How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag --debug to import debug.py from your $PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py.

SubtractBackgroundTask has a debug dictionary containing three integer keys:

- unsubtracted --If >0: fitBackground displays the unsubtracted masked image overlaid with the grid of cells used to fit the background in the specified frame

- subtracted -- If >0: run displays the background-subtracted exposure is the specified frame

- background -- If >0: run displays the background image in the specified frame

Specific functions of class
+++++++++++++++++++++++++++

run
----
Fit and subtract the background of an exposure.

Parameters:

- [in,out]	exposure --	exposure whose background is to be subtracted
- [in,out]	background --	initial background model already subtracted from exposure (an lsst.afw.math.BackgroundList). May be None if no background has been subtracted.
- [in]	stats --	if True then measure the mean and variance of the full background model and record the results in the exposure's metadata
- [in]	statsKeys --	key names used to store the mean and variance of the background in the exposure's metadata (a pair of strings); if None then use ("BGMEAN", "BGVAR"); ignored if stats is false

Returns an lsst.pipe.base.Struct containing:

- background -- full background model (initial model with changes), an lsst.afw.math.BackgroundList
 
fitBackground
-------------
Estimate the background of a masked image. 

Parameters:

- [in]	maskedImage	masked image whose background is to be computed
- [in]	nx	number of x bands; if 0 compute from width and config.binSize
- [in]	ny	number of y bands; if 0 compute from height and config.binSize
- [in]	algorithm	name of interpolation algorithm; if None use self.config.algorithm

Returns: fit background as an lsst.afw.math.Background

_addStats	
----------

Add statistics about the background to the exposure's metadata.

- @param[in,out] exposure --  exposure whose background was subtracted
- @param[in,out] background -- background model (an lsst.afw.math.BackgroundList)
- @param[in] statsKeys --  key names used to store the mean and variance of the background    in the exposure's metadata (a pair of strings); if None then use ("BGMEAN", "BGVAR");    ignored if stats is false
    
Examples
++++++++

This code is in subtractBackgroundExample.py in the examples directory of $MEAS_ALGORITHMS_DIR (detail on how to run on doxygen page).

Doesn't work on old stack:

..
      from lsst.meas.algorithms import SubtractBackgroundTask
      ImportError: cannot import name SubtractBackgroundTask

And on the new one, it requires afwdata.
      
      
What it returns
+++++++++++++++

