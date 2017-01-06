# LSST Data Management System
# Copyright 2008-2017 AURA/LSST.
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
# MSSG
# 1-5-2017

'''
This code does a *very* basic parsing of the config args in a file (hardwired right now for isrTask.py) and puts them into a rst form to be then built into a docs page
'''

import string

# Hardcoded to my local path currently
path='/Users/m/fizzAndAstro/lsst/otherLSSTGithubPkgs/scipi_docs_prototype/'

# Read the whole file just into one str
pyfile = open(path + 'exxampleCodes/isrTask.py', 'r').read()

# Split on the stuff right after the var name for the simple pexConfig.Field vars (which is not all, but the majority of the config vars for this code)
lines = pyfile.split('.Field(') 

# print len(lines)

# Now loop over all the lines
for l in range(0,len(lines)-1):
    line1=lines[l].split() # Split the specific line on the blank spaces in it, this becomes a list of strings
    ll1=len(line1)         # Assign into a temp var
    templine2=lines[l+1].split('Field(') # This is in case there is another var after the current one that is not a pexConfig.Field var, since we'll need the end of the current variable field
    line2=templine2[0].split() # Now assign the first field of the above split line into another list
    ll2 = len(line2)
    
# In order, we'll print:
#    -  var name
#    - var type,
#    - default val
#    - descrip of var

    varname =  "``" + line1[ll1-3] + "``"  # The varname will be in the first string, 3 spots from the end

    vartype = ' -- ( `' + line2[2].strip(',') + '`) -- '  # Its type will be the second spot in the second string

    defaultval = ' defaults to `' + line2[ll2-5].strip(',') + '` - '  # Default val will be 5 spots from end in the second string

    descrip = lines[l+1].split('doc')[1].split(',')[0].strip('"').strip(' = "')  # To extract the piece that is the description field requires some  further processing of splits and strips

    print (varname + vartype + defaultval + descrip)
    
#    print( "``" + line1[ll1-3] + "``" + str(' -- ( `' + line2[2].strip(',') +'`) -- ' ) + ' defaults to `' + line2[ll2-5].strip(',') + '` - ' + descrip)

 

