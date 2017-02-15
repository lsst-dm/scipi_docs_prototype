
Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type

###########
ExampleTask
###########

- Summary/context (1-2 sentences).

- Concise summary of logic/algorithm in a paragaph and/or bullet list.  Be concise and link to other tasks wherever needed.

- Include a sentence about each step, which can be either a:
  
  a) retargetable sub-task

  b) method within a task.


     
- Module membership:

  Here we simply state in which module the task is implemented.

.. seealso::

   Will put in a seealso directive like this one. 
   
  It will link to related content, such as:

  - Tasks that commonly use this task (this helps a reader landing on a “sub task’s” page find the appropriate driver task).
  
  - Tasks that can be used instead of this task (to link families of sub tasks).

  - Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

  - The API Usage page for this Task


    
Configuration
=============

- This section describes the task’s configurations defined in the task class’s associated configuration class.  We split it into 2 natural subsections.

Retargetable Subtasks
---------------------

- For these subtasks, we give a table with:

  - Subtask name
  - Default target
  - Description of what it does

- We would also like to provide list of everything to which this could
  be retargeted.

- Ideally the parameter type links to a documentation topic for that type (such as a class’s API reference)

Parameters
----------

Here, configuration parameters are displayed in a table with the following fields:

- Parameter name.

- Parameter type.  These are generally simple python var types (i.e. `bool`, `int`, `float`, or `str` )

- Default value of parameter.

- A description sentence or paragraph. The description should also mention caveats, and possibly give an example.

- It would be good to call out the most frequently changed config vars in some way as well.


Python usage
============

Class initialization
--------------------

- Interface for declaring an instance of the class

- Description of the parameters in the interface signature

Run method
----------

- A description of the interface for calling the primary entrypoint function for the class

- Description of the parameters in the run signature
  

Debugging
=========

- Debugging framework hooks

Examples
========

- Self-contained example of using this task that can be tested

Algorithm details
====================

- Extended description with mathematical details
