1/4

MeasureMergedCoaddSourcesTask
============================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1multi_band_1_1_measure_merged_coadd_sources_task.html#MeasureMergedCoaddSourcesTask_

Deblend sources from master catalog in each coadd separately and measure. 

Command-line task that uses peaks and footprints from a master catalog to perform deblending and measurement in each coadd.

Given a master input catalog of sources (peaks and footprints), deblend and measure each source on the coadd. Repeating this procedure with the same master catalog across multiple coadds will generate a consistent set of child sources.

The deblender retains all peaks and deblends any missing peaks (dropouts in that band) as PSFs. Source properties are measured and the is-primary flag (indicating sources with no children) is set. Visit flags are propagated to the coadd sources.

Optionally, we can match the coadd sources to an external reference catalog.

How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files.

MeasureMergedCoaddSourcesTask has no debug variables of its own because it delegates all the work to the various sub-tasks.

Specific functions of class
+++++++++++++++++++++++++++


__init__
---------

Initialize the task.

Keyword arguments (in addition to those forwarded to CmdLineTask.__init__):

Parameters:
- [in]	schema:	the schema of the merged detection catalog used as input to this one
- [in]	peakSchema:	the schema of the PeakRecords in the Footprints in the merged detection catalog
- [in]	refObjLoader:	an instance of LoadReferenceObjectsTasks that supplies an external reference catalog. May be None if the loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
- [in]	butler:	a butler used to read the input schemas from disk or construct the reference catalog loader, if schema or peakSchema or refObjLoader is None


The task will set its own self.schema attribute to the schema of the output measurement catalog. This will include all fields from the input schema, as well as additional fields for all the measurements.
Initialize the task. More...
 

run
---------

Deblend and measure.

Parameters
- [in]	patchRef:	Patch reference.


Deblend each source in every coadd and measure. Set 'is-primary' and related flags. Propagate flags from individual visits. Optionally match the sources to a reference catalog and write the matches. Finally, write the deblended sources and measurements out.

 

readSources
---------

Read input sources.

Parameters:

- [in]	dataRef:	Data reference for catalog of merged detections

Returns a list of sources in merged catalog

We also need to add columns to hold the measurements we're about to make so we can measure in-place.

 
writeMatches
-------------

Write matches of the sources to the astrometric reference catalog.

We use the Wcs in the exposure to match sources.

Parameters:

- [in]	dataRef:	data reference
- [in]	exposure:	exposure with Wcs
- [in]	sources:	source catalog


 
write
---------

Write the source catalog.

Parameters:
- [in]	dataRef:	data reference
- [in]	sources:	source catalog


 

getExposureId
--------------

_makeArgumentParser
--------------------

Examples
++++++++

The whole example is simply spelled out in detail on the doxygen page.

What it returns
+++++++++++++++

