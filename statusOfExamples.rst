..
  _begin: top
   


Status of Examples from Doxygen Pages 
===================================


* On the doxygen docs pages, for this class:
  
- \- = No example 
- \+ = Has a standalone example 
- ++ = The example is not a separate code, but on the page
- ~ = Example is part of another primary example

Also, note: local = old (4/2016) stack build on my local machine,
curstack = current stack (generally trying this on tiger at
Princeton).

---------------------------------------------- `Processing CCDs`_

- `Functions that would be called to process single raw CCDs`_

- `Multiple CCD Image processing`_


---------------------------------------------- `Image processing`_

- `PSF matching and processing`_

- `Extracting sources`_

- `Functions to extract sources from a single processed CCD`_

-  `Functions to extract sources from a coadded exp`_
  
---------------------------------------------- `Post-catalog processing`_

- `Basic catalog functions`_

- `Properties of sources`_

- `Single exps`_

- `Coadded exp further processing`_

- `Star selectors`_  

- `Higher level, or unclear ones , for later`_
  
__________________________________________________________________

..
  - `top`_:
  top

   

Processing CCDs
----------------

Functions that would be called to process single raw CCDs
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- \++ ProcessCCD -- The one listed on the doxygen page works all the
way straight through on the old stack including all my print
statements.  Also, the orig version works on current stack.  However,
my print statements cause some curious problem with the version on the
current stack of the form "(ImportError: No module named
detectAndMeasure)".

- \+ IsrTask- Works totally fine locally, but on current stack::

    File "/tigress/HSC/LSST/stack_20160915/Linux64/ip_isr/12.1-3-gcf69c82+43/python/lsst/ip/isr/isrTask.py", line 464, in run
    raise RuntimeError("Must supply a linearizer if config.doBias True")
    RuntimeError: Must supply a linearizer if config.doBias True"


- ~ CharImg -- see calibTask, which also exercises charImg.
   
- \+ CalibTask --

  
Works totally fine locally (except for when the --display flag is turned on, which causes probs).  On current stack, it yields::


   ... File "/tigress/HSC/LSST/stack_20160915/Linux64/daf_persistence/12.1-15-gaf6b168/python/lsst/daf/persistence/posixStorage.py", line 280, in read
    raise RuntimeError("No such FITS catalog file: " + logLoc.locString())
   RuntimeError: No such FITS catalog file: /tigress/HSC/LSST/stack_20160915/Linux64/obs_test/12.1-9-g3e397f1+4/data/input/schema/icSrc.fits"
   
- ? SubtractBackgroundTask -- 
Doesn't work on old stack::


      from lsst.meas.algorithms import SubtractBackgroundTask
      ImportError: cannot import name SubtractBackgroundTask

And on the new one, it requires afwdata.


Multiple CCD Image processing
++++++++++++++++++++++++++++++

- \+ AssembleCcdTask -- This code is in runAssembleTask.py in the examples subdir (of $IP_ISR_DIR).

Works perfectly locally.  On curstack, it does::

    ...     ccd = next(assembleInput.values()).getDetector()
    TypeError: list object is not an iterator

see Jira tikt DM-8355.

- ~ SafeClipAssembleCoaddTask -- Complex example, needs to still be checked.
  
- \- SnapCombineTask -- None given.


---------------------------------------------------


Image processing
------------------ 

PSF matching and processing
+++++++++++++++++++++

- ++ InstallGaussianPsfTask --  I made a test code called 'installGaussian.exx.py', and it works perfectly both locally and on curstack, gives no output by default.
  
-  \+ ImagePsfMatchTask -- This code is imagePsfMatchTask.py in the examples directory of $IP_DIFFIM_DIR (described in detail on the doxygen page).  Works perfectly locally and on curstack, giving steady printing info to the screen as it goes.
   
- \+ ModelPsfMatchTask -- This code is modelPsfMatchTask.py in the examples directory of ipdiffim (described in detail on the doxygen page).  Works perfectly locally and on curstack, with a few lines of printout to screen.

- \+ SnapPsfMatchTask -- There is an example called snapPsfMatchTask.py in the examples directory of ipdiffim (described in detail on the doxygen page).  This prints a boatload of info to screen, and executes just fine, locally and on curstack.

- ~ PsfMatchTask -- As a base class, there is no example code for PsfMatchTask. However, see ImagePsfMatchTask, SnapPsfMatchTask, and ModelPsfMatchTask.


Extracting sources
++++++++++++++++


Functions to extract sources from a single processed CCD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ? SourceDetectionTask --

  This code is in measAlgTasks.py in the examples directory of  $MEAS_ALGORITHMS_DIR, and you run with just::

    examples/measAlgTasks.py --ds9

(There is much more described in the examples section on doxygen.)
    
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

  

 
Functions to extract sources from a coadded exp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- \+ DetectCoaddSourcesTask -- 

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

 
---------------------------------------------

Post-catalog processing
-----------------


Basic catalog functions
++++++++++++++++++++++++

- \+ AstrometryTask -- Run python photoCalTask.py from pipetasksdir.

Broken locally as so::

    Adding columns to the source catalogue
    astrometricSolver.refObjLoader: Loading reference objects using center (1023.5, 2305.5) pix = Fk5Coord(215.5935957, 53.0687594, 2000.00) sky and radius 0.133712386891 deg
    astrometricSolver.refObjLoader: Loaded 262 reference objects
    astrometricSolver.matcher: filterStars purged 0 reference stars, leaving 262 stars
    Traceback (most recent call last):
    File "photoCalTask.py", line 143, in <module>
    run()
    File "photoCalTask.py", line 114, in run
    matches = aTask.run(exposure, srcCat).matches
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/pipe_base/2016_01.0-7-gee41fc9+2/python/lsst/pipe/base/timer.py", line 118, in wrapper
    res = func(self, *args, **keyArgs)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/astrometry.py", line 198, in run
    res = self.solve(exposure=exposure, sourceCat=sourceCat)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/pipe_base/2016_01.0-7-gee41fc9+2/python/lsst/pipe/base/timer.py", line 118, in wrapper
    res = func(self, *args, **keyArgs)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/astrometry.py", line 312, in solve
    maxMatchDist = maxMatchDist,
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/pipe_base/2016_01.0-7-gee41fc9+2/python/lsst/pipe/base/timer.py", line 118, in wrapper
    res = func(self, *args, **keyArgs)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/astrometry.py", line 427, in _matchAndFitWcs
    maxMatchDist = maxMatchDist,
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/pipe_base/2016_01.0-7-gee41fc9+2/python/lsst/pipe/base/timer.py", line 118, in wrapper
    res = func(self, *args, **keyArgs)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/matchOptimisticB.py", line 294, in matchObjectsToSources
    usableSourceCat.extend(s for s in sourceCat if sourceInfo.isUsable(s))
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/afw/2.2016.10-10-gac5da67/python/lsst/afw/table/tableLib.py", line 9216, in extend
    for record in iterable:
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/matchOptimisticB.py", line 294, in <genexpr>
    usableSourceCat.extend(s for s in sourceCat if sourceInfo.isUsable(s))
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_astrom/2016_01.0-7-gb2f4996+3/python/lsst/meas/astrom/matchOptimisticB.py", line 152, in isUsable
    or (source.get(self.fluxKey)/source.get(self.fluxSigmaKey) > self.minSnr))
    ZeroDivisionError: float division by zero
    
Works fine on curstack as so::

  CameraMapper INFO: Unable to locate registry registry in root: /tigress/HSC/LSST/stack_20160915/Linux64/meas_astrom/12.1-3-gb143333+27/tests/data/sdssrefcat/registry.sqlite3
  CameraMapper INFO: Unable to locate registry registry in current dir: ./registry.sqlite3
  CameraMapper INFO: Loading Posix registry from /tigress/HSC/LSST/stack_20160915/Linux64/meas_astrom/12.1-3-gb143333+27/tests/data/sdssrefcat
  Adding columns to the source catalogue
  LoadIndexedReferenceObjectsTask INFO: Loading reference objects using center (1023.5, 2305.5) pix = Fk5Coord(215.5935957, 53.0687594, 2000.00) sky and radius 0.133712386891 deg
  LoadIndexedReferenceObjectsTask INFO: Loaded 566 reference objects
  astrometricSolver.matcher INFO: filterStars purged 0 reference stars, leaving 566 stars
  astrometricSolver.matcher INFO: Purged 0 unusable sources, leaving 337 usable sources
  astrometricSolver.matcher INFO: Matched 268 sources
  astrometricSolver.matcher INFO: filterStars purged 0 reference stars, leaving 566 stars
  astrometricSolver.matcher INFO: Purged 0 unusable sources, leaving 337 usable sources
  astrometricSolver.matcher INFO: Matched 247 sources
  astrometricSolver.matcher INFO: filterStars purged 0 reference stars, leaving 566 stars
  astrometricSolver.matcher INFO: Purged 0 unusable sources, leaving 337 usable sources
  astrometricSolver.matcher INFO: Matched 237 sources
  astrometricSolver INFO: Matched and fit WCS in 3 iterations; found 237 matches with scatter = 0.106 +- 0.073 arcsec
  photoCal INFO: Not applying color terms because config.applyColorTerms is False
  photoCal INFO: Magnitude zero point: 31.325627 +/- 0.000303 from 55 stars
  Used 57 calibration sources out of 237 matches
  RMS error is 0.062mmsg (robust 0.054, Calib says 0.000)
   

- \+ LoadAstrometryNetObjects --  Exercised by photoCalTask.py from pipetasksdir, see output for   AstrometryTask above.
  
- \+ FitTanSipWcsTask --   Exercised by photoCalTask.py from pipetasksdir, see output for   AstrometryTask above.



Properties of sources
+++++++++++++++++++


Single exps
~~~~~~~~~~~~

- \+ DipoleMeasurementTask -- Run: dipoleMeasTask.py in the examples directory of $IP_DIFFIM_DIR.

Fails locally with much output, ending in::

    .... dipoleMeasurement WARNING: Error in base_SkyCoord.measure on record 86: Wcs not attached to exposure.  Required for base_SkyCoord algorithm
    dipoleMeasurement WARNING: Error in base_SkyCoord.measure on record 87: Wcs not attached to exposure.  Required for base_SkyCoord algorithm
    Traceback (most recent call last):
    File "dipoleMeasTask.py", line 126, in <module>
    run(args)
    File "dipoleMeasTask.py", line 100, in run
    measureTask.measure(exposure, diaSources)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/meas_base/2016_01.0-16-g36ec2c5/python/lsst/meas/base/sfm.py", line 360, in measure
    self.run(measCat, exposure)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/ip_diffim/2016_01.0-4-g34b2cfc/python/lsst/ip/diffim/dipoleMeasurement.py", line 337, in run
    self.classify(sources)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/pipe_base/2016_01.0-7-gee41fc9+2/python/lsst/pipe/base/timer.py", line 118, in wrapper
    res = func(self, *args, **keyArgs)
    File "/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/ip_diffim/2016_01.0-4-g34b2cfc/python/lsst/ip/diffim/dipoleMeasurement.py", line 303, in classify
    self.log.log(self.log.INFO, "Classifying %d sources" % len(sources))
    TypeError: object of type 'ExposureF' has no len()


Curstack, after repointing afwdata, fails as so::

  sourceDetection INFO: Detected 29 positive sources to 3 sigma.
  sourceDetection.background WARN: Too few points in grid to constrain fit: min(nx, ny) < approxOrder) [min(3, 3) < 6]
  sourceDetection.background WARN: Reducing approxOrder to 2
  sourceDetection INFO: Resubtracting the background after object detection
  sourceDetection INFO: Detected 31 negative sources to 3 sigma
  Merged 60 Sources into 29 diaSources (from 29 +ve, 31 -ve)
  dipoleMeasurement INFO: Measuring 29 sources (29 parents, 0 children) 
  dipoleMeasurement WARN: Error in ip_diffim_PsfDipoleFlux.measure on record 72: 
  File "src/image/Image.cc", line 91, in static lsst::afw::image::ImageBase<PixelT>::_view_t lsst::afw::image::ImageBase<PixelT>::_makeSubView(const Extent2I&, const Extent2I&, const _view_t&) [with PixelT = double; lsst::afw::image::ImageBase<PixelT>::_view_t = boost::gil::image_view<boost::gil::memory_based_2d_locator<boost::gil::memory_based_step_iterator<boost::gil::pixel<double, boost::gil::layout<boost::mpl::vector1<boost::gil::gray_color_t> > >*> > >; lsst::afw::geom::Extent2I = lsst::afw::geom::Extent<int, 2>]
    Box2I(Point2I(20,19),Extent2I(74,2)) doesn't fit in image 21x21 {0}
    lsst::pex::exceptions::LengthError: 'Box2I(Point2I(20,19),Extent2I(74,2)) doesn't fit in image 21x21'

    dipoleMeasurement WARN: Error in ip_diffim_PsfDipoleFlux.measure on record 79: 
  File "src/image/Image.cc", line 91, in static lsst::afw::image::ImageBase<PixelT>::_view_t lsst::afw::image::ImageBase<PixelT>::_makeSubView(const Extent2I&, const Extent2I&, const _view_t&) [with PixelT = double; lsst::afw::image::ImageBase<PixelT>::_view_t = boost::gil::image_view<boost::gil::memory_based_2d_locator<boost::gil::memory_based_step_iterator<boost::gil::pixel<double, boost::gil::layout<boost::mpl::vector1<boost::gil::gray_color_t> > >*> > >; lsst::afw::geom::Extent2I = lsst::afw::geom::Extent<int, 2>]
    Box2I(Point2I(-131,-523),Extent2I(132,524)) doesn't fit in image 21x21 {0}
    lsst::pex::exceptions::LengthError: 'Box2I(Point2I(-131,-523),Extent2I(132,524)) doesn't fit in image 21x21'

- ++ ExampleCmdLineTask -- From pipetasks examples dir, do::

    ./exampleCmdLineTask.py $OBS_TEST_DIR/data/input --id --output cur_exxCLTaskOut

Works fine locally, with fits files you can display in the output dir, and also screen output::

  ./exampleCmdLineTask.py $OBS_TEST_DIR/data/input --id --output cur_exxCLTaskOut
  \: Config override file does not exist: '/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/obs_test/2016_01.0-3-gafa6dd0+7/config/exampleTask.py'
  \: Config override file does not exist: '/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/obs_test/2016_01.0-3-gafa6dd0+7/config/test/exampleTask.py'
  : input=/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/obs_test/2016_01.0-3-gafa6dd0+7/data/input
  : calib=None
  : output=/Users/m/fizzandastro/lsst/lsstsw/stack/DarwinX86/pipe_tasks/2016_01.0-35-g183e2ce/examples/cur_exxCLTaskOut
  CameraMapper: Loading registry registry from /Users/m/fizzandastro/lsst/lsstsw/stack/DarwinX86/pipe_tasks/2016_01.0-35-g183e2ce/examples/cur_exxCLTaskOut/_parent/registry.sqlite3
  CameraMapper: Loading registry registry from /Users/m/fizzandastro/lsst/lsstsw/stack/DarwinX86/pipe_tasks/2016_01.0-35-g183e2ce/examples/cur_exxCLTaskOut/_parent/registry.sqlite3
  exampleTask: Processing data ID {'filter': 'g', 'visit': 1}
  exampleTask.stats: clipped mean=1184.70; meanErr=0.02; stdDev=33.64; stdDevErr=1.04

  
Works fine also on curstack, with fits files you can display in the output dir, and also screen output::

  root INFO: Running: ./exampleCmdLineTask.py /tigress/HSC/LSST/stack_20160915/Linux64/obs_test/12.1-9-g3e397f1+6/data/input --id --output cur_exxCLTaskOut
  exampleTask INFO: Processing data ID {'filter': 'g', 'visit': 1}
  exampleTask.stats INFO: clipped mean=1184.70; meanErr=0.02; stdDev=33.64; stdDevErr=1.04
  exampleTask INFO: Processing data ID {'filter': 'g', 'visit': 2}
  exampleTask.stats INFO: clipped mean=1228.79; meanErr=0.02; stdDev=34.19; stdDevErr=nan
  exampleTask INFO: Processing data ID {'filter': 'r', 'visit': 3}
  exampleTask.stats INFO: clipped mean=1433.76; meanErr=0.03; stdDev=37.36; stdDevErr=0.93

    

- ++ExampleSimpleStatsTask -- From pipetasks examples dir, do::

    ./exampleStatsTask.py 

Works fine locally, with screen output::

  computing statistics on '/Users/m/fizzAndAstro/lsst/lsstsw/stack/DarwinX86/afwdata/2.2016.10/data/med.fits'

  running ExampleSimpleStatsTask
  exampleSimpleStats: simple mean=2846.29; meanErr=2.57; stdDev=1521.14; stdDevErr=nan
  result  = Struct(meanErr=2.571202746482615; stdDevErr=nan; stdDev=1521.1440586716005; mean=2846.2888800000915)

  running ExampleSigmaClippedStatsTask
  exampleSigmaClippedStats: clipped mean=2811.17; meanErr=0.08; stdDev=45.22; stdDevErr=nan
  result  = Struct(meanErr=0.07771313326235756; stdDevErr=nan; stdDev=45.217358373691106; mean=2811.1677216591843)

Curstack -- my repointing afwdata trick isn't working..?

- ++ ExampleSigmaClippedStatsTask -- Exercised by above exampleStatsTask.py

- ForcedMeasurementTask -- None
  
+ SingleFrameMeasurementTask -- Run runSingleFrameTask.py in measbase/examples, locally output is many lines, and::

    .... sourceDetection: Detected 23 positive sources to 3 sigma.
    sourceDetection: Resubtracting the background after object detection
    sourceDetection: Detected 6 negative sources to 3 sigma
    Found 29 sources (23 +ve, 6 -ve)
    measurement: Measuring 29 sources (29 parents, 0 children) 

    
Curstack -- probs::

  Traceback (most recent call last):
  File "runSingleFrameTask.py", line 30, in <module>
    from lsst.utils import getProductDir
    ImportError: cannot import name getProductDir


Coadded exp further processing
++++++++++++++++++++++++++++++++

- ++ MeasureMergedCoaddSourcesTask -- From pipetasks/bin, need to run measureCoaddSources.py with some flags, as on dox pages.


- ++ MergeDetectionsTask -- Also, from pipetasks/bin, need to run mergeCoaddDetections.py with some flags, as on dox pages.


- ++ PropagateVisitFlagsTask -- My little extracted propflagsexx in the exxamples dir doesn't work.








Star selectors
+++++++++++++++

- DiaCatalogSourceSelectorTask -- 
- ObjectSizeStarSelectorTask -- 
- SecondMomentStarSelectorTask -- 



.. begin_:
   
