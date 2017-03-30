
__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import os
import random
import datetime

import Environment
import OpenFLUID
import Geoserver
import Tools


class Manager:

  def __init__(self,Environment):
    self.Env = Environment

    self.Env.initializeCurrentZoneStorage()


  #=============================================================================
  #=============================================================================


  @staticmethod
  def normalizeContext(Context):

    NContext = Context.copy()

    # Replace None values by blank string
    for Item in NContext:
      if NContext[Item] is None:
        NContext[Item] = ""

    return NContext


  #=============================================================================
  #=============================================================================


  def displayMessage(self,Phase,Msg):
    print "==",self.Env.CodedZoneName,"/",Phase,":",Msg


  #=============================================================================
  #=============================================================================


  @staticmethod
  def generateName():

    Part1 = ["happy", "jolly", "dreamy", "sad", "angry", "pensive", "focused", "sleepy", "grave",
             "jovial", "sick", "hungry", "thirsty", "elegant", "backstabbing", "clever", "trusting", "loving",
             "distracted", "determined", "stoic", "stupefied", "sharp", "agitated", "cocky", "tender",
             "naughty", "kickass", "drunk", "boring", "nostalgic", "ecstatic", "insane", "cranky", "mad",
             "goofy", "furious", "desperate", "hopeful", "compassionate", "silly", "lonely", "condescending",
             "suspicious", "berserk", "high", "romantic", "prickly", "evil"]

    Part2 = ["river","mountain","field","road","beach","hill","ravine","summit","valley","forest","lake","waterfall"]

    Random = random.SystemRandom()

    return "{0}_{1}".format(Random.choice(Part1),Random.choice(Part2))


  #=============================================================================
  #=============================================================================


  @staticmethod
  def getScenarioName(Name):

    ISODateStr = datetime.datetime.now().strftime("%Y%m%dT%H%M%S--")
    if Name is None or not Name:
      return ISODateStr+Manager.generateName()
    else:
      return ISODateStr+Environment.Environment.getCodedName(Name)


  #=============================================================================
  #=============================================================================



  def runPreparation(self,Context):

    self.displayMessage("preparation","Initialization")

    OF = OpenFLUID.OpenFLUID()

    # In/Out paths for the preparation simulation
    INPath = os.path.join(self.Env.CurrentZonePreparationPath,"IN")
    RasterINPath = os.path.join(INPath,"gisdata-input","raster")
    VectorINPath = os.path.join(INPath,"gisdata-input","vector")
    OUTPath = os.path.join(self.Env.CurrentZonePreparationPath,"OUT")
    VectorReleaseOUTPath = os.path.join(OUTPath,"gisdata-release","vector")

    self.displayMessage("preparation","Preparing files tree")

    Tools.makedirs(INPath)


    # 0. Check context contents

    self.displayMessage("preparation","Checking run context")

    if not ("DEM_url" in Context and "plots_url" in Context):
      raise ValueError("Context must contain DEM_url and plots_url parameters")

    NormContext = Manager.normalizeContext(Context)


    # 1. Generate OpenFLUID files from preparation templates + Context

    self.displayMessage("preparation","Generating simulation configuration")

    OF.generateFilesFromTemplates(NormContext,self.Env.PreparationTemplatesPath,
                                              INPath)

    # 2. Retreive required spatial layers from geoserver

    self.displayMessage("preparation","Retreiving geospatial data")

    GS = Geoserver.Geoserver("","")

    GS.retreiveLayer(NormContext["DEM_url"],RasterINPath)
    GS.retreiveLayer(NormContext["plots_url"],VectorINPath)


    # 3. Run simulation

    self.displayMessage("preparation","Running simulation")

    OutErrFilePath = os.path.join(self.Env.CurrentZonePreparationPath,"openfluid-execution.outerr")
    if not OF.execute(INPath,OUTPath,OutErrFilePath):
      raise RuntimeError("Error in OpenFLUID simulation during preparation execution, see file {0} for details".format(OutErrFilePath))

    self.displayMessage("preparation","Completed")


  #=============================================================================
  #=============================================================================


  def runScenario(self,Context):

    self.displayMessage("scenario[?]","Initialization")

    OF = OpenFLUID.OpenFLUID()

    # Check preparation has been run before

    PreparationOUTPath = os.path.join(self.Env.CurrentZonePreparationPath,"OUT")

    if not os.path.exists(PreparationOUTPath):
      raise RuntimeError("Preparation has not been performed before running the scenario")


    # 0. Check context contents and prepare directories tree

    self.displayMessage("scenario[?]","Checking run context")

    if not "scenario_name" in Context:
      raise ValueError("Context must contain scenario_name parameters")

    NormContext = Manager.normalizeContext(Context)

    CurrentScenarioName = Manager.getScenarioName(Context["scenario_name"])

    self.displayMessage("scenario["+CurrentScenarioName+"]","Preparing files tree")

    CurrentScenarioPath = os.path.join(self.Env.CurrentZoneScenariosPath,
                                       CurrentScenarioName)

    INPath = os.path.join(CurrentScenarioPath,"IN")
    RasterINPath = os.path.join(INPath,"gisdata-input","raster")
    VectorINPath = os.path.join(INPath,"gisdata-input","vector")
    OUTPath = os.path.join(CurrentScenarioPath,"OUT")
    VectorOutputOUTPath = os.path.join(OUTPath,"gisdata-output","vector")
    VectorReleaseOUTPath = os.path.join(OUTPath,"gisdata-release","vector")

    PreparationVectorOutputPath = os.path.join(PreparationOUTPath,"gisdata-output","vector")
    PreparationVectorReleasePath = os.path.join(PreparationOUTPath,"gisdata-release","vector")

    Tools.makedirs(INPath)
    Tools.makedirs(RasterINPath)
    Tools.makedirs(VectorINPath)
    Tools.makedirs(OUTPath)


    # 1. Generate OpenFLUID files from scenario templates + Context

    self.displayMessage("scenario["+CurrentScenarioName+"]","Generating simulation configuration")

    OF.generateFilesFromTemplates(NormContext,self.Env.ScenariosTemplatesPath,
                                              INPath)


    # 2. Retreive required spatial layers from preparation local storage and geoserver

    self.displayMessage("scenario["+CurrentScenarioName+"]","Retreiving geospatial data")

    GS = Geoserver.Geoserver("","")

    GS.retreiveLayer("file://"+PreparationVectorOutputPath+"/plots.shp",VectorOutputOUTPath)
    GS.retreiveLayer("file://"+PreparationVectorReleasePath+"/SRF.shp",VectorOutputOUTPath)
    GS.retreiveLayer("file://"+PreparationVectorReleasePath+"/LNR.shp",VectorOutputOUTPath)

    if 'ditches_url' in NormContext:
      GS.retreiveLayer(NormContext["ditches_url"],VectorINPath)

    if 'rivers_url' in NormContext:
      GS.retreiveLayer(NormContext["rivers_url"],VectorINPath)

    if 'hedges_url' in NormContext:
      GS.retreiveLayer(NormContext["hedges_url"],VectorINPath)

    if 'benches_url' in NormContext:
      GS.retreiveLayer(NormContext["benches_url"],VectorINPath)

    if 'grassbands_url' in NormContext:
      GS.retreiveLayer(NormContext["grassbands_url"],VectorINPath)

    if 'thalwegs_url' in NormContext:
      GS.retreiveLayer(NormContext["thalwegs_url"],VectorINPath)


    # 3. Run simulation

    self.displayMessage("scenario["+CurrentScenarioName+"]","Running simulation")

    OutErrFilePath = os.path.join(CurrentScenarioPath,"openfluid-execution.outerr")
    if not OF.execute(INPath,OUTPath,OutErrFilePath):
      raise RuntimeError("Error in OpenFLUID simulation during scenario execution, see file {0} for details".format(OutErrFilePath))

    self.displayMessage("scenario["+CurrentScenarioName+"]","Completed")
