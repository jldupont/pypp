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

from preprocessor import Tpl

class Controller(object):
    """
    """
    __slots__ = ['_processed', '_loader']
    
    def __init__(self):
        
        #load class
        self._loader = None
        self._processed = {}
    
    def handle_import_module(self, name, rpath, path, file, desc, global_scope):
        """
        """
        #paranoia
        if (name in self._processed):
            return None
        
        self._processed[name] = path
        #print "handle_import_module: name(%s) rpath(%s)" % (name, rpath)
    
        #Perform the preprocessing
        if (file):
            processed_file = self.preprocessModule(name, file)
        else:
            processed_file = self.preprocessPackage(name, path)
    
        #Finally load
        try:
            return self._loader(name, processed_file, rpath, desc, global_scope)
        except ImportError:
            pass #pass-through
        
        return None

    def preprocessModule(self, name, file):
        """
        """
        #get rid of originating file because
        # we will anyway generate a new one
        path = file.name
        file.close()
        print "Controller.preprocessModule: name(%s)" % name
        return self._preprocessFile(path)
        

    def preprocessPackage(self, name, path):
        """
        """
        print "Controller.preprocessPackage: name(%s)" % name
        return self._preprocessFile(path)


    def _preprocessFile(self, path):
        """
        """

        try:
            rendered = Tpl( path )
        except:
            return None
        
        
        

    def processed(self):
        for i in self._processed:
            yield i
        