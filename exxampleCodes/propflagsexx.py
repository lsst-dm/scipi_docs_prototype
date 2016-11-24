# Requires:
# * butler: data butler, for retrieving the CCD catalogs
# * coaddCatalog: catalog of source measurements on the coadd (lsst.afw.table.SourceCatalog)
# * coaddExposure: coadd (lsst.afw.image.Exposure)
from lsst.pipe.tasks.propagateVisitFlags import PropagateVisitFlagsTask, PropagateVisitFlagsConfig
config = PropagateVisitFlagsConfig()
config.flags["calib.psf.used"] = 0.3 # Relative threshold for this flag
config.matchRadius = 0.5 # Matching radius in arcsec
task = PropagateVisitFlagsTask(coaddCatalog.schema, config=config)
ccdInputs = task.getCcdInputs(coaddExposure)
task.run(butler, coaddCatalog, ccdInputs, coaddExposure.getWcs())
