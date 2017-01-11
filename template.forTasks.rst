
Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type

##################
Template for Tasks
##################

- Summary/context (1 sentence).

- Summary of logic/algorithm in a paragaph and/or bullet list.  Be concise and link to other tasks wherever needed.

- Include a sentence about each step, which can be either a:
  
  - a) retargetable sub-task

  - b) method within a task.

- Module membership

Here we state what module implemented the task.

See also
=========

.. seealso::

   Will put in a seealso directive like this.
   
It will link to related content, such as:

- Tasks that commonly use this task (this helps a reader landing on a “sub task’s” page find the appropriate driver task).
  
- Tasks that can be used instead of this task (to link families of sub tasks).

- Pages in the Processing and Frameworks sections of the Science Pipelines documentation.

    
Configuration
=============

- This section describes the task’s configurations defined in the task class’s associated configuration class. Configuration parameters are displayed with the following fields per configuration:


- Parameter name.

- Parameter type. Ideally the parameter type links to a documentation topic for that type (such as a class’s API reference), if it's anything beyond simple python var types.

- Default value of parameter.

- A description sentence or paragraph. The description should also mention caveats, and possibly give an example.

- It would be good to call out the most frequently changed config vars in some way as well.

The Configuration section will be split into two types:

Flags  and utility variables
----------------------------

- Simple `boolean`, `int`, `float`, or `str` config vars
  
Subtasks
--------

- For subtasks, provide list of everything to which this could be retargeted.


Entrypoint
==========

- Link to API page for the "run" method.

(Note that task run methods are not necessarily named ‘run,’ nor do they necessarily share a uniform interface.)

Butler Inputs
=============

- Dataset type + description of Butler gets()

- Best effort for now; hopefully auto-doc'd in SuperTask framework

Butler Outputs
==============

- Dataset type + description of Butler puts()

- Best effort for now; hopefully auto-doc'd in SuperTask framework

Examples
========

- Self-contained example of using this task that can be tested

Debugging
=========

- Debugging framework hooks


Algorithm details
====================

- Extended description with mathematical details
