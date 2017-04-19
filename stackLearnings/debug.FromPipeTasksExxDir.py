import lsstDebug
def DebugInfo(name):
    di = lsstDebug.getInfo(name)
    if name == "lsst.ip.isrFunctions.isrTask":
        di.display = {'postISRCCD':2}
        #di.display = True


    if name == "lsst.pipe.tasks.characterizeImage":
        di.display = dict(
            repair = True,
        )


    if name == "lsst.pipe.tasks.calibrate":
        di.display = dict(
            calibrate = 1,
        )
    
    return di
lsstDebug.Info = DebugInfo
