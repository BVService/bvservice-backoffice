
__license__ = "GPLv3"

import os
import sys
import shutil
import glob
import ConfigParser


class Environment:

  TemplatesDir = "templates"
  ZonesDir = "zones"
  PreparationDir = "preparation"
  ScenariosDir = "scenarios"
  ResourcesDir = "resources"
  ExecutionDataPath = "/var/local/bvservice"


  def __init__(self,ZoneName):

    self.ZoneName = ZoneName
    self.CodedZoneName = self.getCodedZoneName(ZoneName.decode())

    self.TemplatesPath = os.path.join(Environment.ExecutionDataPath,Environment.TemplatesDir)
    self.PreparationTemplatesPath = os.path.join(self.TemplatesPath,Environment.PreparationDir)
    self.ScenariosTemplatesPath = os.path.join(self.TemplatesPath,Environment.ScenariosDir)
    self.ZonesPath = os.path.join(Environment.ExecutionDataPath,Environment.ZonesDir)
    self.CurrentZonePath = os.path.join(self.ZonesPath,self.CodedZoneName)

    self.ResourcesPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),Environment.ResourcesDir)


  #=============================================================================
  #=============================================================================


  @staticmethod
  def getCodedZoneName(OriginalName):
    CodedName = OriginalName.replace(" ","_")
    return CodedName
    # other method, using unicodedata : removing accents then replacing spaces by underscores
    #return unicodedata.normalize('NFD',OriginalName).encode('ascii', 'ignore').replace(" ","_")


  #=============================================================================
  #=============================================================================


  def initializeGlobalStorage(self):
    os.makedirs(self.TemplatesPath)
    os.makedirs(self.PreparationTemplatesPath)
    os.makedirs(self.ScenariosTemplatesPath)
    os.makedirs(self.ZonesPath)

    # installation of templates for preparation
    for File in glob.glob(os.path.join(self.ResourcesPath,Environment.TemplatesDir,Environment.PreparationDir,'*')):
      shutil.copy(File,self.PreparationTemplatesPath)

    # installation of templates for scenarios
    for File in glob.glob(os.path.join(self.ResourcesPath,Environment.TemplatesDir,Environment.ScenariosDir,'*')):
      shutil.copy(File,self.ScenariosTemplatesPath)


  #=============================================================================
  #=============================================================================


  def initializeCurrentZoneStorage(self):
    os.makedirs(self.CurrentZonePath)
