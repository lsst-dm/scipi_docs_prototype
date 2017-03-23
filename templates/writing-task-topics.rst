.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

###################
Writing Task Topics
###################

This page describes how to document science pipelines tasks for the `pipelines.lsst.io <https://pipelines.lsst.io>`_ documentation project.

.. _task-topics-usage:

Using the template
==================

We provide a standardized template for all task documentation pages.
This required template ensures consistency and style, and also provides you tools for automatically extracting documentation from your code.

You can obtain the template from :doc:`here <template-for-tasks>`.

.. _task-topics-install:

Installing the template
-----------------------

To install the template, copy it into the `doc/tasks` directory of your stack package. Then name the file after the task class, with a `.rst` extension.
For example: `doc/tasks/ProcessCcdTask.rst`.

.. _task-topics-instructions:

Filling out the template
------------------------

The template includes brief instructions as reStructuredText comments.
Each component of the documentation page is described in more detail on this page, below.


.. _task-topics-title:

Titling the Page
================

The title of the page should be the name of the task class (*ProcessCcdTask*, for example).


.. _task-topics-summary:

Summary/context (1-2 sentences)
===============================
Write this section concisely, as it should be very brief, and is primarily about whether the reader should choose to use this task to achieve h/her goal in a very quick scan.

For example, for `ProcessCcd` we might write:

.. code-block:: rst

   ProcessCcdTask is a command line task which executes the processing
   steps to turn raw pixel-level data into characterized images and
   calibrated catalogs.

.. _task-topics-logic:
	  
Summary of logic/algorithm
==========================
This should be done in just a paragaph and/or a bullet list.
Be concise and link to other tasks wherever needed.
This can be a few more sentences, but should not contain very many details or math at this point (that will go in the algorithmic section at the bottom).
It should just say where this fits into the larger DM structure, what retargetable subtasks or methods within a task it calls by default.

For example, for `ProcessCcd` we would give a list of the 3 subtasks that `ProcessCcd` invokes to do its job.  For another example, for `IsrTask` we might say:

.. code-block:: rst
		
   Instrument Signature Removal (ISR) is a sequence of steps taken to
   correct the effects imprinted on the counts coming out of the readout
   by the physical characteristics of the detector and the electronics of
   the readout chain.  It is generally the very first procedure carried
   out on the pixel-level data of an exposure.
	  
If there are optional tasks that are called you can choose to fill those in here as well, but note them as optional and depending on whether a flag is set in the configuration parameters

.. _task-topics-module:

Module membership
=================
Here, simply state the module the task is implemented inside of, filling in the required line in the template.

For example, for `ProcessCcd`

.. code-block:: rst

   This task is implemented in the `lsst.pipe.tasks <taskModules.html#pipetasks>`_ module.

.. _task-topics-seealso:
	   
"SeeAlso" box
=============
The API Usage page for this task will automatically be linked to in this box, but please fill in the following types of tasks and pages into this section:

  - Tasks that commonly use this task (this helps a reader
    landing on a subtask’s page find the appropriate driver
    task).     
  
  - Tasks that can be used instead of this task (to link families of subtasks).   

  - Pages in the **Processing** and **Frameworks** sections of the Science Pipelines documentation.

  - The API Usage page for this Task

In the case of `ProcessCcd`, we would simply say is called as a `command line task`, where for e.g. IsrTask, we would say that that it is most commonly called by `ProcessCcd`.

.. _task-topics-config:	  

Configuration
=============
The guidance here we give is how to describe configuration flags inside the code itself, as they will be picked up automatically and populated into this page.

At the very beginning of your TaskNameConfig class, you will put in a simple docstring that explains what this class does.

E.g. at the top of `ProcessCcdConfig` we would write:

.. code-block:: rst
		
    """Config for ProcessCcd"""

After this, we have the standard listing of configurable parameters and retargetable subtasks for the task, and inside of each of these write a description in a string for what that specific parameter or subtask does.


.. _task-topics-params:
   
Parameters
----------

To given one example here, for `ProcessCcdConfig` we have a `pexConfig.Field` configurable parameter called `doCalibrate`, and we can write into the string that describes it

.. code-block:: rst

   doc="Perform calibration?"

These `doc` normal string variables will be be shown verbatim when the `--show config` flag is used when a command is executed, and should contain minimal reST syntax to make them more readable when printed out.
   
.. _task-topics-retarg:

Retargetable Subtasks
---------------------

As an example for documenting the retargetable subtask named `calibrate` in `ProcessCcdConfig` we might write:

.. code-block:: rst

   doc="""Task to perform astrometric and photometric calibration:
            - refine the WCS in the exposure
            - refine the Calib photometric calibration object in the exposure
            - detect sources, usually at low S/N
       """


As for parameters, the `doc` content will be shown verbatim when the `--show config` flag is used when a command is executed, and should contain minimal reST syntax to make them more readable when printed out.

.. _task-topics-python:
   
Python usage
============

.. _task-topics-initzn:

Class initialization
--------------------
The guidance here we give is how to describe the class initialization and the parameters of the signature inside the code itself, as this will all be picked up automatically and populated into this page.

For the `__init__` class of `ProcessCcd` we might write for the starting part of the docstring:


.. code-block:: rst
		
   """!
   @param[in] butler  The butler is passed to the refObjLoader constructor in case it is
      needed.  Ignored if the refObjLoader argument provides a loader directly.
   @param[in] psfRefObjLoader  An instance of LoadReferenceObjectsTasks that supplies an
      external reference catalog for image characterization.  An example of when this would
      be used is when a CatalogStarSelector is used.  May be None if the desired loader can
      be constructed from the butler argument or all steps requiring a catalog are disabled.
   """

.. _task-topics-run:
	  
Run method
----------
The guidance here we give is how to describe the run method and the parameters of its signature inside the code itself, as this will all be picked up automatically and populated into this page.

We do this by inserting a docstring at the beginning of the `run` method, describing initially what it does, then the parameters and returns from it, as an example from `ProcessCcd` we might write:


.. code-block:: rst

   """Process one CCD

   The sequence of operations is:
   - remove instrument signature
   - characterize image to estimate PSF and background
   - calibrate astrometry and photometry

   @param sensorRef: butler data reference for raw data

   @return pipe_base Struct containing these fields:
   - charRes: object returned by image characterization task; an lsst.pipe.base.Struct
     that will include "background" and "sourceCat" fields
   - calibRes: object returned by calibration task: an lsst.pipe.base.Struct
     that will include "background" and "sourceCat" fields
   - exposure: final exposure (an lsst.afw.image.ExposureF)
   - background: final background model (an lsst.afw.math.BackgroundList)
   """
		
.. _task-topics-debug:

Debugging
=========
The guidance here we give is how to describe debugging flags inside the code itself, as they will be picked up automatically and populated into this page.

Here we will use an example for `IsrTask`, where we might write:

.. code-block:: rst

   - `display` - A dictionary containing debug point names as keys with frame number as value.  The only valid key is:

      `postISRCCD`_ (to display exposure after ISR has been applied)
		
.. _task-topics-examples:
   
Examples
========

Making a good example can be a substantial job which requires writing the actual code and then going through and describing line by line in comments inside it to explain what the example is doing.  

The example should be very stripped down and use only the basic functionality of the task.  It should also be self-contained, allowing a user to follow a few steps to exercise the task. Any data and configuration should be included in the example.

To give some specific guidance, we will give a few pointers for how one might write an example for IsrTask, which we will call `exampleIsrTask.py`, then describe it with reST.

In some cases, we might want to write a separate local `utilities.py` class which will contain some some utility functions which are normally spread found in other packages.
By writing them locally, we can allow the user to inspect the functions immediately without going far afield for them.

Next, we describe some of the details for the content of `exampleIsrTask.py`.

Where needed, when describing any part of code, including task configuration, the python code block directive can be used as so:

.. code-block:: rst

   .. code-block:: python

      #Create the isr task with modified config
      isrConfig = IsrTask.ConfigClass()
      isrConfig.doBias = False #We didn't make a zero frame
      isrConfig.doDark = True
      isrConfig.doFlat = True
      isrConfig.doFringe = False #There is no fringe frame for this example
		   
Then, to describe the block setting up configuration parameters, we can say in reST:

.. code-block:: rst
		
   The first line: ``isrConfig = IsrTask.ConfigClass()`` indicates this is
   a section about setting up the configuration that the code will be run
   with.  The next several set up specific flags, indicating that we will
   not do bias or fringing corrections in this code, but will do the dark
   and flat corrections.

We can then describe the other intermediate sections in ways similar to the above, saying that the final output is created with the call to the `IsrTask` `run` method:

.. code-block:: python
		
   output = isrTask.run(rawExposure, dark=darkExposure, flat=flatExposure)


.. _task-topics-algorithm:
   
Algorithm details
=================

This should be written in detailed form and can refer to prior written documentation as long as it is accessible by all potential code users.
Mathematical notation can be used here and written in LaTeX through the :rst:directive:`math directive <sphinx:math>` of reST, for details on this see `the reStructuredText Style Guide <https://developer.lsst.io/docs/rst_styleguide.html#rst-math>`_ .

Here is an example of the syntax for inserting an equation (from IsrTask):

.. code-block:: rst

   :math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]` 		
  
Which will render as:

:math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]`
      
