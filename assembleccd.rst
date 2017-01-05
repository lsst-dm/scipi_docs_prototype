
###############
AssembleCcdTask
###############

This task assembles sections of an image (e.g. typically
amplifier-defined sub-images) into a larger mosaic.

The sub-sections are most often amplifier sections and are to be
assembled into a detector size pixel grid.  See below for details.

This task is implemented in the ``lsst.ip.isr`` module.

.. seealso::

   This is called once the single-amplifier subimages are processed,
   and the whole CCD image needs to be assembled.
  
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

- ``lsst.ip.isr.assembleCcdTask.assembleCcd``

Butler Inputs
=============

Butler Outputs
==============

Examples
========

The example code is ``runAssembleTask.py`` in the examples directory.
What it does is set up the configuration for the task (in this case
with all the defaults), then invoke the assembly task itself with this
configuration assigning this to the object `assembleTask`.  It then
shows how the assembly is done in two situations, on a dictionary of
amp size images, and then on a single amp mosaic image.  It prepares
the input to the task in each of these situations, then runs the
primary ``lsst.ip.isr.assembleCcdTask.assembleCcd`` method of this
task on the `assembleTask` object.  Then by default it calls the
viewer to show the result to the screen.
  

Debugging
=========

- ``display`` -  A dictionary containing debug point names as keys with frame number as value. The only valid key is:
``assembledExposure`` (to display assembled exposure)

Algorithm details
====================

In more detail: The sub-sections are most often amplifier sections and are to be
assembled into a detector size pixel grid.  This is done overall by
calling the ``lsst.ip.isr.assembleCcdTask.assembleCcd`` method.

As a part of the running of this primary method, other task methods may be called, such as ``lsst.ip.isr.assembleCcdTask.setGain`` which will renormalize the
gain across the amps, if requested, and set gain metadata,
``lsst.ip.isr.assembleCcdTask.setWcs``, which will set output WCS
equal to input WCS (adjusted as required for the image coordinates
(i.e. FITS header keyword datasecs) not starting at lower left corner,
and ``lsst.ip.isr.assembleCcdTask.postprocessExposure``, which will
set exposure non-image attributes, including WCS and metadata and
display exposure (if requested).

The assembly is driven by the entries in the raw amp information.  The
task can be configured to:

    - return a detector image with non-data (e.g. overscan) pixels included.

    - renormalize the pixel values to a nominal gain of 1.

    - by default remove exposure metadata that has context in raw amps, but not in trimmed detectors.

