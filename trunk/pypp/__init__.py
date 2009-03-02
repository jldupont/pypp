"""\
PYthon PreProcessor
===================

A directive .pypp must be found following a comment hash
for the file to be preprocessed.

Usage
-----
    import pypp
    

    @author: Jean-Lou Dupont
"""
__all__ = []

import sys
from importer import *
from controller import *

_controller = Controller()
_importer = Importer()

# I'd rather not have the Importer module handle the chain of events
_importer.callback_import_module = _controller.handle_import_module

# Hook-up our Importer following PEP302
sys.meta_path.append(_importer)

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import os.path
    import jld.cmd_g2.base_ui

    for e in _controller.processed():
        print e

    #for e in _importer.processed:
    #    print e