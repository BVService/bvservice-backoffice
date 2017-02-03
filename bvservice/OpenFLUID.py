
__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import os
import glob
import Environment
from string import Template


class OpenFLUID:

  def __init__(self):
    pass


  #=============================================================================
  #=============================================================================


  def generateFileFromTemplate(self,Context,TplFilePath,FinalFilePath):

    with open(TplFilePath,'rt') as TplFile:
      Content = Template(TplFile.read())
      FinalContent = Content.safe_substitute(Context)
      with open(FinalFilePath,'wt') as FinalFile:
        FinalFile.write(FinalContent)


  #=============================================================================
  #=============================================================================


  def generateFilesFromTemplates(self,Context,TplDirPath,FinalDirPath):

    for File in glob.glob(os.path.join(TplDirPath,'*.fluidx.tpl')):
      self.generateFileFromTemplate(Context,File,os.path.join(FinalDirPath,os.path.splitext(os.path.basename(File))[0]))


  #=============================================================================
  #=============================================================================


  def execute(self,InPath,OutPath):
    return (os.system("openfluid run {0} {1}".format(InPath,OutPath)) == 0)
