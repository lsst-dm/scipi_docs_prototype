#!/usr/bin/env python
"""Sphinx configurations to build package documentation."""

from documenteer.sphinxconfig.stackconf import build_package_configs

#import lsst.validate.base


_g = globals()
_g.update(build_package_configs(
    project_name='Sci-Pipelines-Prototype',
    copyright='2017 Association of Universities for '
              'Research in Astronomy, Inc.',
    version="0.1",
    doxygen_xml_dirname=None))

intersphinx_mapping['astropy'] = ('http://docs.astropy.org/en/stable', None)

html_static_path = []

# DEBUG only
automodsumm_writereprocessed = False

exclude_patterns += ['src']

del intersphinx_mapping['scipy']
del intersphinx_mapping['numpy']
