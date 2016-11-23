# mssg changes -- start: 11/16/2016

from lsst.ip.isr import AssembleCcdTask
# import assembleCcdTask_fromIP_ISR_4_2016
import lsst.afw.display.ds9 as ds9
import exampleUtils_fromIsrExamplesDir
import sys # mssg

def runAssembler():
    '''Run the task to assemble amps into a ccd'''

    #Create the assemble task with default config
    assembleConfig = AssembleCcdTask.ConfigClass()
 #   assembleConfig = AssembleCcdTask.ConfigClass(keysToRemove="exxkey",setGain=False) #mssg tests
    print " *********** In runAssembler: assembleConfig = ", assembleConfig # mssg
    assembleTask = AssembleCcdTask(config=assembleConfig)  # MG: Their version
#    assembleTask = AssembleCcdTask()                        # This works, too
    frame = 0

    #The assemble task can operate in two ways:
    #1. On a dictionary of amp size images
    #2. On a single amp mosaic image
    #Both methods should produce the same output.
    for isPerAmp in (True, False):
        print "\n\n &&&& isPerAmp = ", isPerAmp
        print " \n ******************************** About to call exampleUtils_fromIsrExamplesDir.makeAssemblyInput(isPerAmp)"
        assemblyInput = exampleUtils_fromIsrExamplesDir.makeAssemblyInput(isPerAmp)
        print " \n *** Back in runAssembler, isPerAmp = ", isPerAmp
        print " assemblyInput = ", assemblyInput
        print " \n ******** About to call assembleTask.assembleCcd(assemblyInput) " 
        ##### mssg: Getting a sense for what assemblyInput is, and probing values
        if (isPerAmp == True):
            ai = assemblyInput
            print type(assemblyInput)
            skeys = sorted(assemblyInput.keys())
            print type(skeys), skeys
            print type(skeys[0])
            print ai['A:0,0']    
        ###### sys.exit()
        assembledExposure = assembleTask.assembleCcd(assemblyInput)
        ae = assembledExposure
        print " \n *** assembledExposure = ", assembledExposure
        aemi = assembledExposure.getMaskedImage()
#        ds9.mtv(aemi, frame=frame, title="Per amp input is %s"%(isPerAmp))
#        ds9.mtv(ae, frame=frame, title=" non-masked -- Per amp input is %s"%(isPerAmp))  # mssg - i found nothing dif in the two ds9 displays

        print " \n ************* assembledExposure.getMaskedImage() = ", assembledExposure.getMaskedImage()

        frame += 1
        print "\n framecounter = ", frame
#        sys.exit()
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Demonstrate the use of AssembleCcdTask")
    parser.add_argument('--debug', '-d', action="store_true", help="Load debug.py?", default=False)
    args = parser.parse_args()

    print " \n\n *********** args = ", args
    if args.debug:
        print " ****** Importing debugger"
        try:
            import debug
        except ImportError as e:
            print >> sys.stderr, e
    print " ****** About to call runAssembler"        
    runAssembler()
    print " >>>>>>>>>>>>>>>>>> Done out over"
