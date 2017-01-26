
###############
API for IsrTask
###############

*[Incomplete]*

Class initialization
==================== 
 
.. code-block:: python
 
   lsst.ip.isr.isrTask.IsrTask(
       *args,
       **kwargs
       )
 
Parameters
----------
 
``*args``
   A list of positional arguments passed on to the Task constructor   
  
``**kwargs``
   A dictionary of keyword arguments passed on to the Task constructor
   



Run method
==========
 
.. code-block:: python
 
   run(ccdExposure,
 	bias = None,
 	linearizer = None,
 	dark = None,
 	flat = None,
 	defects = None,
 	fringes = None,
 	bfKernel = None
	)
	
 
Parameters
----------
 
- ``ccdExposure``	– lsst.afw.image.exposure of detector data
- ``bias``	– exposure of bias frame
- ``linearizer``	– linearizing functor; a subclass of lsst.ip.isr.LinearizeBase
- ``dark``	– exposure of dark frame
- ``flat``	– exposure of flatfield
- ``defects``	– list of detects
- ``fringes``	– a pipeBase.Struct with field fringes containing exposure of fringe frame or list of fringe exposure
- ``bfKernel``	– kernel for brighter-fatter correction


 
Returns
-------
 
``struct`` (lsst.pipe.base.Struct)
   lsst.pipe.base.Struct containing these fields:
 
   - ``exposure``: exposure of processed detector data (an lsst.afw.image.Exposure)



