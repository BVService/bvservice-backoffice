
__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import os
import glob
import shutil

import Environment
import Tools

class Geoserver:

  def __init__(self,Login,Password):
    self.Login = Login
    self.Password = Password


  #=============================================================================
  #=============================================================================


  def retreiveLayer(self,FromURL,ToLocalPath):

    # check if source URL is not none nor empty
    if FromURL is None or not FromURL:
      return

    Tools.makedirs(ToLocalPath)

    # processing of local files
    if (FromURL.startswith("file://")):
      FromLocalPath = FromURL[7:]

      # transformation of relative paths to absolute paths
      if not os.path.isabs(FromLocalPath):
        FromLocalPath = os.path.join(os.getcwd(),FromLocalPath)

      for FromFile in glob.glob(os.path.splitext(FromLocalPath)[0]+".*"):
        shutil.copyfile(FromFile,os.path.join(ToLocalPath,os.path.basename(FromFile)))

    # processing of other remote files
    else:
      raise RuntimeError("Geoserver.retreiveLayer : not implemented for remote url")


  #=============================================================================
  #=============================================================================


  def publishLayer(self,FromLocalPath,ToURL):
    raise RuntimeError("Geoserver.publishLayer : not implemented")
