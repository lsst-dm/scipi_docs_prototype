.. Based on:
   https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with
   learnings from the 4 sfp pages built in branch DM-8717

.. Please fill in the below sections with the contents as described in
   the reST comments, removing the comments as you do so, and using the
   links to locations in the `Guidance Document
   <writing-task-topics.html>`_ if needed.


.. The title of the page should be the name of the Task class (ProcessCcdTask, for example).
.. Also, update the section anchor below to have the same name.
.. See tbd URL (e.g. https://developer.lsst.io/writing/user-guides/task-topics.html#title) for details.


.. _TaskClassName:

#############
TaskClassName
#############

.. Fill in introductory material here - this section needs the following:
.. - Summary/context (1-2 sentences).
.. - Concise summary of logic/algorithm in a paragaph and/or bullet list.
.. - A sentence about each step, which can be either:
..  a) A retargetable subtask
..  b) A method within a task.
.. `Guidance for the Introduction Section  <writing-task-topics.html#task-topics-intro>`_ .

.. - Insert Module Membership here:
.. This component simply mentions and links to the task's parent module.
.. Modify the module-anchor in the ref to point to the module page.
.. `Guidance for the Module Membership Section  <writing-task-topics.html#task-topics-module>`_ .

This task is implemented in the :ref:`module-anchor` module.


.. SeeAlso Box:
..   -  Things inside the `SeeAlso` Directive Box need to link to related content, such as:  
         - Tasks that commonly use this task (this helps a reader
           landing on a subtask’s page find the appropriate driver
           task).     
         - Tasks that can be used instead of this task (to link families of subtasks).   
         - Pages in the **Processing** and **Frameworks** sections of
           the Science Pipelines documentation.  
         - The API Usage page for this Task     
.. `Guidance for the See Also Section  <writing-task-topics.html#task-topics-seealso>`_ .

.. seealso::
.. Insert material for the SeeAlso Box here  

.. For the anchor below and all similar ones below, replace
   "TaskClassName" with the actual name of the Task you are
   documenting.
   
.. _TaskClassName-config:
      
Configuration
=============

.. - This section will be autofilled and requires no input. (It describes the task’s
   configurations defined in the task class’s associated configuration
   class, split into 2 subsections, Retargetable Subtasks, and Parameters.)
.. `Details about the Configuration Subsection  <writing-task-topics.html#task-topics-config>`_ .


.. _TaskClassName-python-usage:
   
Python usage
============

.. _TaskClassName-class-init:

Class initialization
--------------------

..  This section will be autofilled also -- the content is filled in
    from docstrings in the code itself, not in this reST document (see
    Guidance Doc for details).
.. This section consists of:
.. - Interface for declaring an instance of the class
.. - Description of the parameters in the interface signature
.. `Details about the Class initialization Subsection  <writing-task-topics.html#task-topics-init>`_ .

.. _TaskClassName-run:
   
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
.. `Details about the Run Method Subsection  <writing-task-topics.html#task-topics-run>`_ .

.. _TaskClassName-debugging:

Debugging
=========

.. This section will be autofilled also.
.. `Details about the Debugging Section  <writing-task-topics.html#task-topics-debug>`_ .


.. _TaskClassName-examples:

Examples
========

.. - Fill in a self-contained example of using this task that can be tested by any reader.
.. `Guidance for the Examples Subsection  <writing-task-topics.html#task-topics-examples>`_ .

.. _TaskClassName-algorithm:
   
Algorithm details
=================

.. - Fill in an extended description with mathematical details - this
   will require thinking on what the significant parts of the
   algorithm are to be presented.  Mathjax will be implemented so that
   the math can be nicely displayed and written in straight Latex
   (through the **math** directive of reST).

.. `Guidance for the Algorithm Details Section  <writing-task-topics.html#task-topics-algorithm>`_ .
