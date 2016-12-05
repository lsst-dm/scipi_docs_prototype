
1/4


SourceDetectionTask
===================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1algorithms_1_1detection_1_1_source_detection_task.html#SourceDetectionTask_

Detect positive and negative sources on an exposure and return a new table.SourceCatalog.

How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files.

The available variables in SourceDetectionTask are:

- display
  - If True, display the exposure on ds9's frame 0. +ve detections in blue, -ve detections in cyan
  - If display > 1, display the convolved exposure on frame 1


Specific functions of class
+++++++++++++++++++++++++++

__init__
---------
Create the detection task. 
 
Most arguments are simply passed onto pipe.base.Task.

Parameters:

- schema -- An lsst::afw::table::Schema used to create the output lsst.afw.table.SourceCatalog
  
- **kwds --	Keyword arguments passed to lsst.pipe.base.task.Task.__init__.
If schema is not None, a 'flags.negative' field will be added to label detections made with a negative threshold.

Note:

This task can add fields to the schema, so any code calling this task must ensure that these columns are indeed present in the input match list;

run
---

Run source detection and create a SourceCatalog.

Parameters:
- table --	lsst.afw.table.SourceTable object that will be used to create the SourceCatalog.
- exposure --	Exposure to process; DETECTED mask plane will be set in-place.
- doSmooth --	if True, smooth the image before detection using a Gaussian of width sigma (default: True)
- sigma --	sigma of PSF (pixels); used for smoothing and to grow detections; if None then measure the sigma of the PSF of the exposure (default: None)
- clearMask --	Clear DETECTED{,_NEGATIVE} planes before running detection (default: True)
  
Returns a lsst.pipe.base.Struct with:

- sources – an lsst.afw.table.SourceCatalog object
- fpSets — lsst.pipe.base.Struct returned by detectFootprints


 

detectFootprints
----------------

Detect footprints.

Parameters:

- exposure --	Exposure to process; DETECTED{,_NEGATIVE} mask plane will be set in-place.
- doSmooth --	if True, smooth the image before detection using a Gaussian of width sigma
- sigma --	sigma of PSF (pixels); used for smoothing and to grow detections; if None then measure the sigma of the PSF of the exposure
- clearMask --	Clear both DETECTED and DETECTED_NEGATIVE planes before running detection
  
Returns a lsst.pipe.base.Struct with fields:

- positive: lsst.afw.detection.FootprintSet with positive polarity footprints (may be None)
- negative: lsst.afw.detection.FootprintSet with negative polarity footprints (may be None)
- numPos: number of footprints in positive or 0 if detection polarity was negative
- numNeg: number of footprints in negative or 0 if detection polarity was positive
- background: re-estimated background. None if reEstimateBackground==False


 
thresholdImage
--------------

Threshold the convolved image, returning a FootprintSet.

Helper function for detect().

Parameters:

- image	-- The (optionally convolved) MaskedImage to threshold
- thresholdParity --	Parity of threshold
- maskName --	Name of mask to set

Returns FootprintSet

setEdgeBits
-----------

Set the edgeBitmask bits for all of maskedImage outside goodBBox.

Parameters:

- [in,out] --	maskedImage	image on which to set edge bits in the mask
- [in]	goodBBox -- 	bounding box of good pixels, in LOCAL coordinates
- [in]	edgeBitmask --	bit mask to OR with the existing mask bits in the region outside goodBBox


Examples
++++++++

This code is in measAlgTasks.py in the examples directory of  $MEAS_ALGORITHMS_DIR (detail on how to run on doxygen page).

Locally, fails with::

  Traceback (most recent call last):
  File "./examples/measAlgTasks.py", line 123, in <module>
    run(display=args.ds9)
  File "./examples/measAlgTasks.py", line 82, in run
    tab = afwTable.SourceTable.make(schema)
  File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/afw/2.2016.10-10-gac5da67/python/lsst/afw/table/tableLib.py", line 8704, in make
    return _tableLib.SourceTable_make(*args)
    lsst.pex.exceptions.wrappers.NotFoundError: 
  File "src/table/Schema.cc", line 239, in SchemaItem<T> lsst::afw::table::detail::SchemaImpl::find(const std::string &) const [T = double]
    Field or subfield withname 'base_CircularApertureFlux_3_0_flux' not found with type 'D'. {0}
    lsst::pex::exceptions::NotFoundError: 'Field or subfield withname 'base_CircularApertureFlux_3_0_flux' not found with type 'D'.'

On curstack, can't yet run, requires afwdata.

  


What it returns
+++++++++++++++

