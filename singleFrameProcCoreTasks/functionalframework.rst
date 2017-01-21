..
  _begin: top
   


Functional Framework
========================

Functions that would be called to process single raw CCDs
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- \++ ProcessCCD_ -- Does the  actual steps of how an image is processed from raw data to a science-grade image that can be used in analyses.  Calls the 3 main tasks below.

.. _ProcessCCD: processccd.html

- \+ IsrTask_ - Instrumental Signature Removal (ISR) is a sequence of steps taken to ‘clean’ images of various aspects of defects that any system of optics and detectors will imprint on an image by default. 

.. _IsrTask: isrtask.html
   
- ~ CharImg_ -- Detect and measure bright sources on an exp, repair cosmic rays, measure and subtract background, measure the PSF

.. _CharImg: charimg.html
  
- \+ CalibTask_ -- Run detectAndMeasure subtask on an exp to peform deep detection and measurement, run astrometry subtask to fit an improved WCS, and run photoCal subtask to fit the exposure’s photometric zero-point

.. _CalibTask: calibimg.html

