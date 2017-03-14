:orphan: true
	 
.. Based on:
   https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with
   learnings from the 4 sfp pages built in branch DM-8717

Please fill in the below sections with the contents as described in
the reST comments, removing the comments as you do so, and using the
links to locations in the `Guidance Document
<writing-task-topics.html>`_ if needed.


########################
Structure of ExampleTask 
########################

.. Fill in introductory material here - this section needs the following:

.. - Summary/context (1-2 sentences).

.. - Concise summary of logic/algorithm in a paragaph and/or bullet list.

.. - A sentence about each step, which can be either:

..  a) A retargetable subtask

..  b) A method within a task.

`Guidance for the Introduction Section  <writing-task-topics.html#task-topics-intro>`_ .


.. - Insert Module Membership here:

..  This section needs only the module the task is implemented inside of.

`Guidance for the Module Membership Section  <writing-task-topics.html#task-topics-module>`_ .

.. Insert material for the SeeAlso Box here:
  
..   -  Things inside the `seealso` directive box need to link to related content, such as:
  
         - Tasks that commonly use this task (this helps a reader
           landing on a subtask’s page find the appropriate driver
           task).
     
         - Tasks that can be used instead of this task (to link families of subtasks).
   
         - Pages in the **Processing** and **Frameworks** sections of
           the Science Pipelines documentation.
  
         - The API Usage page for this Task
     
`Guidance for the See Also Section  <writing-task-topics.html#task-topics-seealso>`_ .

    
Configuration
=============

.. - This section will be autofilled -- it describes the task’s
   configurations defined in the task class’s associated configuration
   class.  It will be split into 2 natural subsections, as below.

Retargetable Subtasks
---------------------

.. This section will be autofilled also -- the content is filled in
   from docstrings in the code itself, not in this reST document (see
   Guidance Doc for details).

.. - For these subtasks, a table will be shown with 3 columns:

..  - Subtask name
..  - Default target
..  - Description of what it does

`Details about the Retargetable Subtasks Subsection  <writing-task-topics.html#task-topics-retarg>`_ .
   
Parameters
----------

.. This section will be autofilled also -- the content is filled in
   from docstrings in the code itself, not in this reST document (see
   Guidance Doc for details).

.. Here, configuration parameters will be displayed in a table with the following fields:

.. - Parameter name.

.. - Parameter type.  These are generally simple python var types
   (i.e. `bool`, `int`, `float`, or `str`) , which will automatically
   be linked to existing python documentation on these types)

.. - Default value of parameter.

.. - A description sentence or paragraph. 

`Details about the Parameters Subsection  <writing-task-topics.html#task-topics-params>`_ .

Python usage
============

Class initialization
--------------------

..  This section will be autofilled also -- the content is filled in
    from docstrings in the code itself, not in this reST document (see
    Guidance Doc for details).

.. This section consists of:

.. - Interface for declaring an instance of the class
  
.. - Description of the parameters in the interface signature

`Details about the Class initialization Subsection  <writing-task-topics.html#task-topics-initzn>`_ .

Run method
----------

.. This section will be autofilled also -- the content is filled in
   from docstrings in the code itself, not in this reST document (see
   Guidance Doc for details).

.. This will consist of:

.. - A description of the interface for calling the primary entrypoint
   function for the class -- again, this will be picked up
   automatically from the interface of the `run` method and will not
   require developer input.

.. - A short description of what the `run` method requires as required and optional inputs

.. - Description of the parameters in the run signature

`Details about the Run Method Subsection  <writing-task-topics.html#task-topics-run>`_ .


Debugging
=========

.. This section will be autofilled also -- the content is filled in
   from docstrings in the code itself, not in this reST document (see
   Guidance Doc for details).

.. - Debugging framework hooks: if there are several debugging
   parameters, they will be displayed in a table similar to how the
   configuration parameters are done, with three columns:

..  - Parameter name
..  - Parameter type
..  - Parameter description

`Details about the Debugging Section  <writing-task-topics.html#task-topics-debug>`_ .
    
Examples
========

.. - Fill in a self-contained example of using this task that can be tested by any reader.

`Guidance for the Examples Subsection  <writing-task-topics.html#task-topics-examples>`_ .
   
Algorithm details
====================

.. - Fill in an extended description with mathematical details - this
   will require thinking on what the significant parts of the
   algorithm are to be presented.  Mathjax will be implemented so that
   the math can be nicely displayed and written in straight Latex
   (through the **math** directive of reST).

`Guidance for the Algorithm Details Section  <writing-task-topics.html#task-topics-algorithm>`_ .
