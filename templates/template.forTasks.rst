
.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

###########
ExampleTask
###########

.. role:: red
	  
We give guidance here for developers on what to write into their
docstrings in the code in order to populate the documentation page
best.  These docstrings will be written in Numpydoc format.

Some sections are automatically populated from the code and will not
require developer input, and we demarcate those as well, here.

Introduction
=============

This section will consist of the following, all of which need to be written:

- Summary/context (1-2 sentences):

.. note:: Write this section concisely, as it should be very brief, and is primarily about whether the reader should choose to use this task to  achieve h/her goal in a very quick scan.

- Concise summary of logic/algorithm in a paragaph and/or bullet list.

.. note:: Be concise and link to other tasks wherever needed.  This can be a  few more sentences, but should not contain very many details or math  at this point (that will go at the bottom).  It should just say  where this fits into the larger DM structure, what retargetable  subtasks or methods within a task it calls by default.

The  doc-building code will automatically link these to the appropriate  destinations ultimately, as for other methods and tasks below as well.

.. note:: If there are optional tasks that are called you can choose to fill those in here as well, but not them as optional and depending on  whether a flag is set in the configuration parameters

.. We used to have this, but i think it's covered now by the above:
..   - Do include a sentence about each step, which can be either a:
..  a) retargetable sub-task
..  b) methods within a task

     
- Module membership:

.. note::  Here, simply state the module the task is implemented inside of.

.. seealso::

  This seealso directive will link to related content, such as:

  - Tasks that commonly use this task (this helps a reader landing on
    a “subtask’s” page find the appropriate driver task).
  
  - Tasks that can be used instead of this task (to link families of subtasks).

  - Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

  - The API Usage page for this task

.. note:: So please fill in all the above types of tasks and pages into this section.  

    
Configuration
=============

- This section describes the task’s configurations defined in the task  class’s associated configuration class.  It will be split into 2  natural subsections, as below.

Retargetable Subtasks
---------------------

- For these subtasks, a table will be shown with 3 columns:

  - Subtask name
  - Default target
  - Description of what it does

.. note:: So please fill in the docstring for each subtask must with its default
target and further, a description of what the subtask is supposed to
do.

..  [We would also like to provide list of everything to which this could be retargeted.. do we need the developer to do this too, we didn't for the sfp tasks..  ]

- Ultimately, the parameter type will link to a documentation  topic for that type (such as a class’s API reference), which will  happen automatically.

.. For the sfp pages, these links were all stubs

Parameters
----------

Here, configuration parameters will be displayed in a table with the following fields:

- Parameter name.

- Parameter type.  These are generally simple python var types
  (i.e. `bool`, `int`, `float`, or `str`) , which will automatically be
  linked to existing python documentation on these types)

- Default value of parameter.

- A description sentence or paragraph. The description should also
  mention caveats, and possibly give an example.

.. I don't think there are any examples in any of the sfp tasks.. i wonder if this should actually be in there.
   
.. note:: Please fill in the docstrings in the config class for this task with all the above (type, default value, description), for each parameter.

.. - It would be good to call out the most frequently changed config vars in some way as well -- we haven't talked about asking developers to delineate these, yet.


Python usage
============

Class initialization
--------------------

This section will consist of:

- Interface for declaring an instance of the class -- this will be
  picked up automatically from the interface of the `__init__` method
  and will not require developer input.
  
- Description of the parameters in the interface signature

.. note:: Please separately enter information on each  parameter in a docstring in the `__init__` method.
  
Run method
----------

This will consist of:

- A description of the interface for calling the primary entrypoint
  function for the class -- again, this will be picked up
  automatically from the interface of the `run` method and will not
  require developer input.

- A short description of what the `run` method requires as required
  and optional inputs

.. note:: Again, please enter this information in a docstring in the `run` method.
  
- Description of the parameters in the run signature

.. note:: Once again, please separately enter information on each parameter in a docstring in the `run` method.
  

Debugging
=========

- Debugging framework hooks: if there are several debugging
  parameters, they will be displayed in a table similar to how the
  configuration parameters are done, with three columns:

  - Parameter name
  - Parameter type
  - Parameter description

.. note:: Please fill in all of these are to be analogously to how the configuration parameters are done in docstrings.

Examples
========

- This will be a self-contained example of using this task that can be
  tested by any reader.

.. note:: Making this is a substantial job which requires writing an
  actual example and then going through and describing line by line in 
  the docstrings inside of it what the example is doing.

.. Since nothing but the procCcd example is currently working in sfp tasks, those aren't very good prototypes currently here.  We eventually need to figure out how to include these in CI, keep them updated, etc., which is a somewhat open q right now.
  
Algorithm details
====================

- Extended description with mathematical details - this will require
  some thinking on what the significant parts
  of the algorithm are to be presented.  Mathjax will be implemented
  so that the math can be nicely displayed and written in straight tex
  (though the math directive of reST).
