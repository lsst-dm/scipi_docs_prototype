.. Based on:
   https://dmtn-030.lsst.io/v/DM-7096/index.html#task-topic-type, with
   learnings from the 4 sfp pages built in branch DM-8717

.. Please fill in the below sections with the contents as described in
   the reST comments, removing the comments as you do so, and using the
   links to locations in the "Guidance Document"
   <writing-task-topics.html> if needed.


.. The title of the page should be the name of the Task class (ProcessCcdTask, for example).
.. Also, update the section anchor below to have the same name.
.. See tbd URL (e.g. https://developer.lsst.io/writing/user-guides/task-topics.html#title) for details.
.. Guidance for Titling the page:  <writing-task-topics.html#task-topics-title> 

.. _TaskClassName:

#############
TaskClassName
#############

.. For the anchor below and all similar ones below, replace
   "TaskClassName" with the actual name of the Task you are
   documenting.
   
     
.. Introductory material:
.. Fill in introductory material here, which will consist of the following sections:

.. Summary/context section
.. Give summary/context of what the task does and is for (1-2 sentences)
.. Guidance for the Summary/context Section:  <writing-task-topics.html#task-topics-summary> .
.. _TaskClassName-summary:
   
.. Summary of logic/algorithm section
.. - This should be a concise summary of task's logic/algorithm in a paragaph and/or bullet list.
.. - A sentence about each step, which can be either:
..  a) A retargetable subtask
..  b) A method within a task.
.. Guidance for the Summary of logic Section:  <writing-task-topics.html#task-topics-logic>.
.. _TaskClassName-logic:

   
.. Module membership section
.. This component simply mentions and links to the task's parent module.
.. Modify the module-anchor in the ref to point to the module page.
.. Guidance for the Module Membership Section:  <writing-task-topics.html#task-topics-module> .
.. _TaskClassName-modulemembership:

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

.. Guidance for the See Also Box:  <writing-task-topics.html#task-topics-seealso>.
.. _TaskClassName-seealso:

.. seealso::
.. Insert material for the SeeAlso Box here  

   
.. Configuration Section
.. This section will be autofilled.   
.. Details about the Configuration Subsection:  <writing-task-topics.html#task-topics-config> .
.. _TaskClassName-config:


   
.. Python usage Section
.. This section will be autofilled also.
.. _TaskClassName-python-usage:   

.. Class initialization Section
.. This section will be autofilled also.
.. Guidance for the Class initialization Subsection  <writing-task-topics.html#task-topics-init> .
.. _TaskClassName-class-init:
   
.. Run method Section
.. This section will be autofilled also.
.. Guidance for the Run Method Subsection  <writing-task-topics.html#task-topics-run> .
.. _TaskClassName-run:



.. Debugging Section
.. This section will be autofilled also.
.. Details about the Debugging Section  <writing-task-topics.html#task-topics-debug> .
.. _TaskClassName-debugging:

.. Examples Section   
.. - Fill in a self-contained example of using this task that can be tested by any reader.
.. See:  writing-task-topics.html#task-topics-examples
.. _TaskClassName-examples:


   
.. Algorithm details Section
.. - Fill in an extended description with mathematical details - this
   will require thinking on what the significant parts of the
   algorithm are to be presented.  Mathjax will be implemented so that
   the math can be nicely displayed and written in straight Latex
   (through the **math** directive of reST).

.. Guidance for the Algorithm Details Section  <writing-task-topics.html#task-topics-algorithm> .
.. _TaskClassName-algorithm:   
