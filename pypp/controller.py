#!/usr/bin/env python
""" Controller class
    project: pypp
    
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['Controller']

import os
import sys

class Controller(object):
    """
    """
    __slots__ = ['_processed']
    
    def __init__(self):
        self._processed = {}
    
    def handle_import_module(self, name, path):
        """
        """
        #paranoia
        if (name in self._processed):
            return None
        
        self._processed[name] = path
        print "handle_import_module: name(%s) path(%s)" % (name, path)
        return None

    def processed(self):
        for i in self._processed:
            yield i
        