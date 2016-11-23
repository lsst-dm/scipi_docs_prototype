
AstrometryTask
==============

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1astrom_1_1astrometry_1_1_astrometry_task.html#AstrometryTask_

The essential function for this task is to match an input sourceCat
with a reference catalog and solve for the WCS across the field.

There are three steps, each performed by different subtasks:

- Find position reference stars that overlap the exposure

- Match sourceCat to position reference stars
  
- Fit a WCS based on the matches

      [ Prob with \ref to the example in the body of the code?]
      
How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py
from your PYTHONPATH; see Using lsstDebug to control debugging output
for more about debug.py files.

The available variables in AstrometryTask are:

- display (bool) -- If True display information at three stages: after finding reference objects, after matching sources to reference objects, and after fitting the WCS; defaults to False

- frame (int) -- whether to use a ds9 frame to display the reference objects; the next two frames are used to display the match list and the results of the final WCS; defaults to 0

Specific functions of class
+++++++++++++++++++++++++++

Primary functions in the class:

computeMatchStatsOnSky
----------------------

This computes on-sky radial distance statistics for a match list.

It takes in a matchList: a list of matches between reference object
and sources; the distance field is the only field read for each
matched object and it must be set to distance in radians.

Returns a normal pipe_base Struct containing these fields:

- distMean  -- clipped mean of on-sky radial separation

- distStdDev  -- clipped standard deviation of on-sky radial separation

- maxMatchDist  -- distMean + self.config.matchDistanceSigma*distStdDev


getExposureMetadata
---------------------

This extracts metadata from an exposure.

It returns a normal *lsst.pipe.base.Struct* containing the following exposure metadata:

- bbox -- parent bounding box

- wcs -- WCS (an *lsst.afw.image.Wcs*)

- calib -- calibration (an *lsst.afw.image.Calib*), or None if unknown

- filterName -- name of filter used for this exposure, or None if unknown


matchAndFitWcs
--------------

This function matches sources to reference objects and fits a WCS.

Input parameters:

- 	refCat --	catalog of reference objects

-	sourceCat --	catalog of sources detected on the exposure (an *lsst.afw.table.SourceCatalog*)

-	refFluxField --	which field of refCat to use for flux

-	bbox	-- bounding box of exposure (an *lsst.afw.geom.Box2I*)

-	wcs	-- initial guess for WCS of exposure (an *lsst.afw.image.Wcs*)

-	maxMatchDist	-- maximum on-sky distance between reference objects and sources (an *lsst.afw.geom.Angle*); if None then use the matcher's default

-	exposure	-- exposure whose WCS is to be fit, or None; used only for the debug display


Returns: an *lsst.pipe.base.Struct* with these fields:

- matches -- list of reference object/source matches (an *lsst.afw.table.ReferenceMatchVector*)

- wcs -- the fit WCS (an *lsst.afw.image.Wcs*)

- scatterOnSky -- median on-sky separation between reference objects and sources in "matches" (an *lsst.afw.geom.Angle*)


loadAndMatch
------------

Load reference objects overlapping an exposure and match to sources detected on that exposure.

Input Parameters:

- 	exposure --	exposure that the sources overlap

-	sourceCat --	catalog of sources detected on the exposure (an *lsst.afw.table.SourceCatalog*)

Returns an *lsst.pipe.base.Struct* with these fields:

- refCat -- reference object catalog of objects that overlap the exposure (with some margin) (an *lsst::afw::table::SimpleCatalog*)

- matches -- list of reference object/source matches (an *lsst.afw.table.ReferenceMatchVector*)
  
- matchMeta -- metadata needed to unpersist matches (an *lsst.daf.base.PropertyList*)

solve
-----

Loads reference objects overlapping an exposure, matches to sources and fits a WCS.

Returns an *lsst.pipe.base.Struct* with these fields:

- refCat -- reference object catalog of objects that overlap the exposure (with some margin) (an *lsst::afw::table::SimpleCatalog*)

- matches -- list of reference object/source matches (an *lsst.afw.table.ReferenceMatchVector*)

- scatterOnSky -- median on-sky separation between reference objects and sources in "matches" (an *lsst.afw.geom.Angle*)

- matchMeta -- metadata needed to unpersist matches (an *lsst.daf.base.PropertyList*)



Examples
++++++++

photoCalTask.py in $PIPE_TASKS_DIR
