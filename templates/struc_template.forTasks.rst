:orphan: true
	 
.. Based on: https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with learnings from the 4 sfp pages built in branch DM-8717

Please fill in the below sections with the contents as described in the reST comments, removing the comments as you do so, and using the links to locations in the Guidance Document if needed. 


########################
Structure of ExampleTask 
########################

.. Introductory material - this section needs the following filled in:

.. - Summary/context (1-2 sentences).

.. - Concise summary of logic/algorithm in a paragaph and/or bullet list.

.. - A sentence about each step, which can be either:

..  a) A retargetable subtask

..  b) A method within a task.

.. `Guidance for the Introduction Section  <instruc_template.forTasks.html#intro>`_ .


.. - Module Membership:

..  This section needs only the module the task is implemented inside of.

.. `Guidance for the Module Membership Section  <instruc_template.forTasks.html#module>`_ .

.. SeeAlso Box:
  
..   -  Things inside the `seealso` directive box need to link to related content, such as:
  
         - Tasks that commonly use this task (this helps a reader landing on a subtask’s page find the appropriate driver task).
     
         - Tasks that can be used instead of this task (to link families of subtasks).
   
         - Pages in the **Processing** and **Frameworks** sections of the Science Pipelines documentation.
  
         - The API Usage page for this Task
     
..         `Guidance for the See Also Section  <instruc_template.forTasks.html#seealso>`_ .

    
Configuration
=============

.. - This section describes the task’s configurations defined in the task class’s associated configuration class.  It will be split into 2  natural subsections, as below.

Retargetable Subtasks
---------------------

.. This section does not need filling in by hand as in this case, the content is filled in from strings in the code itself, not in this reST document (see Guidance Doc for details).   

.. (Wonder if i need to specify any of the below since we're not filling this in by hand..)
   
.. - For these subtasks, a table will be shown with 3 columns:

..  - Subtask name
..  - Default target
..  - Description of what it does

.. - Ultimately, the parameter type will link to a documentation topic for that type (such as a class’s API reference).

.. (For the sfp pages, these links were all stubs)

.. `Guidance for the Retargetable Subtasks Subsection  <instruc_template.forTasks.html#retarg>`_ .
   
Parameters
----------

.. This section does not need filling in by hand as in this case, the content is filled in from strings in the code itself, not in this reST document (see Guidance Doc for details).   

.. Here, configuration parameters will be displayed in a table with the following fields:

.. - Parameter name.

.. - Parameter type.  These are generally simple python var types (i.e. `bool`, `int`, `float`, or `str`) , which will automatically be  linked to existing python documentation on these types)

.. - Default value of parameter.

.. - A description sentence or paragraph. The description should also mention caveats, and possibly give an example.

.. (I don't think there are any examples in any of the sfp tasks.. i wonder if this should actually be in there.)
   
.. (It would be good to call out the most frequently changed config vars in some way as well -- we haven't talked about asking developers to delineate these, yet.)

.. `Guidance for the Parameters Subsection  <instruc_template.forTasks.html#params>`_ .

Python usage
============

Class initialization
--------------------

.. This section does not need filling in by hand as in this case, the content is filled in from strings in the code itself, not in this reST document (see Guidance Doc for details).   

.. This section consists of:

.. - Interface for declaring an instance of the class
  
.. - Description of the parameters in the interface signature

.. These are filled in in the code itself, not in this reST document.
   
.. `Guidance for the Class initialization Subsection  <instruc_template.forTasks.html#initzn>`_ .

Run method
----------

.. This section does not need filling in by hand as in this case, the content is filled in from strings in the code itself, not in this reST document (see Guidance Doc for details).   

.. This will consist of:

.. - A description of the interface for calling the primary entrypoint function for the class -- again, this will be picked up  automatically from the interface of the `run` method and will not  require developer input.

.. - A short description of what the `run` method requires as required and optional inputs

.. - Description of the parameters in the run signature

.. `Guidance for the Run Method Subsection  <instruc_template.forTasks.html#run>`_ .


Debugging
=========

.. This section does not need filling in by hand as in this case, the content is filled in from strings in the code itself, not in this reST document (see Guidance Doc for details).   

.. - Debugging framework hooks: if there are several debugging parameters, they will be displayed in a table similar to how the  configuration parameters are done, with three columns:

..  - Parameter name
..  - Parameter type
..  - Parameter description

.. `Guidance for the Debugging Section  <instruc_template.forTasks.html#debug>`_ .
    
Examples
========

.. - This should be a self-contained example of using this task that can be tested by any reader.

.. (Since nothing but the procCcd example is currently working in sfp tasks, those aren't very good prototypes currently here.  We eventually need to figure out how to include these in CI, keep them updated, etc., which is a somewhat open q right now.)

.. `Guidance for the Examples Subsection  <instruc_template.forTasks.html#examples>`_ .
   
Algorithm details
====================

.. - Extended description with mathematical details - this will require thinking on what the significant parts  of the algorithm are to be presented.  Mathjax will be implemented  so that the math can be nicely displayed and written in straight tex  (through the **math** directive of reST).

.. `Guidance for the Algorithm Details Section  <instruc_template.forTasks.html#algo>`_ .
