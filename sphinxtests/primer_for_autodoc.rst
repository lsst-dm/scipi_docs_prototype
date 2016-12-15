
Primer for doc
========================

Basic syntax for autodoc
--------------------------

- So when you put the directive:

".. automodule:: python_codename" at the start of a line, followed by any or all of these, indented:

   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

.

- Now in the python files themselves, all classes inside a file will be extracted to the highest level heading

.

- From here, all the functions are extracted out into subheadings (and their args may not be shown if the function is preceded by a decorator)

.

- Inside, standard function descriptions are set off by the standard
  triple-quote docstring delimiters, and Parameters and Returns will
  be special keywords that have lists underneath them (and Return-type
  will be picked up automatically from how Returns is described)

.
  
- Single backquotes here will signify italics, double backquotes will be rendered in red text.
  
.

- Extra formatting like tables, or directives like ``See also``, ``Notes``, ``Warnings`` or links to other pages can also be inserted as normal (for this, see the tstcode info)


  
  
Doctests
--------

To test the example code inside a docstring from the cmd line and see
the output do:

  py tstcode -v
