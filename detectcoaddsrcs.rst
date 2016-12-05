
DetectCoaddSourcesTask 
=========================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1multi_band_1_1_detect_coadd_sources_task.html#DetectCoaddSourcesTask_

Command-line task that detects sources on a coadd of exposures obtained with a single filter.

Coadding individual visits requires each exposure to be warped. This introduces covariance in the noise properties across pixels. Before detection, we correct the coadd variance by scaling the variance plane in the coadd to match the observed variance. This is an approximate approach – strictly, we should propagate the full covariance matrix – but it is simple and works well in practice.

After scaling the variance plane, we detect sources and generate footprints by delegating to the detection subtask.

DetectCoaddSourcesTask delegates most of its work to the detection subtask. You can retarget this subtask if you wish.



How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 


Specific functions of class
+++++++++++++++++++++++++++


__init__
----------

Initialize the task.

Create the detection subtask.

Keyword arguments (in addition to those forwarded to CmdLineTask.__init__):

Parameters:

- [in]	schema:	initial schema for the output catalog, modified-in place to include all fields set by this task. If None, the source minimal schema will be used.

- [in]	**kwargs:	keyword arguments to be passed to lsst.pipe.base.task.Task.__init__


run
----

Run detection on a coadd.

Invokes runDetection and then uses write to output the results.

Parameters:

- [in]	patchRef:	data reference for patch


 
runDetection
--------------

Run detection on an exposure.

First scale the variance plane to match the observed variance using scaleVariance. Then invoke the detection subtask to detect sources.

Parameters:
- [in]	exposure:	Exposure on which to detect
- [in]	idFactory:	IdFactory to set source identifiers

Returns a pipe.base.Struct with fields:

- sources: catalog of detections
- backgrounds: list of backgrounds

write
-----

Write out results from runDetection.

Parameters:
- [in]	exposure:	Exposure to write out
- [in]	results:	Struct returned from runDetection
- [in]	patchRef:	data reference for patch



_makeArgumentParser
---------------------
	
Examples
++++++++

The whole example is spelled out in some detail on the doxygen page, doing it as so::

   detectCoaddSources.py $CI_HSC_DIR/DATA --id patch=5,4 tract=0 filter=HSC-I --output curout

Some required syntax to make it work  even locally is missing right now, as cur output is::
   
  \: Config override file does not exist: '/Users/m/fizzAndAstro/lsst/lsstsw/obs_subaru/config/detectCoaddSources.py'
  \: Config override file does not exist: '/Users/m/fizzAndAstro/lsst/lsstsw/obs_subaru/config/hsc/detectCoaddSources.py'
  \: input=/Users/m/fizzAndAstro/lsst/lsstsw/ci_hsc/DATA
  \: calib=None
  \: output=/Users/m/fizzandastro/lsst/otherLSSTGithubPkgs/scipi_docs_prototype/exxampleCodes/curout
  CameraMapper: Loading registry registry from /Users/m/fizzandastro/lsst/otherLSSTGithubPkgs/scipi_docs_prototype/exxampleCodes/curout/_parent/registry.sqlite3
  CameraMapper: Loading calibRegistry registry from /Users/m/fizzAndAstro/lsst/lsstsw/ci_hsc/DATA/CALIB/calibRegistry.sqlite3
  CameraMapper: Loading registry registry from /Users/m/fizzandastro/lsst/otherLSSTGithubPkgs/scipi_docs_prototype/exxampleCodes/curout/_parent/registry.sqlite3
  CameraMapper: Loading calibRegistry registry from /Users/m/fizzAndAstro/lsst/lsstsw/ci_hsc/DATA/CALIB/calibRegistry.sqlite3
  WARNING: Not running the task because there is no data to process; you may preview data using "--show data"

 
  

What it returns
+++++++++++++++

