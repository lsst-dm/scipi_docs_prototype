
######################
API for ProcessCcdTask
######################

Class initialization
==================== 
 
.. code-block:: python
 
   lsst.pipe.tasks.processCcd.ProcessCcdTask(
       butler = None,
    	 psfRefObjLoader = None,
    	 astromRefObjLoader = None,
    	 photoRefObjLoader = None,
    	 **kwargs)
 
Parameters
----------
 
``butler``
   The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.
 
``psfRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for image characterization. An example of when this would be used is when a CatalogStarSelector is used. May be None if the desired loader can be constructed from the butler argument or all steps requiring a catalog are disabled.
 
``astromRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
``photoRefObjLoader``
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
``**kwargs``
   Other keyword arguments for lsst.pipe.base.CmdLineTask.



Run method
==========
 
.. code-block:: python
 
   run(sensorRef)
 
Parameters
----------
 
``sensorRef``
   butler data reference for raw data.
 
Returns
-------
 
``struct`` (lsst.pipe.base.Struct)
   lsst.pipe.base.Struct containing these fields:
 
   - ``charRes``: object returned by image characterization task; an lsst.pipe.base.Struct that will include "background" and "sourceCat" fields.
   - ``calibRes``: object returned by calibration task: an lsst.pipe.base.Struct that will include "background" and "sourceCat" fields
   - ``exposure``: final exposure (an lsst.afw.image.ExposureF)
   - ``background``: final background model (an lsst.afw.math.BackgroundList)


