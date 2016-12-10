
ForcedMeasurementTask
=============================


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1base_1_1forced_measurement_1_1_forced_measurement_task.html#ForcedMeasurementTask_


A subtask for measuring the properties of sources on a single exposure, using an existing "reference" catalog to constrain some aspects of the measurement. 

The task is configured with a list of "plugins": each plugin defines the values it measures (i.e. the columns in a table it will fill) and conducts that measurement on each detected source (see ForcedPlugin). The job of the measurement task is to initialize the set of plugins (which includes setting up the catalog schema) from their configuration, and then invoke each plugin on each source.

Most of the time, ForcedMeasurementTask will be used via one of the subclasses of ForcedPhotImageTask, ForcedPhotCcdTask and ForcedPhotCoaddTask [none of these have doxygen dox, yet]. These combine this measurement subtask with a "references" subtask (see BaseReferencesTask and CoaddSrcReferencesTask) to perform forced measurement using measurements performed on another image as the references. There is generally little reason to use ForcedMeasurementTask outside of one of these drivers, unless it is necessary to avoid using the Butler for I/O.

ForcedMeasurementTask has only three methods: init(), run(), and generateMeasCat().  For configuration options, see SingleFrameMeasurementConfig.

How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

Specific functions of class
+++++++++++++++++++++++++++

run
---

Perform forced measurement. 
 
generateMeasCat
---------------

Initialize an output SourceCatalog using information from the reference catalog. More...

This generates a new blank SourceRecord for each record in refCat. Note that this method does not attach any Footprints. Doing so is up to the caller (who may call attachedTransformedFootprints or define their own method - see run() for more information).

attachTransformedFootprints
---------------------------

The default implementation for attaching Footprints to blank sources prior to measurement.

Footprints for forced photometry must be in the pixel coordinate system of the image being measured, while the actual detections may start out in a different coordinate system. This default implementation transforms the Footprints from the reference catalog from the refWcs to the exposure's Wcs, which downgrades HeavyFootprints into regular Footprints, destroying deblend information.

Note that ForcedPhotImageTask delegates to this method in its own attachFootprints method. attachFootprints can then be overridden by its subclasses to define how their Footprints should be generated.

See the documentation for run() for information about the relationships between run(), generateMeasCat(), and attachTransformedFootprints().
	

Examples
++++++++

None given.

What it returns
+++++++++++++++

Returns: Source catalog ready for measurement


   
