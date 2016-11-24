
SingleFrameMeasurementTask
===========================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1base_1_1sfm_1_1_single_frame_measurement_task.html#SingleFrameMeasurementTask_

A subtask for measuring the properties of sources on a single exposure.

The task is configured with a list of "plugins": each plugin defines
the values it measures (i.e. the columns in a table it will fill) and
conducts that measurement on each detected source (see
SingleFramePlugin). The job of the measurement task is to initialize
the set of plugins (which includes setting up the catalog schema) from
their configuration, and then invoke each plugin on each source.

When run after the deblender, SingleFrameMeasurementTask also replaces
each source's neighbors with noise before measuring each source,
utilizing the HeavyFootprints created by the deblender (see
NoiseReplacer).

SingleFrameMeasurementTask has only two methods: init() and run(). For
configuration options, see SingleFrameMeasurementConfig.


How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

Specific functions of class
+++++++++++++++++++++++++++

initializePlugin
----------------

Sets up undeblended plugins in addition to regular plugins.

The parent class will set up the regular plugins; we just set up the undeblended plugins.

Keyword arguments are forwarded directly to plugin constructors,
allowing derived classes to use plugins with different signatures.


Examples
++++++++

See:  examples/runSingleFrameTask.py  (well-documented).

What it returns
+++++++++++++++

measCat: a *lsst.afw.table.SourceCatalog* to be filled with outputs. Must contain all the SourceRecords to be measured (with Footprints attached), and have a schema that is a superset of self.schema.
