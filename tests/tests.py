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
oneup = os.path.dirname( here )
thislib = os.path.join( oneup, 'pypp' )
sys.path.append( thislib )

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    #import doctest
    #doctest.testmod()
    print here
    print oneup
    print thislib
