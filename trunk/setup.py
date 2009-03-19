""" pypp: python preprocessor based on the Mako template engine
"""
__author__  = "Jean-Lou Dupont"
__version__ = "0.0.3"
__email__   = "python (at) jldupont.com"

__desc__    = """
Benefits
========

The primary benefit of pypp is improved readability of source code.
Furthermore, the template engine provides powerful macro functionality which helps save keystrokes whilst coding.  

Features
========

* Ease of use: just one import statement
* No additional file to declare nor any change in file extension required
* Once compilation is done, no runtime overhead
* Freshness check: compilation is only performed upon changes to source files
* Based on the Mako_ template engine

Drawbacks
=========

* Increases start-up time
* Some template constructs confuse source code editor syntax highlight functionality 

Changelog
---------
**0.0.3**

* Added 'freshness' check in order to save recompiles
* Removed debug print statements


**0.0.2**

* disabled template caching: (1) pypp is not optimizing start-up time (2) runtime time resources are optimized

**0.0.1** 

Initial alpha release


.. _Mako: http://www.makotemplates.org/
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
