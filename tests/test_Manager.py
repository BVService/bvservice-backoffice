# -*-coding:Latin-1 -*

__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import unittest
import os
import sys
import shutil

from bvservice.Environment import Environment
from bvservice.Manager import Manager

import TestsHelpers

class testManager(unittest.TestCase):

  TestExecutionDataPath = ""


  @classmethod
  def setUpClass(cls):

    cls.TestExecutionDataPath = TestsHelpers.getDataPath("Manager")


  #=============================================================================
  #=============================================================================


  def setUp(self):
    self.Env = Environment("The New Zone",self.TestExecutionDataPath)


  #=============================================================================
  #=============================================================================


  def test01_ScenarioName(self):

    print Manager.generateName()
    print Manager.generateName()
    print Manager.getScenarioName(None)
    print Manager.getScenarioName("")

    print Manager.getScenarioName("MyFirstScenario")
    print Manager.getScenarioName("My Second Scenario")


  #=============================================================================
  #=============================================================================


  def test10_Preparation(self):

    if os.path.isdir(self.TestExecutionDataPath):
      shutil.rmtree(self.TestExecutionDataPath)


    self.Env.initializeGlobalStorage()
    self.Env.initializeCurrentZoneStorage()

    self.Man = Manager(self.Env)

    Context = {'DEM_url': 'file://tests/datasets/DardaillonSmall/raster/dem.tif',
               'plots_url': 'file://tests/datasets/DardaillonSmall/vector/plots.shp',
               'landuse_field': None, 'min_ent_size': None, 'EPSG_code': None}

    self.Man.runPreparation(Context)


  #=============================================================================
  #=============================================================================


  def test11_Scenario(self):

    self.Env.initializeGlobalStorage()
    self.Env.initializeCurrentZoneStorage()

    self.Man = Manager(self.Env)

    Context = {'scenario_name' : 'MyScenario',
               'ditches_url' : 'file://tests/datasets/DardaillonSmall/vector/fosses.shp',
               'hedges_url' : 'file://tests/datasets/DardaillonSmall/vector/haies.shp',
               'benches_url' : 'file://tests/datasets/DardaillonSmall/vector/talus.shp',
               'grassbands_url' : 'file://tests/datasets/DardaillonSmall/vector/bandesenherbees.shp'}

    self.Man.runScenario(Context)



if __name__ == '__main__':
    unittest.main()
