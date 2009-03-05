#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

import os
import sys

# SETUP
#  Add our library under test to the system path
# ==============================================
here  = os.path.dirname( os.path.abspath( __file__ ) )
thislib = os.path.dirname( here )
sys.path.append( thislib )

# ==============================================
import pypp

import tester as tester
print tester.result.__doc__
tester.some_function();
