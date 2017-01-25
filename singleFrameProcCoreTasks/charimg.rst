
#####################
CharacterizeImageTask
#####################

Given an exposure with defects repaired (masked and interpolated over,
e.g. as output by :doc:`IsrTask <isrtask>`), this task does initial
source extraction and PSF estimation.


Its primary functions are to:

  - Detect and measure bright sources

  - Repair cosmic rays

  - Measure and subtract background

  - Measure the PSF


This task is implemented in the ``lsst.pipe.tasks`` module.

.. seealso::
   
    This task is most commonly called by :doc:`ProcessCcd <processccd>`.
    
Configuration
=============


Retargetable Subtasks
---------------------

.. csv-table:: 
   :header: Task, Default, Description
   :widths: 15, 25, 50

	``background``,  SubtractBackgroundTask,    Configuration for initial background estimation
	``detection``,  SourceDetectionTask, Detect sources
	``deblend``,  SourceDeblendTask, Split blended source into their components
	``measurement``,  SingleFrameMeasurementTask, Measure sources
	``measureApCorr``,   MeasureApCorrTask, Subtask to measure aperture corrections
	``applyApCorr``,  ApplyApCorrTask, Subtask to apply aperture corrections
	``catalogCalculation``,  CatalogCalculationTask, Subtask to run catalogCalculation plugins on catalog
	``installSimplePsf``,   InstallGaussianPsfTask, Install a simple PSF model
	``refObjLoader``,   LoadAstrometryNetObjectsTask, Reference object loader
	``astrometry``,  AstrometryTask, Task to load and match reference objects. Only used if `measurePsf` can use matches. Warning: matching will only work well if the initial WCS is accurate enough to give good matches (roughly: good to 3 arcsec across the CCD).
	``measurePsf``,  MeasurePsfTask, Measure PSF
	``repair``,   RepairTask, Remove cosmic rays
 


Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

   ``doDeblend``, (`bool`),  `True`, Run deblender on input exposure?
   ``doApCorr``, (`bool`),  `True`,  Run subtasks to measure and apply aperture corrections
   ``doMeasurePsf``, (`bool`),  `True`, Measure the PSF? If `False` then keep the existing PSF model (which must exist) and use that model for all operations."
   ``doWrite``, (`bool`),  `True`, Persist results?
   ``doWriteExposure``, (`bool`),  `True`, Write icExp and icExpBackground in addition to icSrc? Ignored if doWrite False.
   ``useSimplePsf``, (`bool`),  `True`, Replace the existing PSF model with a simplified version that has the same sigma at the start of each PSF determination iteration? Doing so makes PSF determination converge more robustly and quickly.
   ``psfIterations``, (`int`),  2; min=1,    Number of iterations of doing: detect sources; measure sources; estimate PSF. If `useSimplePsf`=`True` then 2 should be plenty; otherwise more may be wanted.
   ``checkUnitsParseStrict``,  (`str`), `raise`, Strictness of Astropy unit compatibility check.  Can be 'raise'; 'warn'; 'silent'

Entrypoint
==========

- ``lsst.pipe.tasks.characterizeImage.CharacterizeImageTask.run`` 

If you want this task to unpersist inputs or persist outputs, then call the ``run`` method (which is a thin wrapper around the ``characterize`` method).

If you already have the inputs unpersisted and do not want to persist the output then it is more direct to call the ``characterize`` method directly.



Butler Inputs
=============

A butler object is passed to the `refObjLoader` constructor in case it
is needed to load catalogs. It may be `None` if a catalog-based star
selector is not used, if the reference object loader constructor does
not require a butler, or if a reference object loader is passed
directly via the `refObjLoader` argument.

Butler Outputs
==============

Output catalogs are of type ``icSrc``.

Examples
========

This code is in ``calibrateTask.py`` (which calls ``CharacterizeImageTask`` before calling ``CalibrateTask``) in the ``$PIPE_TASKS/examples`` directory, and can be run as, e.g.::

     python examples/calibrateTask.py,-display

Running this example currently requires that over and above the DM Stack installation, ``afwdata`` is installed and set up (via the EUPS ``setup`` command).

Debugging
=========

- frame = (`int`) - if specified, the frame of first debug image displayed (defaults to 1)

- repair_iter - (`bool`) -  if `True` display image after each repair in the measure PSF loop

- background_iter - (`bool`) -  if `True` display image after each background subtraction in the measure PSF loop

- measure_iter - (`bool`) -  if `True` display image and sources at the end of each iteration of the measure PSF loop See lsst.meas.astrom.displayAstrometry for the meaning of the various symbols.

- psf - (`bool`) -  if `True` display image and sources after PSF is measured; this will be identical to the final image displayed by measure_iter if measure_iter is true

- repair - (`bool`) -  if `True` display image and sources after final repair

- measure - (`bool`) -  if `True` display image and sources after final measurement



Algorithm details
====================

