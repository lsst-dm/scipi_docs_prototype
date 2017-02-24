##############
ProcessCcdTask
##############


`ProcessCcdTask` is a `command line task <CLTs.html>`_ which executes the
processing steps to turn raw pixel-level data into characterized
images and calibrated catalogs.

.. We also will insert links higher level pages in the Framework docs about CLT's at this location

In more detail, ProcessCcdTask executes the following steps:


1.  `Instrument Signature Removal` -- Implemented by the :doc:`IsrTask <isrtask>` subtask, this step applies  pixel-level corrections in preparation for image characterization. Corrections include: bias, dark current, cross-talk, flat-fielding and bad pixel masking.
    
2. `Image Characterization` -- Implemented by the :doc:`CharacterizeImageTask <charimg>` subtask, this step repairs cosmic ray tracks by interpolating over them, estimates and subtracts a background, and estimates the PSF using a set of high signal-to-noise detections. This entire process is done iteratively, converging to the best PSF possible for the image.
  
3. `Image Calibration`  -- Implemented by the :doc:`CalibrateTask <calibimg>` subtask, this step measures all sources down to a configurable signal-to-noise threshold, fits an astrometric WCS and extracts a photometric zero-point for the image.


This task is implemented in the `lsst.pipe.tasks <taskModules.html#pipetasks>`_ module.

.. seealso::
   
    This task is most commonly called directly on the command line as
    the initial controller task to analyze exposures.
    

    API Usage: See :doc:`ProcessCcdTask API <apiUsage_processccd>`
   
Command Line Usage
==================

`ProcessCcdTask` is available as the processCcd.py  `command line task`_ and is executable directly from the command line as so::

  processCcd.py path/to/input_data [options]

.. Later, when we have the proper technology for it, we will insert the link to the CLT options page at "[options]"  
  
.. _processCcd.py: https://github.com/lsst/pipe_tasks/blob/master/python/lsst/pipe/tasks/processCcd.py


   
Where the path to the input data is required, but all other arguments are optional.

All the flag options available to a normal `command line task`_, which are listed in the `table of CLT options <CLTs.html#optionslink>`_, are also usable for `ProcessCcdTask`.

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
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for image characterization. An example of when this would be used is when a CatalogStarSelector is used. May be ``None`` if the desired loader can be constructed from the butler argument or all steps requiring a catalog are disabled.
 
`astromRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for astrometric calibration. May be ``None`` if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`photoRefObjLoader`
   An instance of LoadReferenceObjectsTasks that supplies an external reference catalog for photometric calibration. May be ``None`` if the desired loader can be constructed from the butler argument or all steps requiring a reference catalog are disabled.
 
`**kwargs`
   Other keyword arguments for `lsst.pipe.base.CmdLineTask <CLTs.html#CLTbaseclass>`_.




Run method
----------
 
.. code-block:: python
 
   run(sensorRef)

(More information can be found at `run <apiUsage_processccd.html#run>`_)


   
Parameters
^^^^^^^^^^
 
`sensorRef`
   `Butler <LSSTglossary.html#butlerlink>`_ data reference for raw data.

Returns
^^^^^^^
 
``struct`` - a `lsst.pipe.base.Struct <objectClasses.html#structlink>`_ containing these fields:

   - `charRes`: object returned by image characterization task; an `lsst.pipe.base.Struct`_ that will include `background` and `sourceCat` fields.
   - `calibRes`: object returned by calibration task: an `lsst.pipe.base.Struct`_ that will include `background` and `sourceCat` fields
   - `exposure`: final exposure (an `lsst.afw.image.ExposureF <LSSTglossary.html#exposureF>`_)
   - `background`: final background model (an `lsst.afw.math.BackgroundList <LSSTglossary.html#bkgdlist>`_)
 





Examples
========

The `obs_test`_ package  models a simple camera with one CCD and includes a data repository containing a few raw images (simulating three visits, two with with the g-band filter, and one with the r-band one), and some associated calibration data. Its camera consists of a single CCD whose geometry matches a subregion of a single LSST CCD.

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

`ProcessCcdTask` has no debug output, but its several subtasks do.


Algorithm details
=================

`ProcessCcdTask` is essentially a wrapper around the three subtasks
that carry out the work, see those for actual contentful algorithmic
details.
