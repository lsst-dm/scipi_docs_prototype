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

Below, the normal text lists notes on the each of the sections of the
template, some of which is repeated from the `Task Template
<struc_template.forTasks.html>`_, but here with more specific
direction to the developer of what to include into the reST for that
section.

To be explicit, we will give some examples for what to put into the
sections taken primarily from `ProcessCcd` specifically, but from other tasks as well.

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

For example, for `ProcessCcd` we might write:

``ProcessCcdTask is a command line task which executes the processing
steps to turn raw pixel-level data into characterized images and
calibrated catalogs.``
	  
	  
- **Concise summary of logic/algorithm in a paragaph and/or bullet list.**

.. Note:: Be concise and link to other tasks wherever needed.  This can be a  few more sentences, but should not contain very many details or math  at this point (that will go in the algorithmic section at the bottom).  It should just say  where this fits into the larger DM structure, what retargetable  subtasks or methods within a task it calls by default.

For example, for `ProcessCcd` we would give a list of the 3 subtasks that `ProcessCcd` invokes to do its job.
	  
.. Note:: If there are optional tasks that are called you can choose to fill those in here as well, but note them as optional and depending on  whether a flag is set in the configuration parameters

.. _module:

- **Module membership:**

.. Note::  Here, simply state the module the task is implemented inside of, one sentence is sufficient.
	   
.. _seealso:
	   
- **"SeeAlso" box:**

.. Note:: The API Usage page for this task will automatically be linked to in this box, but please fill in the following types of tasks and pages into this section:

  - Tasks that commonly use this task
  
  - Tasks that can be used instead of this task

  - Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

In the case of `ProcessCcd`, we would simply say is called as a `command line task`, where for e.g. IsrTask, we would say that that it is most commonly called by `ProcessCcd`.

.. _config:	  
    
Configuration
=============

.. _retarg:

Retargetable Subtasks
---------------------

.. Note:: This content will be automatically derived from the Task code (in which keywords that describe the subtasks in the python code, including a `doc` keyword in which the subtask is described, will already be written).

.. _params:
   
Parameters
----------


.. Note:: Like the Retargetable Subtasks, this content will be derived from keywords that describe the parameters where they are defined in the Task Config class.


.. _python:
   
Python usage
============

.. _initzn:

Class initialization
--------------------

- The interface declaring the instance of the class will be
  picked up automatically from the interface of the `__init__` method
  and will not require developer input.
  
.. _run:
	  
Run method
----------

- Similarly to the Class initialization, the description of the interface for calling the primary entrypoint  function of the class will be picked up  automatically from the interface of the `run` method and will not  require developer input.

  
.. _debug:

Debugging
=========

- Also similarly to the Class initialization, information on the debugging parameters, specifically their name, type, and description, will be picked up  automatically from docstrings in the class definition.

.. _examples:
   
Examples
========

.. Note:: Making this can be a substantial job which requires writing an actual example and then going through and describing line by line in comments inside of it what the example is doing.


The example should be very stripped down and use only the basic functionality of the Task.  You don't necessarily need to write a separate example, but can use run on a directory that already contains some test data, for example for `ProcessCcd`, one can just exercise the code via e.g.:

``processCcd.py $OBS_TEST_DIR/data/input --output processCcdOut --id``

.. _algo:
   
Algorithm details
====================

This should be written in detailed form and can refer to prior written
documentation as long as it is accessible by all potential code users.
Mathematical notation can be used here and written in LaTex through the `math`
directive of reST, for details see `this section of the Developer Guide that
describes how to insert mathematical expressions
<https://developer.lsst.io/docs/rst_styleguide.html#rst-math>`_ .

Here is an example of the syntax for how one would insert an equation (from IsrTask):

```:math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]`
```

.. Hm - how to remove initial and final bticks in how the above appears on the page.. (?)
   
Which will render as:

:math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]`
      
