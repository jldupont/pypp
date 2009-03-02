#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

try:
    from mako.template import Template
    from mako.lookup import TemplateLookup
except:
    print "pypp: Mako template package not found. Please install"
    sys.exit(1)
 
 
# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import doctest
    doctest.testmod()
