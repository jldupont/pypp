""" EGG setup

    @author: Jean-Lou Dupont
"""
_DEBUG = False

import sys
import os.path
from setuptools import setup, find_packages

_packages = ['jld',
             'jld.api', 
            'jld.backup', 
            'jld.cmd', 
            'jld.cmd_g2',
            'jld.cmd_g2.transmission',
            'jld.registry',
            'jld.template',  
            'jld.tools'
            ]

_scripts = [ 
            'jld/backup/scripts/mm.py',
            'jld/backup/scripts/mm.bat', 
            'jld/backup/scripts/mm',
            
            'jld/backup/scripts/dlc.py',
            'jld/backup/scripts/dlc.bat', 
            'jld/backup/scripts/dlc',
            
            'jld/backup/scripts/glf.py',
            'jld/backup/scripts/glf.bat', 
            'jld/backup/scripts/glf', 
            
            'jld/cmd/pypre.py',
            
            'jld/scripts/trns.py',            
            ]

if (not _DEBUG):
    setup(
        name = "jld",
        description      = jld.__desc__,
        author_email     = jld.__email__,
        author           = jld.__author__,
        url              = jld.__doc_url__,
        long_description = jld.__long_desc__,
        version          = jld.__version__,
        package_data     = {'':['*.*']},
        packages         = _packages,
        scripts          = _scripts,
        classifiers      = jld.__classifiers__,
        install_requires = _dependencies,
        zip_safe         = False,
    )

import shutil

# Copy to tags directory
if (not _DEBUG):
    print 'copying to tags directory'
    shutil.copy(source_egg_path, dest_egg_path)
