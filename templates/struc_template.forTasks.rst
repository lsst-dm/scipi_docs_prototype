:orphan: true
	 
.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

###########
ExampleTask
###########

Introduction
=============

This section will consist of the following, all of which need to be written:

- Summary/context (1-2 sentences).

- Concise summary of logic/algorithm in a paragaph and/or bullet list.  Be concise and link to other tasks wherever needed.

- Include a sentence about each step, which can be either:

  a) A retargetable sub-task

  b) A method within a task.


     
- Module membership:

  Here, simply state the module the task is implemented inside of.


.. seealso::
  
   -   We put in a `seealso` directive like this one. 
 
   -  It will link to related content, such as:
  
         - Tasks that commonly use this task (this helps a reader landing on a subtask’s page find the appropriate driver task).
     
         - Tasks that can be used instead of this task (to link families of subtasks).
   
         - Pages in the **Processing** and **Frameworks** sections of the Science Pipelines documentation.
  
         - The API Usage page for this Task
     

    
Configuration
=============

- This section describes the task’s configurations defined in the task
  class’s associated configuration class.  It will be split into 2
  natural subsections, as below.

Retargetable Subtasks
---------------------

- For these subtasks, a table will be shown with 3 columns:

  - Subtask name
  - Default target
  - Description of what it does


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

  
Run method
----------

This will consist of:

- A description of the interface for calling the primary entrypoint
  function for the class -- again, this will be picked up
  automatically from the interface of the `run` method and will not
  require developer input.

- A short description of what the `run` method requires as required
  and optional inputs

- Description of the parameters in the run signature


Debugging
=========

- Debugging framework hooks: if there are several debugging
  parameters, they will be displayed in a table similar to how the
  configuration parameters are done, with three columns:

  - Parameter name
  - Parameter type
  - Parameter description

Examples
========

- This will be a self-contained example of using this task that can be
  tested by any reader.

.. Since nothing but the procCcd example is currently working in sfp tasks, those aren't very good prototypes currently here.  We eventually need to figure out how to include these in CI, keep them updated, etc., which is a somewhat open q right now.
  
Algorithm details
====================

- Extended description with mathematical details - this will require
  some thinking on what the significant parts
  of the algorithm are to be presented.  Mathjax will be implemented
  so that the math can be nicely displayed and written in straight tex
  (though the **math** directive of reST).

  
