
AssembleCcdTask
=========================================

- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1ip_1_1isr_1_1assemble_ccd_task_1_1_assemble_ccd_task.html#AssembleCcdTask_

    This task assembles sections of an image into a larger mosaic.  The sub-sections
    are typically amplifier sections and are to be assembled into a detector size pixel grid.
    The assembly is driven by the entries in the raw amp information.  The task can be configured
    to return a detector image with non-data (e.g. overscan) pixels included.  The task can also 
    renormalize the pixel values to a nominal gain of 1.  The task also removes exposure metadata that 
    has context in raw amps, but not in trimmed detectors.

    
How to call with options/flags
++++++++++++++++++++++++++++++

Debugging
+++++++++ 

The command line task interface supports a flag -d to import debug.py from your PYTHONPATH; see Using lsstDebug to control debugging output for more about debug.py files.

The available variables in AssembleCcdTask are:

- display -- A dictionary containing debug point names as keys with frame number as value. Valid keys are:

- assembledExposure -- display assembled exposure

Examples
++++++++

This code is in runAssembleTask.py in the examples subdir (of $IP_ISR_DIR).

(It runs fully successfully on the 4/2016 stack.)

Specific functions of class
+++++++++++++++++++++++++++

assembleCcd
-----------

Assemble a set of amps into a single CCD size image.

postprocessExposure
-------------------

Set exposure non-image attributes, including wcs and metadata and display exposure (if requested)

setGain
-------

Renormalize, if requested, and set gain metadata

setWcs
------

Set output WCS = input WCS, adjusted as required for datasecs not starting at lower left corner


What it returns
+++++++++++++++

assembledCcd – An *lsst.afw.image.Exposure* of the assembled amp sections.
