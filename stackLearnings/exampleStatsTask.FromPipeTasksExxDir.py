#!/usr/bin/env python

# With a few changes by MSSG, 4/2017

#
# LSST Data Management System
# Copyright 2014 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
from __future__ import print_function
import os
import sys

import lsst.utils
from lsst.afw.image import MaskedImageF
from lsst.pipe.tasks.exampleStatsTasks import ExampleSimpleStatsTask, ExampleSigmaClippedStatsTask

# Parse command-line arguments. If the user supplies an image, use it;
# otherwise use one from the afwdata package (or complain if afwdata is not setup).
if len(sys.argv) < 2:
#    afwDataDir = lsst.utils.getPackageDir('afwdata') -- mg: all these give errors
#    print("  afwDataDir = ", afwDataDir)
#    maskedImagePath = os.path.join(afwDataDir, "data", "med.fits")

    maskedImagePath="/Users/m/fizzAndAstro/lsst/lsstsw/build/afwdata/CFHT/D4/cal-53535-i-797722_1.fits"

else:
    maskedImagePath = sys.argv[1]
    print("File = ", sys.argv[1])  # mg
    
print("\n\n\n ************ Computing statistics on %r\n" % (maskedImagePath,))



# Read the masked image from the specified file. The file may be a masked image or exposure,
# but if the file is a simple image, with no mask or variance plane, then this call will fail.
maskedImage = MaskedImageF(maskedImagePath)

# Construct the simple stats task configuration and use that to construct and run the task
print("running ExampleSimpleStatsTask")
config1 = ExampleSimpleStatsTask.ConfigClass()
config1 = ExampleSigmaClippedStatsTask.ConfigClass(numSigmaClip=1, numIter=1)

# print(" config1.numSigmaClip = ",  config1.numSigmaClip )

print(" config1 = ",  config1)


# ...modify the config if desired...


config1.validate()  # check that the config parameters are valid; optional, but catches errors early
print(" \n Config1 is good \n" )

task1 = ExampleSimpleStatsTask(config=config1)


res1 = task1.run(maskedImage)
print("result  =", res1)
print()
# Orig results:  simple mean=62.12; meanErr=0.22; stdDev=55.41;



# Construct the sigma-clipped stats task configuration and use that to construct and run the task
print("running ExampleSigmaClippedStatsTask")
config2 = ExampleSigmaClippedStatsTask.ConfigClass()
# ...modify the config if desired...
config2.validate()
task2a = ExampleSigmaClippedStatsTask(config=config1)
res2a = task2a.run(maskedImage)

task2b = ExampleSigmaClippedStatsTask(config=config2)
res2b = task2b.run(maskedImage)
print("result2a  =", res2a, "\n\n\n")
print("result2b  =", res2b, "\n\n\n")


# Orig results: exampleSigmaClippedStats: clipped mean=59.08; meanErr=0.03; stdDev=6.87; 
