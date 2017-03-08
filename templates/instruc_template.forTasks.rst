:orphan: true
	 
.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

########################
Guidance for ExampleTask
########################

We give guidance here for developers on what to write into the
reStructured Text (reST) `Task Template
<struc_template.forTasks.html>`_ which, when processed by the
documentation-building code, will make the primary page for that Task.

Some sections are fully automatically populated from python docstrings
in the code and will not require developer input, and this information
is also copied into the API page for this Task.  We demarcate those
sections as well and guidance for how to write those docstrings is
covered in `this section of the Developer Guide
<https://developer.lsst.io/docs/py_docs.html>`_ .

.. in order to populate the documentation page best.

Below, the normal text lists notes on the each of the sections of the
template, some of which is repeated from the `Task Template
<struc_template.forTasks.html>`_, but here with more specific
direction to the developer of what to include into the reST for that
section.

To be explicit, we will give some examples for what to put into the
sections taken primarily from procCcd specifically, but from other tasks as well.

.. and general contents in them,

[NB: The structure is substantially different from how docstrings were
populated for DM's previous Doxygen documentation, for those familiar
with it.]

.. _intro:

Introduction
=============

This section will consist of the below, all of which need to be
written.

- **Summary/context (1-2 sentences):**

.. Note:: Write this section concisely, as it should be very brief, and is primarily about whether the reader should choose to use this task to  achieve h/her goal in a very quick scan.

For example, for procCcd we might write:

``ProcessCcdTask is a command line task which executes the processing
steps to turn raw pixel-level data into characterized images and
calibrated catalogs.``
	  
	  
- **Concise summary of logic/algorithm in a paragaph and/or bullet list.**

.. Note:: Be concise and link to other tasks wherever needed.  This can be a  few more sentences, but should not contain very many details or math  at this point (that will go in the algorithmic section at the bottom).  It should just say  where this fits into the larger DM structure, what retargetable  subtasks or methods within a task it calls by default.

For example, for procCcd we would give a list of the 3 subtasks that procCcd invokes to do its job.
	  
.. The  documentation-building code will automatically link these to the appropriate  destinations ultimately, as for other methods and tasks below as well.

.. Note:: If there are optional tasks that are called you can choose to fill those in here as well, but note them as optional and depending on  whether a flag is set in the configuration parameters

.. We used to have this, but i think it's covered now by the above:
..   - Do include a sentence about each step, which can be either a:
..  a) retargetable sub-task
..  b) methods within a task

   
.. _module:

- **Module membership:**

.. Note::  Here, simply state the module the task is implemented inside of, one sentence is sufficient.
	   
.. _seealso:
	   
- **"SeeAlso" box:**

.. Note:: The API Usage page for this task will automatically be linked to in this box, but please fill in the following types of tasks and pages into this section:

  - Tasks that commonly use this task
  
  - Tasks that can be used instead of this task

  - Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

In the case of procCcd, we would simply say is called as a `command line task`, where for e.g. IsrTask, we would say that that it is most commonly called by procCcd.

.. _config:	  
    
Configuration
=============

.. _retarg:

Retargetable Subtasks
---------------------

.. Note:: This content will be automatically derived from the Task code (in which keywords that describe the subtasks in the python code, including a `doc` keyword in which the subtask is described, will already be written).

..	  Inside of the Task Config class (which is generally defined in the the same file as the Task itself), please fill in the `target` keyword with the name of the default subtask and the `doc` keyword with a string with a description of what the subtask is supposed to do.

.. [We would also like to provide a list of everything to which this could be retargeted.. do we need the developer to do this too, we didn't for the sfp tasks..  ]

.. For the sfp pages, these links were all stubs

.. _params:
   
Parameters
----------


.. I don't think there are any examples in any of the sfp tasks.. i wonder if this should actually be in there.
   
.. Note:: Like the Retargetable Subtasks, this content will be derived from keywords that describe the parameters where they are defined in the Task Config class.


.. Please fill in the keywords strings in the Config Class for this task with the following properties for each parameter: type, default value, description.

.. - Later, the parameter type will link to a documentation topic for that type automatically.

.. - It would be good to call out the most frequently changed config vars in some way as well -- we haven't talked about asking developers to delineate these, yet.

.. _python:
   
Python usage
============

.. _initzn:

Class initialization
--------------------

- The interface declaring the instance of the class will be
  picked up automatically from the interface of the `__init__` method
  and will not require developer input.
  
..  The content describing the parameters in the interface signature will be derived from the content of a docstring which will go at the top of the `__init__` method.  Please separately enter information on each parameter there.

.. _run:
	  
Run method
----------

- Similarly to the Class initialization, the description of the interface for calling the primary entrypoint  function of the class will be picked up  automatically from the interface of the `run` method and will not  require developer input.

..  The description of what the `run` method requires as required  and optional inputs goes at the top of the `run` method in a docstring.  Please enter this information.
  
..  Similarly, please separately enter information on each parameter in the run signature in the same docstring in the `run` method.
  
.. _debug:

Debugging
=========

- Also similarly to the Class initialization, information on the debugging parameters, specifically their name, type, and description, will be picked up  automatically from docstrings in the class definition.

.. for the task. of the interface for calling the primary entrypoint  function of the class will be  the interface of the `run` method and will not  require developer input.

..  Information on the debugging parameter name, type, and description should be inserted into a docstring also in the class definition for the task.

.. _examples:
   
Examples
========

.. Note:: Making this can be a substantial job which requires writing an actual example and then going through and describing line by line in comments inside of it what the example is doing.


..	  This should be inserted into docstrings in the class definition for the task, after the above content listed in the `Debug` section.

The example should be very stripped down and use only the basic functionality of the Task.  You don't necessarily need to write a separate example, but can use example in a directory that already contains some data, for example for procCcd, one can just exercise the code via e.g.:

``processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id``

.. Since nothing but the procCcd example is currently working in sfp tasks, those aren't very good prototypes currently here.  We eventually need to figure out how to include these in CI, keep them updated, etc., which is a somewhat open q right now.

.. _algo:
   
Algorithm details
====================

This should be written in detailed form and can refer to prior written
documentation as long as it is accessible by all potential code users.
Mathematical notation can be used here and written in LaTex through the `math`
directive of reST, for details see `this section of the Developer Guide that
describes how to insert mathematical expressions
<https://developer.lsst.io/docs/rst_styleguide.html#rst-math>`_ .

