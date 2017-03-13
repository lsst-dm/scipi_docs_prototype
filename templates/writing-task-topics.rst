:orphan: true
	 
.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

###################
Writing Task Topics
###################

This page describes how to document science pipelines tasks for the
`pipelines.lsst.io <http://pipelines.lsst.io>`_ documentation project.

Using the template
==================

We provide a standardized template for all task documentation
pages. This required template ensures consistency and style, and also
provides you tools for automatically extracting documentation from
your code.

You can obtain the template from :doc:`here <template-for-tasks>`.

Installing the template
-----------------------

To install the template, copy it into the `doc/tasks` directory of
your stack package. Then name the file after the task class, with a
`.rst` extension. For example: `doc/tasks/ProcessCcdTask.rst`.

Filling out the template
------------------------

The template includes brief instructions as reStructuredText
comments. Each component of the documentation page is described in
more detail on this page, below,.



.. _task-topics-intro:

Introduction
============

This section will consist of the below, all of which need to be
written.

- **Summary/context (1-2 sentences):**

.. Note:: Write this section concisely, as it should be very brief,
          and is primarily about whether the reader should choose to
          use this task to achieve h/her goal in a very quick scan.

For example, for `ProcessCcd` we might write:

.. code-block:: rst

 ProcessCcdTask is a command line task which executes the processing
 steps to turn raw pixel-level data into characterized images and
 calibrated catalogs.
	  
	  
- **Concise summary of logic/algorithm in a paragaph and/or bullet list.**

.. Note:: Be concise and link to other tasks wherever needed.  This
          can be a few more sentences, but should not contain very
          many details or math at this point (that will go in the
          algorithmic section at the bottom).  It should just say
          where this fits into the larger DM structure, what
          retargetable subtasks or methods within a task it calls by
          default.

For example, for `ProcessCcd` we would give a list of the 3 subtasks
that `ProcessCcd` invokes to do its job.
	  
.. Note:: If there are optional tasks that are called you can choose
          to fill those in here as well, but note them as optional and
          depending on whether a flag is set in the configuration
          parameters

.. _task-topics-module:

- **Module membership:**

.. Note::  Here, simply state the module the task is implemented inside of, one sentence is sufficient.
	   
.. _task-topics-seealso:
	   
- **"SeeAlso" box:**

.. Note:: The API Usage page for this task will automatically be
          linked to in this box, but please fill in the following
          types of tasks and pages into this section:

  - Tasks that commonly use this task
  
  - Tasks that can be used instead of this task

  - Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

In the case of `ProcessCcd`, we would simply say is called as a
`command line task`, where for e.g. IsrTask, we would say that that it
is most commonly called by `ProcessCcd`.

.. _task-topics-config:	  
    
Configuration
=============

.. _task-topics-retarg:

Retargetable Subtasks
---------------------

.. Note:: This content will be automatically derived from the Task
          code (in which keywords that describe the subtasks in the
          python code, including a `doc` keyword in which the subtask
          is described, will already be written).

.. _task-topics-params:
   
Parameters
----------


.. Note:: Like the Retargetable Subtasks, this content will be derived
          from keywords that describe the parameters where they are
          defined in the Task Config class.


.. _task-topics-python:
   
Python usage
============

.. _task-topics-initzn:

Class initialization
--------------------

- The interface declaring the instance of the class will be
  picked up automatically from the interface of the `__init__` method
  and will not require developer input.
  
.. _task-topics-run:
	  
Run method
----------

- Similarly to the Class initialization, the description of the
  interface for calling the primary entrypoint function of the class
  will be picked up automatically from the interface of the `run`
  method and will not require developer input.

  
.. _task-topics-debug:

Debugging
=========

- Also similarly to the Class initialization, information on the
  debugging parameters, specifically their name, type, and
  description, will be picked up automatically from docstrings in the
  class definition.

.. _task-topics-examples:
   
Examples
========

.. Note:: Making this can be a substantial job which requires writing
          an actual example and then going through and describing line
          by line in comments inside of it what the example is doing.


The example should be very stripped down and use only the basic functionality of the Task.

To give some specific guidance, we will give a few pointers for how
one might write an example for IsrTask, which we will call
`exampleIsrTask.py`, then describe it with reST.

In this particular case, we need to use some functions which are
normally in the `utils.py` class, and to make it more transparent, we
might want to strip this down and rewrite them locally in the
`exampleUtils.py` class.

Next, we describe some of the details for the content of `exampleIsrTask.py`.

Where needed, when describing code, the python code block directive can be used as so:

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
		
 The first line: `isrConfig = IsrTask.ConfigClass()` indicates this is
 a section about setting up the configuration that the code will be run
 with.  The next several set up specific flags, indicating that we will
 not do bias or fringing corrections in this code, but will do the dark
 and flat corrections.

We can then describe the other intermediate sections in ways similar to
the above, saying that the final output is created with the call to
the `IsrTask` `run` method:

.. code-block:: python
		
       output = isrTask.run(rawExposure, dark=darkExposure, flat=flatExposure)


.. _task-topics-algorithm:
   
Algorithm details
====================

This should be written in detailed form and can refer to prior written
documentation as long as it is accessible by all potential code users.
Mathematical notation can be used here and written in LaTex through the `math`
directive of reST, for details see `this section of the Developer Guide that
describes how to insert mathematical expressions
<https://developer.lsst.io/docs/rst_styleguide.html#rst-math>`_ .

Here is an example of the syntax for how one would insert an equation (from IsrTask):

.. code-block:: rst

  :math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]` 		
  
Which will render as:

:math:`Ic(x) = I(x) + {1 \over 2} {d \over dx} \left[ I(x) {d \over dx} \int K(x-y) I(y) dy  \right]`
      
