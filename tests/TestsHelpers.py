
__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import os

def getDataPath(Dir):
  return os.path.join(os.getcwd(),"_tests-exec",Dir)
