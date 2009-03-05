#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

#.pypp

#<%def name="var()">some variable</%def>

def result():
    """
    ${var()}
    """

#<%include file="include.py" />

#<%def name="some_var()">print "This will appear at the beginning"</%def>

#${some_var()}


