
__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import os
import sys
import shutil
import glob

import Tools


class Environment:

  TemplatesDir = "templates"
  ZonesDir = "zones"
  PreparationDir = "preparation"
  ScenariosDir = "scenarios"
  ResourcesDir = "resources"

  def __init__(self,ZoneName,ExecDataPath="/var/local/bvservice",):

    self.ExecutionDataPath = ExecDataPath

    self.ZoneName = ZoneName
    self.CodedZoneName = Environment.getCodedName(ZoneName)

    self.TemplatesPath = os.path.join(self.ExecutionDataPath,Environment.TemplatesDir)
    self.PreparationTemplatesPath = os.path.join(self.TemplatesPath,Environment.PreparationDir)
    self.ScenariosTemplatesPath = os.path.join(self.TemplatesPath,Environment.ScenariosDir)
    self.ZonesPath = os.path.join(self.ExecutionDataPath,Environment.ZonesDir)
    self.CurrentZonePath = os.path.join(self.ZonesPath,self.CodedZoneName)
    self.CurrentZonePreparationPath = os.path.join(self.CurrentZonePath,Environment.PreparationDir)
    self.CurrentZoneScenariosPath = os.path.join(self.CurrentZonePath,Environment.ScenariosDir)

    self.ResourcesPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),Environment.ResourcesDir)


  #=============================================================================
  #=============================================================================


  @staticmethod
  def getCodedName(OriginalName):
    CodedName = OriginalName.replace(" ","_")
    return CodedName
    # other method, using unicodedata : removing accents then replacing spaces by underscores
    #return unicodedata.normalize('NFD',OriginalName).encode('ascii', 'ignore').replace(" ","_")


  #=============================================================================
  #=============================================================================


  def initializeGlobalStorage(self):
    Tools.makedirs(self.TemplatesPath)
    Tools.makedirs(self.PreparationTemplatesPath)
    Tools.makedirs(self.ScenariosTemplatesPath)
    Tools.makedirs(self.ZonesPath)

    # installation of templates for preparation
    for File in glob.glob(os.path.join(self.ResourcesPath,self.TemplatesDir,self.PreparationDir,'*')):
      shutil.copy(File,self.PreparationTemplatesPath)

    # installation of templates for scenarios
    for File in glob.glob(os.path.join(self.ResourcesPath,self.TemplatesDir,self.ScenariosDir,'*')):
      shutil.copy(File,self.ScenariosTemplatesPath)


  #=============================================================================
  #=============================================================================


  def initializeCurrentZoneStorage(self):
    Tools.makedirs(self.CurrentZonePath)
    Tools.makedirs(self.CurrentZonePreparationPath)
    Tools.makedirs(self.CurrentZoneScenariosPath)
