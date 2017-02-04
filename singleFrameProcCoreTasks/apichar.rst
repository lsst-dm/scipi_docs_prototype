:orphan: true

.. _top:

.. py:module:: randname

.. py:class:: lsst.pipe.tasks.characterizeImage.CharacterizeImageTask

  .. py:method:: characterize()
		 
.. code-block:: python
		
  characterize(exposure,
               exposureIdInfo = None,
	       background = None )

Characterize a science image.

Performs the following operations:

- Iterate the following `config.psfIterations` times, or once if `config.doMeasurePsf= False`:

		- Detect and measure sources and estimate PSF (see :ref:`detectMeasureAndEstimatePsf <detlink>` for details)

- Interpolate over cosmic rays

- Perform final measurement


Parameters
----------

-	`exposure`	- exposure to characterize (an `lsst.afw.image.ExposureF` or similar). The following changes are made:

	- update or set psf
	- set apCorrMap
	- update detection and cosmic ray mask planes
	- subtract background and interpolate over cosmic rays

-	`exposureIdInfo` -	ID info for exposure (an `lsst.obs.base.ExposureIdInfo`). If not provided, returned `SourceCatalog` IDs will not be globally unique.

-	`background` -	initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList`). May be `None` if no background has been subtracted, which is typical for image characterization.

Returns
-------

pipe_base Struct containing these fields, all from the final iteration of :ref:`detectMeasureAndEstimatePsf <detlink>`:

  - `exposure`: characterized exposure; image is repaired by interpolating over cosmic rays, mask is updated accordingly, and the PSF model is set

  - `sourceCat`: detected sources (an `lsst.afw.table.SourceCatalog`)

  - `background`: model of background subtracted from exposure (an `lsst.afw.math.BackgroundList`)

  - `psfCellSet`: spatial cells of PSF candidates (an `lsst.afw.math.SpatialCellSet`)


  .. py:method:: detectMeasureAndEstimatePsf()
	       
.. code-block:: python
		
  detectMeasureAndEstimatePsf(exposure,
		              exposureIdInfo,
 			      background )
	
Perform one iteration of detect, measure and estimate PSF.

Performs the following operations:

If `config.doMeasurePsf` or `not exposure.hasPsf()`:

- Install a simple PSF model (replacing the existing one, if need be)

- Interpolate over cosmic rays with `keepCRs=True`
- Estimate background and subtract it from the exposure
- Detect, deblend and measure sources, and subtract a refined background model;
- If `config.doMeasurePsf`: measure PSF

Parameters
----------

-	`exposure` -	exposure to characterize (an lsst.afw.image.ExposureF or similar) The following changes are made:

	- Update or set psf
	- Update detection and cosmic ray mask planes
	- Subtract background

-	`exposureIdInfo` -	ID info for exposure (an lsst.obs_base.ExposureIdInfo)

-	`background` -	initial model of background already subtracted from exposure (an `lsst.afw.math.BackgroundList`).


Returns
-------

pipe_base Struct containing these fields, all from the final iteration of detect sources, measure sources and estimate PSF:

  - `exposure` -  characterized exposure; image is repaired by interpolating over cosmic rays, mask is updated accordingly, and the PSF model is set
  - `sourceCat` - detected sources (an lsst.afw.table.SourceCatalog)
  - `background` - model of background subtracted from exposure (an lsst.afw.math.BackgroundList)
  - `psfCellSet` - spatial cells of PSF candidates (an lsst.afw.math.SpatialCellSet)


  .. py:method:: getSchemaCatalogs()
		     
.. code-block:: python
		
 getSchemaCatalogs()

No parameters.

Returns
-------

Return a dictionary of empty catalogs for each catalog dataset
produced by this task.


  .. py:method:: display()

.. code-block:: python
		
 display(itemName,
 	 exposure,
 	 sourceCat = None)

Display exposure and sources on next frame, if display of `itemName` has been requested

Parameters
----------

- `itemName`-  name of item in `debugInfo`
- `exposure`-  exposure to display
- `sourceCat`-  source catalog to display

[ :ref:`Top of page <top>`]  
