

AssembleCcdTask.fromTaskTemplate
================================

AssembleCcdTask
---------------

This task assembles sections of an image into a larger mosaic.

The sub-sections are typically amplifier sections and are to be
    assembled into a detector size pixel grid.  The assembly is driven
    by the entries in the raw amp information.  The task can be
    configured to:

    - return a detector image with non-data (e.g. overscan) pixels
    included.

    - or to renormalize the pixel values to a nominal gain of 1.

    - by default remove exposure metadata that has context in raw
    amps, but not in trimmed detectors.

[ link to methods API pages -- fill in in a narrative sort of way, make links to all the dif methods]

Configuration
-------------

- ``setGain`` (`bool`) - Set the gain , default is `True`.

- ``doRenorm`` 

- ``keysToRemove`` (`str`) - FITS headers to remove (in addition to ``DATASEC``, ``BIASSEC``, ``TRIMSEC`` and perhaps ``GAIN``)

- Document fields in associated config class

- For subtasks, provide list of everything to which this could be retargeted.

Entrypoint
----------

`AssembleCcdTask.assembleCcd` 


Examples
--------

- Self-contained example of using this task that can be tested

Debugging
----------------

``display`` -  A dictionary containing debug point names as keys with frame number as value. Valid keys are:
assembledExposure

display assembled exposure

- Debugging framework hooks

- Algorithm details

- Extended description with mathematical details
