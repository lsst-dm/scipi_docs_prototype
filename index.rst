.. LSST DM Stack  documentation master file, created by
   sphinx-quickstart on Tue May 12 10:44:33 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

LSST DM Stack documentation
============================

We want to try to understand how the current DM Stack processes images, showing the steps in an interactive format.


.. From here on in the below we will use the color coding:
 - Green = code or executable to be run 
 - Blue and Cyan = data files to run over
 - Red = Flags
 - Magenta = lines of code


We will take the worked out ci_hsc pkg as an example, and we assume
the user has this installed already, along with the entire DM Stack
for the cmds to work.  For quick pointers on where to go to know how
to do the install, see the first link in the 'Contents' below.

Current Status
--------------

-   astrometry    ---- photoCalTask.py -- DOESN'T RUN properly
-   assembleccd   ---- runAssembleTask.py -- runs fine on old stack; covered at a decent level, needs cleanup
-   calibimg      ---- *calibrateTask.py -- runs fine on old stack - not on new one; needs covering
-   charimg       ---- *calibrateTask.py -- runs fine on old stack - not on new one; needs covering
-   coaddsrcxform ---- no example given
-   diacat         ---- no example given
-   decorrALkernel ---- *This task has no standalone example, however it is applied as a subtask of ImageDifferenceTask  
-   deblendimg     ---- no example given
-   detectcoaddsrcs ---- *The whole example is spelled out in some detail on the doxygen page.
-   dipolemeas     ---- * dipoleMeasTask.py -- has probs, doesn't run through on old or cur stack
-   examplecmdline  ---- *The whole example is on the doxygen page.
-   examplesigmaclippedstats
-   examplesimplestats
-   fittansip     ---- *this is exercised through photoCalTask.py -- which DOESN'T RUN properly
-   forcedmeas     ----  no example given
-   forcedsrcxform ---- no example given
-   imagepsfmatch  ----  *imagePsfMatchTask.py -- runs fine on old stack - and appears to on new one too 
-   ingest
-   installgaussianpsf
-   isrtask        ---- *runIsrTask.py --  runs fine on old stack - not on new one; needs covering
-   loadastrom
-   loadrefobjects
-   measureapcorr
-   measuremergedcoaddsrcs
-   mergedets
-   mergemeasts
-   modelpsfmatch
-   objectsizestarsel
-   processccd  --- on old, immediate prob with setup obs_test: 'Unable to find an acceptable version of obs_test', same for pipe_tasks - but the actual script does run through! ; one listed on the doxygen page works all the way straight through on new code.
-   propvisitflags --- minimal exx on page, but it has some prereqs, doesn't work right off
-   psfmatch --- no code for this, they say to look at the other \*match codes
-   readfitscat --- old stack: the readfitscat code is not in measalg, is it moved..?
-   readtextcat --- old stack: the readtxtcat code is not in measalg, is it moved..?
-   safeclipassemble --- assembleCoadd.py --- ??? this is in the main pipetasks dir, and isn't an exx..?
-   secondmomentstarsel -- None given..
-   singleframemeas --  runSingleFrameTask.py* in measbase - works fine on old, not on new 
-   sourcedet --- measAlgTasks.py in measalg - old doesn't work, new needs afwdata
-   srcxform --- none
-   subtractbkgd ---  subtractBackgroundExample.py in measalg -- doesn't exist in old (??), needs afwdata for new
-   snapcombine --- none
-   snappsfmatch  --- snapPsfMatchTask.py in ipdiffim -- works old and new
-   xform --- none
-   template

Brief description of image processing
--------------------------------------

Image processing is one of the first steps that are undertaken in
analyzing data from a telescope for any purpose, be it astronomical,
astrophysical, or cosmological.  It generally consists of a few
separable steps:

 - Remove image defects in each CCD through ISR
 - Assemble the CCD's together into a large single image
 - Do characterization of the image

We'll now describe each of these steps in more detail.

-----------

Contents:

.. toctree::
   :maxdepth: 2

   install	      
   astrometry   
   assembleccd
   calibimg
   charimg
   coaddsrcxform
   diacat
   decorrALkernel
   deblendimg
   detectcoaddsrcs
   dipolemeas
   examplecmdline
   examplesigmaclippedstats
   examplesimplestats
   fittansip
   forcedmeas
   forcedsrcxform
   imagepsfmatch
   ingest
   install
   installgaussianpsf
   isrtask
   loadastrom
   loadrefobjects
   measureapcorr
   measuremergedcoaddsrcs
   mergedets
   mergemeasts
   modelpsfmatch
   objectsizestarsel
   processccd
   propvisitflags
   psfmatch
   readfitscat
   readtextcat
   safeclipassemble
   secondmomentstarsel
   singleframemeas
   sourcedet
   srcxform
   subtractbkgd
   snapcombine
   snappsfmatch
   xform
   template
