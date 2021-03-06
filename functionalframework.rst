..
  _begin: top
   


Functional Framework
========================


* On the doxygen docs pages, for this class:
  
- \- = No example 
- \+ = Has a standalone example 
- ++ = The example is not a separate code, but on the page
- ~ = Example is part of another primary example



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

- \++ ProcessCCD_ -- Does the  actual steps of how an image is processed from raw data to a science-grade image that can be used in analyses.  Calls the 3 main tasks below.

.. _ProcessCCD: processccd.html

- \+ IsrTask_ - Instrumental Signature Removal (ISR) is a sequence of steps taken to ‘clean’ images of various aspects of defects that any system of optics and detectors will imprint on an image by default. 

.. _IsrTask: isrtask.html
   
- ~ CharImg_ -- Detect and measure bright sources on an exp, repair cosmic rays, measure and subtract background, measure the PSF

.. _CharImg: charimg.html
  
- \+ CalibTask_ -- Run detectAndMeasure subtask on an exp to peform deep detection and measurement, run astrometry subtask to fit an improved WCS, and run photoCal subtask to fit the exposure’s photometric zero-point

.. _CalibTask: calibimg.html

- ? SubtractBackgroundTask -- Fit a model of the background of an exposure and subtract it.





Multiple CCD Image processing
++++++++++++++++++++++++++++++

- \+ AssembleCcdTask_ -- This task assembles sections of an image into a larger mosaic. The sub-sections are typically amplifier sections and are to be assembled into a detector size pixel grid. 

.. _AssembleCcdTask: assembleccd.html

- ~ :doc:`SafeClipAssembleCoaddTask <safeclipassemble>` -- Assemble a coadded image from a set of coadded temporary exposures, being careful to clip & flag areas with potential artifacts.


- \- :doc:`SnapCombineTask <snapcombine>` -- Combine snaps


---------------------------------------------------


Image processing
----------------- 



PSF matching and processing
+++++++++++++++++++++

- ++ :doc:`InstallGaussianPsfTask <installgaussianpsf>` -- Install a Gaussian PSF model in an exposure.


-  \+ :doc:`ImagePsfMatchTask <imagepsfmatch>` -- Psf-match two MaskedImages or Exposures using the sources in the images.




- \+ :doc:`ModelPsfMatchTask <modelpsfmatch>` -- Matching of two model Psfs, and application of the Psf-matching kernel to an input Exposure


- ~ :doc:`PsfMatchTask <psfmatch>` -- Base class for Psf Matching; should not be called directly.


- \+ :doc:`SnapPsfMatchTask <snappsfmatch>` -- This Task differs from ImagePsfMatchTask in that it matches two Exposures assuming that the images have been acquired very closely in time. 


Extracting sources
++++++++++++++++


Functions to extract sources from a single processed CCD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- ? SourceDetectionTask --  Detect positive and negative sources on an exposure and return a new table.SourceCatalog.

 
Functions to extract sources from a coadded exp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- \+ DetectCoaddSourcesTask -- Command-line task that detects sources on a coadd of exposures obtained with a single filter.


---------------------------------------------

Post-catalog processing
-----------------


Basic catalog functions
++++++++++++++++++++++++

- \+ AstrometryTask -- The essential function for this task is to match an input sourceCat with a reference catalog and solve for the WCS across the field.
- \+ LoadAstrometryNetObjects -- Load reference objects from astrometry.net index files.
- \+ FitTanSipWcsTask -- Fit a TAN-SIP WCS given a list of reference object/source matches.



Properties of sources
+++++++++++++++++++


Single exps
~~~~~~~~~~~~

- \+ DipoleMeasurementTask -- Measurement of Sources, specifically ones from difference images, for characterization as dipoles.


- ++ ExampleCmdLineTask -- Example command-line task that computes simple statistics on an image.


- ++ExampleSimpleStatsTask -- Example task to compute mean and standard deviation of an image.  This was designed to be run as a subtask by ExampleCmdLineTask. It is about as simple as a task can be; it has no configuration parameters and requires no special initialization.


- ++ ExampleSigmaClippedStatsTask -- Example task to compute sigma-clipped mean and standard deviation of an image. This is a simple example task designed to be run as a subtask by ExampleCmdLineTask (but a bit more complex than ExampleSimpleStatsTask)


- ForcedMeasurementTask -- A subtask for measuring the properties of sources on a single exposure, using an existing “reference” catalog to constrain some aspects of the measurement.
+ SingleFrameMeasurementTask -- A subtask for measuring the properties of sources on a single exposure.







Coadded exp further processing
++++++++++++++++++++++++++++++++

- ++ MeasureMergedCoaddSourcesTask -- Deblend sources from master catalog in each coadd separately and measure.


- ++ MergeDetectionsTask -- Merge coadd detections from multiple bands.


- ++ PropagateVisitFlagsTask -- Task to propagate flags from single-frame measurements to coadd measurements.








Star selectors
+++++++++++++++

- DiaCatalogSourceSelectorTask -- A naive star selector based on second moments. 
- ObjectSizeStarSelectorTask -- A star selector that looks for a cluster of small objects in a size-magnitude plot.
- SecondMomentStarSelectorTask -- A star selector based on second moments.



Higher level, or unclear ones , for later
-----------------------------------------


- \- CoaddSourceTransformTask --Transform measuremenents made on coadds to calibrated form. This is a specialization of RunTransformTaskBase which operates on measurements made on coadds. Refer to the parent documentation for details.


- \- DecorrelateALKernelTask -- Decorrelate the effect of convolution by Alard-Lupton matching kernel in image difference.


- \-  ForcedSourceTransformTask -- Transform forced_source measuremenents to calibrated form.


- \- LoadReferenceObjectsTask -- Abstract base class for tasks that load objects from a reference catalog in a particular region of the sky.


- \- MeasureApCorrTask -- Task to measure aperture correction.


- ++ReadFitsCatalogTask --  Read an object catalog from a FITS table. Designed to read foreign catalogs so they can be written out in a form suitable for IngestIndexedReferenceTask.


- ++ ReadTextCatalogTask --Read an object catalog from a text file.

-  \- SourceTransformTask -- Transform source measuremenents to calibrated form.


- \- TransformTask -- Transform a SourceCatalog containing raw measurements to calibrated form.


.. begin_:
   
