""" pypp: python preprocessor based on the Mako template engine
"""
__author__  = "Jean-Lou Dupont"
__version__ = "0.0.1"
__email__   = "python (at) jldupont.com"

__desc__    = """
Features
========

* Ease of use: just one import statement

* Speed: once compilation is done, no runtime overhead

* Based on the Mako template engine  
"""

__doc_url__ = """http://pypp.googlecode.com/"""

import sys
import os.path
from setuptools import setup, find_packages

__classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

__dependencies = ['mako',]

setup(
    name = "pypp",
    description      = __doc__,
    author_email     = __email__,
    author           = __author__,
    url              = __doc_url__,
    long_description = __desc__,
    version          = __version__,
    package_data     = {'':['*.*']},
    packages         = find_packages(),
    classifiers      = __classifiers,
    install_requires = __dependencies,
    zip_safe         = True,
)
