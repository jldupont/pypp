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
    __slots__ = ['_processed', '_loader']
    
    def __init__(self):
        self._loader = None
        self._processed = {}
    
    def handle_import_module(self, name, rpath, path, file, desc, global_scope):
        """
        """
        #paranoia
        if (name in self._processed):
            return None
        
        self._processed[name] = path
        print "handle_import_module: name(%s) rpath(%s)" % (name, rpath)
    
        try:
            return self._loader(name, file, rpath, desc, global_scope)
        except ImportError:
            pass #pass-through
        
        return None

    def processed(self):
        for i in self._processed:
            yield i
        