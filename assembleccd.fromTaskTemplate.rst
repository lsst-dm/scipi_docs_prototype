

AssembleCcdTask.fromTaskTemplate
=========================================

Template For Tasks
====================

TaskName
--------

-     This task assembles sections of an image into a larger mosaic.

- The sub-sections are typically amplifier sections and are to be
    assembled into a detector size pixel grid.  The assembly is driven
    by the entries in the raw amp information.  The task can be
    configured to:

    - return a detector image with non-data (e.g. overscan) pixels
    included.

    - or to renormalize the pixel values to a nominal gain of 1.

    - by default remove exposure metadata that has context in raw
    amps, but not in trimmed detectors.
      

Configuration
----------------

- Document fields in associated config class

- For subtasks, provide list of everything to which this could be retargeted.

Entrypoint
--------

- Link to API page for the "run" method

Butler Inputs
----------------

- Dataset type + description of Butler gets()

- Best effort for now; hopefully auto-doc'd in SuperTask framework

Butler Outputs
----------------

- Dataset type + description of Butler puts()

- Best effort for now; hopefully auto-doc'd in SuperTask framework

Examples
--------

- Self-contained example of using this task that can be tested

Debugging
----------------

- Debugging framework hooks

- Algorithm details

- Extended description with mathematical details
