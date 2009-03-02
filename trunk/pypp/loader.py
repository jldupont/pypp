#!/usr/bin/env python
""" Module Loader class
    project: pypp
    
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['Loader']

import imp
import sys

class Loader(object):
    """ Loads a .pypp file in place of the usual .py
    """
    def __init__(self, name, file, pathname, desc, scope):
        self.file = file
        self.name = name
        self.pathname = pathname
        self.desc = desc
        self.scope = scope

    def load_module(self, fullname):
        if fullname in __builtins__:
            try:
                mod = imp.load_module(self.name, self.file,
                                      self.pathname, self.desc)
            finally:
                if self.file:
                    self.file.close()
            sys.modules[fullname] = mod
        else:
            if self.file:
                self.file.close()
            mod = makeImportedModule(self.name, self.pathname, self.desc,
                                     self.scope)
            sys.modules[fullname] = mod
        return mod
    

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
