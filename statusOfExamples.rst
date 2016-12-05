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

- \+ AstrometryTask -- 
- \+ LoadAstrometryNetObjects -- 
- \+ FitTanSipWcsTask -- 



Properties of sources
+++++++++++++++++++


Single exps
~~~~~~~~~~~~

- \+ DipoleMeasurementTask -- 


- ++ ExampleCmdLineTask -- 


- ++ExampleSimpleStatsTask -- 


- ++ ExampleSigmaClippedStatsTask -- 


- ForcedMeasurementTask --
  
+ SingleFrameMeasurementTask -- 







Coadded exp further processing
++++++++++++++++++++++++++++++++

- ++ MeasureMergedCoaddSourcesTask -- 


- ++ MergeDetectionsTask -- 


- ++ PropagateVisitFlagsTask -- 








Star selectors
+++++++++++++++

- DiaCatalogSourceSelectorTask -- 
- ObjectSizeStarSelectorTask -- 
- SecondMomentStarSelectorTask -- 



.. begin_:
   
