
##############
ProcessCcdTask
##############


`ProcessCcdTask <#>`_ is a `command line task`_ which executes the processing steps to turn raw pixel data into characterized images and calibrated catalogs.

.. _`command line task`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_base.html#pipeBase_argumentParser

.. We also will insert links higher level pages in the Framework docs about CLT's at this location

.. `ProcessCcdTask <#>`_ will link to the API page when it's made

In more detail, ProcessCcdTask executes the following steps:


1.  `Instrument Signature Removal` -- Implemented by the :doc:`IsrTask <isrtask>` subtask, this step applies  pixel-level corrections in preparation for image characterization. Corrections include: bias, dark current, cross-talk, flat-fielding and bad pixel masking."
    
2. `Image Characterization` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` subtask, this step interpolates over cosmic rays, estimates and subtracts a background, and estimates the PSF using a set of high signal-to-noise detections. This process is iterative.
  
3. `Image Calibration`  -- Implemented by the :doc:`CalibrateTask <calibimg>` subtask, this step measures all sources down to a configurable signal-to-noise threshold, fits an astrometric WCS and extracts a photometric zero-point for the image.


This task is implemented in the `lsst.pipe.tasks`_ module.

.. _lsst.pipe.tasks: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/pipe_tasks.html
    
.. seealso::
   
    This task is most commonly called directly on the command line as
    the initial controller task to analyze exposures.
    

    `API Usage <#>`_: *[To be filled in, like in charimg case]*

.. We will have a link to a separate page here called apiUsage_processccd.rst

Command Line Usage
==================

`ProcessCcdTask <#>`_ is available as the processCcd.py  `command line task`_ and is executable directly from the command line as so::

  processCcd.py path/to/input_data [options]

.. Later, when we have the proper technology for it, we will insert the link to the CLT options page at "[options]"  
  
.. _processCcd.py: https://github.com/lsst/pipe_tasks/blob/master/python/lsst/pipe/tasks/processCcd.py


   
Where the path to the input data is required, but all other arguments are optional.

All the flag options available to a normal `command line task`_, which are listed in the :doc:`table of CLT options <tableOfCLToptions>`, are also usable for `ProcessCcdTask <#>`_.

Configuration
=============

Retargetable Subtasks
---------------------

.. raw:: html

   <table border="1" class="colwidth-given docutils">
     <colgroup>
       <col width="17%">
       <col width="28%">
       <col width="56%">
     </colgroup>
     <thead valign="bottom">
       <tr class="row-odd">
         <th>Task</th>
         <th>Default</th>
         <th>Description</th>
       </tr>
     </thead>
     <tbody valign="top">
       <tr class="row-even">
         <td>
           <code class="xref py py-obj docutils literal">isr</code>
         </td>
         <td>
           <a class="reference internal" href="isrtask.html">
             <span class="doc">IsrTask</span>
           </a>
         </td>
         <td>
           <p>Task to perform instrumental signature removal or load a post-ISR image:</p>
           <ul>
             <li>Assemble raw amplifier images into an exposure with image; variance and mask planes.</li>
             <li>Perform bias subtraction and flat fielding.</li>
             <li>Mask known bad pixels.</li>
             <li>Provide a preliminary WCS.</li>
           </ul>
         </td>
       </tr>
       <tr class="row-odd">
         <td>
           <code class="xref py py-obj docutils literal">charImage</code>
         </td>
         <td>
           <a class="reference internal" href="charimg.html">
             <span class="doc">CharacterizeImageTask</span>
           </a>
         </td>
         <td>
           <p>Task to characterize a science exposure, including:</p>
           <ul>
             <li>Detect sources, usually at high S/N.</li>
             <li>Estimate and subtract the background. Persisted as field <code>background</code>.</li>
             <li>Estimate a PSF model, which is added to the exposure.</li>
             <li>Interpolate over defects and cosmic rays, updating the image, variance, and mask planes.</li>
           </ul>
         </td>
       </tr>
       <tr class="row-even">
         <td>
           <code class="xref py py-obj docutils literal">calibrate</code>
         </td>
         <td>
           <a class="reference internal" href="calibimg.html">
             <span class="doc">CalibrateTask</span>
           </a>
         </td>
         <td>
           <p>Task to perform astrometric and photometric calibration</p>
           <ul>
             <li>Refine the WCS in the exposure.</li>
             <li>Refine the Calib photometric calibration object in the exposure.</li>
             <li>Detect sources, usually at low S/N.</li>
           </ul>
         </td>
       </tr>
     </tbody>
   </table>

	
Parameters
----------

.. csv-table:: 
   :header: Parameter, Type, Default, Description
   :widths: 10, 5, 5, 50

     `doCalibrate` ,`bool`, ``True``, Perform calibration?

     
Python usage
============
 
Class initialization
--------------------
 
.. code-block:: python
 
   lsst.pipe.tasks.processCcd.ProcessCcdTask(
       butler = None,
    	 psfRefObjLoader = None,
    	 astromRefObjLoader = None,
    	 photoRefObjLoader = None,
    	 **kwargs)
 
Parameters
^^^^^^^^^^
 
`butler`
   The butler is passed to the refObjLoader constructor in case it is needed. Ignored if the refObjLoader argument provides a loader directly.
 
`psfRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for image characterization. An example of when this would be used is when a CatalogStarSelector is used. May be None if the desired loader can be constructed from the butler argument or all steps requiring a catalog are disabled.
 
`astromRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`photoRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be None if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`**kwargs`
   Other keyword arguments for `lsst.pipe.base.CmdLineTask`_.

.. _`lsst.pipe.base.CmdLineTask`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1cmd_line_task_1_1_cmd_line_task.html


Run method
----------
 
.. code-block:: python
 
   run(sensorRef)

(More information can be found at `run`_)

.. _run: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1tasks_1_1process_ccd_1_1_process_ccd_task.html#a82488db6374fb538db2ec4418419bdd4
   
Parameters
^^^^^^^^^^
 
`sensorRef`
   `Butler <#>`_ data reference for raw data.

.. Butler: we'll link to this in a glossary, minimally
   
   
Returns
^^^^^^^
 
``struct`` - a `lsst.pipe.base.Struct`_ containing these fields:

.. _`struct`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1struct_1_1_struct.html

.. _`lsst.pipe.base.Struct`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1pipe_1_1base_1_1struct_1_1_struct.html

   - `charRes`: object returned by image characterization task; an `lsst.pipe.base.Struct`_ that will include `background` and `sourceCat` fields.
   - `calibRes`: object returned by calibration task: an `lsst.pipe.base.Struct`_ that will include `background` and `sourceCat` fields
   - `exposure`: final exposure (an `lsst.afw.image.ExposureF <#>`_)
   - `background`: final background model (an `lsst.afw.math.BackgroundList`_)
 
.. We want to eventually link this to a page explaining the different
   kinds of exposures accessible in the afw.image pkg

.. _`lsst.afw.math.BackgroundList`: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/namespacelsst_1_1afw_1_1math.html

Examples
========

The `obs_test`_ package  models a simple camera with one CCD and includes a data repository containing a few raw images (simulating three visits, two with with the `g`-band filter, and one with the `r`-band one), and some associated calibration data. Its camera consists of a single CCD whose geometry matches a subregion of a single LSST CCD.

.. _`obs_test`: https://github.com/LSST/obs_test

The following commands will process all raw data in `obs_test`_'s data
repository. Be sure to specify a `--output` directory that does not
already exist::

  setup obs_test
  setup pipe_tasks
  processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id

The data is read from the small repository in the `obs_test`_ package and output images and catalogs are written to subdirectories in `processCcdOut` (or whatever output name you specified).

Specifying `--id` with no values processes all data.

Add the option `--help` to see more options.


Debugging
=========

`ProcessCcdTask <#>`_ has no debug output, but its several subtasks do.


Algorithm details
=================

`ProcessCcdTask <#>`_ is essentially a wrapper around the three subtasks, see those for actual contentful algorithmic details.
