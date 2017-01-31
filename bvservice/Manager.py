
__license__ = "GPLv3"

import Environment


class Manager:

  def __init__(self,Environment):
    self.Environment = Environment


  #=============================================================================
  #=============================================================================


  def runPreparation(self,Context):

    print("Manager.runPreparation : not implemented")

    # 1. Generate OpenFLUID files from preparation templates + Context
    # 2. Download required spatial layers from geoserver
    # 3. Run simulation
    # 4. Publish resulting layers to geoserver


  #=============================================================================
  #=============================================================================


  def runScenario(self,Context):
    print("Manager.runScenario : not implemented")

    # 1. Generate OpenFLUID files from scenario templates + Context
    # 2. Download required spatial layers from geoserver
    # 3. Run simulation
    # 4. Publish resulting layers to geoserver
