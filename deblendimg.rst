
SourceDeblendTask
===================


- `Doxygen link`_
.. _Doxygen link: https://lsst-web.ncsa.illinois.edu/doxygen/x_masterDoxyDoc/classlsst_1_1meas_1_1deblender_1_1deblend_1_1_source_deblend_task.html#SourceDeblendTask_


Debugging
+++++++++ 

Specific functions of class
+++++++++++++++++++++++++++


deblend
-------

This is the key function in which the deblending is done.  It takes
the exposure, and the src catalog as has been output by
e.g. processCcd, as those are the two primary things it will need to
figure out which srcs are overlapping.

There is another special import done here that calls the actual
deblend function from the same dir where this class lives
(*lsst.meas.deblender*).  As the algorithm that is to be used for
deblending is currently still being developed and has not been settled
upon, it can be swapped in and out at this point without affecting the
rest of the structure of the deblending.

In the end, the srcs catalog is modified in place to separately
contain all deblended objects.

[**Internals**:

The first step of this function is to start a loop over all the
objects in the srcs catalog.  Inside the loop, the footprint for this
src is extracted, and number of peaks inside the current source is
checked.  If it's zero or unity, we pop out of this loop because of
course this just means there is at most one identified object in this
src, and nothing is thus overlapping.  [But what does zero peaks mean..?]

If the footprint of the given source is very large beyond a preset
value, then deblending of this source will be skipped.  'Large' is
defined by thresholds on the area, size and axis ratio.  This test is
principally intended to get rid of satellite streaks, which the
deblender or other downstream processing can have trouble dealing with
(e.g., trying to deblend multiple large srcs can chew up memory).

If the footprint is masked out, we also pop out of the loop, since we do
not analyze masked areas.

Now we try to actually deblend this source by sending it, along with
the footprint, PSF, and a number of config params to the deblend
algorithm.  If it works, we put the entire result into a variable
(*res*), but if not, we'll raise an error depending or pop out of the
loop depending on whether a certain flag (*deblendFailedKey*) is set.

We then go through the whole set of children that have been deblended,
and properly set the footprint for each of these, which can be an
involved process to not overlap any pixels etc. [is that what the long
kids loop does?]  ]



Examples
++++++++

None given.
