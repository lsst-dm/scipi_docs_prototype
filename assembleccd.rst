
###############
AssembleCcdTask
###############

This task assembles sections of an image into a larger mosaic.

The sub-sections are typically amplifier sections and are to be
assembled into a detector size pixel grid.  The assembly is driven by
the entries in the raw amp information.  The task can be configured
to:

    - return a detector image with non-data (e.g. overscan) pixels included.

    - renormalize the pixel values to a nominal gain of 1.

    - by default remove exposure metadata that has context in raw amps, but not in trimmed detectors.

    
Methods
=======
    
- ``lsst.ip.isr.assembleCcdTask.assembleCcd`` - Assemble a set of amps into a single CCD size image.

- ``lsst.ip.isr.assembleCcdTask.postprocessExposure`` - Set exposure non-image attributes, including wcs and metadata and display exposure (if requested)

- ``lsst.ip.isr.assembleCcdTask.setWcs`` - Set output WCS equal to input WCS, adjusted as required for datasecs not starting at lower left corner 

- ``lsst.ip.isr.assembleCcdTask.setGain`` - Renormalize, if requested, and set gain metadata
  
Configuration
=============

- ``setGain`` (`bool`) - Whether to set the gain , default is `True`.

- ``doRenorm`` (`bool`) -
    Whether to renormalize to a gain of unity
    (ignored if ``setGain`` is False).  Setting to `True` gives 1 ADU
    per electron. However, setting to `True` is not recommended for
    mosaic cameras because it breaks normalization across the focal
    plane. However, if the CCDs are sufficiently flat then the
    resulting error may be acceptable.  Default is `False`.

- ``doTrim`` (`bool`) - Whether to trim out non-data regions, default is `True`.

- ``keysToRemove`` (`str`) - FITS headers to remove
  (in addition to ``DATASEC``, ``BIASSEC``, ``TRIMSEC`` and perhaps ``GAIN``).  Default is an empty string.

Entrypoint
==========

``AssembleCcdTask.assembleCcd`` - Does the actual assembly.


Examples
========

This code is in ``runAssembleTask.py`` in the examples directory.
  

Debugging
=========

``display`` -  A dictionary containing debug point names as keys with frame number as value. The only valid key is:
``assembledExposure`` (to display assembled exposure)

