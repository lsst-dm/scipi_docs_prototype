
DiaCatalogSourceSelectorTask
=============================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1diffim_1_1dia_catalog_source_selector_1_1_dia_catalog_source_selector_task.html#DiaCatalogSourceSelectorTask_


A naive star selector based on second moments. Use with caution.

[Yes, that's it, on the doxygen page.]

How to call with options/flags
++++++++++++++++++++++++++++++

Like all star selectors, the main method is run.


Debugging
+++++++++ 

DiaCatalogSourceSelectorTask has a debug dictionary with the following keys:

- display -- bool; if True display debug information

- displayExposure -- bool; if True display exposure

- pauseAtEnd -- bool; if True wait after displaying everything and wait for user input

Specific functions of class
+++++++++++++++++++++++++++

selectStars	
----------------

Returns: an *lsst.pipe.base.Struct* containing:

- starCat  a list of sources to be used as kernel candidates

Examples
++++++++

None given.

What it returns
+++++++++++++++

