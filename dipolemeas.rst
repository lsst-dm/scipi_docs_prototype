
DipoleMeasurementTask
=======================

Measurement of Sources, specifically ones from difference images, for characterization as dipoles.

This class provides a default configuration for running Source measurement on image differences.

These plugins enabled by default allow the user to test the hypothesis that the Source is a dipole. This includes a set of measurements derived from intermediate base classes DipoleCentroidAlgorithm and DipoleFluxAlgorithm. Their respective algorithm control classes are defined in DipoleCentroidControl and DipoleFluxControl. Each centroid and flux measurement will have _neg (negative) and _pos (positive lobe) fields.

The first set of measurements uses a "naive" alrogithm for centroid and flux measurements, implemented in NaiveDipoleCentroidControl and NaiveDipoleFluxControl. The algorithm uses a naive 3x3 weighted moment around the nominal centroids of each peak in the Source Footprint. These algorithms fill the table fields ip_diffim_NaiveDipoleCentroid* and ip_diffim_NaiveDipoleFlux*

The second set of measurements undertakes a joint-Psf model on the negative and positive lobe simultaneously. This fit simultaneously solves for the negative and positive lobe centroids and fluxes using non-linear least squares minimization. The fields are stored in table elements ip_diffim_PsfDipoleFlux*.

Because this Task is just a config for SourceMeasurementTask, the same result may be acheived by manually editing the config and running SourceMeasurementTask.

How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d/–debug to import debug.py from your PYTHONPATH.

Specific functions of class
+++++++++++++++++++++++++++

Detailed descrip of primary functions in the class

Examples
++++++++

The example code is dipoleMeasTask.py in the examples directory of $IP_DIFFIM_DIR  (and the doxygen page gives a very detailed step-through of it).

What it returns
+++++++++++++++

[Not clear -- boolean for each obj..?]

measureTask.run(diaSources, exposure)

