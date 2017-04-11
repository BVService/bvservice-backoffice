# -*-coding:Latin-1 -*

__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import unittest
import os
import shutil

import TestsHelpers


class testCLI(unittest.TestCase):

  TestExecutionDataPath = ""


  @classmethod
  def setUpClass(cls):

    cls.TestExecutionDataPath = TestsHelpers.getDataPath("cli")


  #=============================================================================
  #=============================================================================


  def setUp(self):
    pass


  #=============================================================================
  #=============================================================================


  def test01_Preparation(self):

    if os.path.isdir(self.TestExecutionDataPath):
      shutil.rmtree(self.TestExecutionDataPath)

    returncode = os.system("python BVservice-cli.py --exec-data-path={0} preparation --zone-name=\"My CLI zone\" "
                                                   "--DEM-url=file://tests/datasets/DardaillonSmall/raster/dem.tif "
                                                   "--plots-url=file://tests/datasets/DardaillonSmall/vector/plots.shp"
                                                   .format(self.TestExecutionDataPath))

    self.assertEqual(returncode,0)


  #=============================================================================
  #=============================================================================


  def test02_Scenario(self):
    returncode = os.system("python BVservice-cli.py --exec-data-path={0} scenario --zone-name=\"My CLI zone\" "
                                                   "--ditches-url=file://tests/datasets/DardaillonSmall/vector/fosses.shp "
                                                   "--hedges-url=file://tests/datasets/DardaillonSmall/vector/haies.shp "
                                                   "--benches-url=file://tests/datasets/DardaillonSmall/vector/talus.shp "
                                                   "--grassbands-url=file://tests/datasets/DardaillonSmall/vector/bandesenherbees.shp"
                                                   .format(self.TestExecutionDataPath))

    self.assertEqual(returncode,0)


  #=============================================================================
  #=============================================================================


  def test03_ScenarioNamed(self):
    returncode = os.system("python BVservice-cli.py --exec-data-path={0} scenario --zone-name=\"My CLI zone\" "
                                                   "--scenario-name=\"My story\" "
                                                   "--ditches-url=file://tests/datasets/DardaillonSmall/vector/fosses.shp "
                                                   "--hedges-url=file://tests/datasets/DardaillonSmall/vector/haies.shp "
                                                   "--benches-url=file://tests/datasets/DardaillonSmall/vector/talus.shp "
                                                   "--grassbands-url=file://tests/datasets/DardaillonSmall/vector/bandesenherbees.shp"
                                                   .format(self.TestExecutionDataPath))

    self.assertEqual(returncode,0)


  #=============================================================================
  #=============================================================================


  def test10_WrongCommand(self):
    returncode = os.system("python BVservice-cli.py --exec-data-path={0} wrngcmd --zone-name=\"My WRNGCMD CLI zone\" "
                                                   "--DEM-url=file://tests/datasets/DardaillonSmall/raster/dem.tif "
                                                   "--plots-url=file://tests/datasets/DardaillonSmall/vector/plots.shp"
                                                   .format(self.TestExecutionDataPath))

    self.assertNotEqual(returncode,0)


  #=============================================================================
  #=============================================================================


  def test20_WrongPlotsFileName(self):
    returncode = os.system("python BVservice-cli.py --exec-data-path={0} preparation --zone-name=\"My WRNGPLOT CLI zone\" "
                                                   "--DEM-url=file://tests/datasets/DardaillonSmall/raster/dem.tif "
                                                   "--plots-url=file://tests/datasets/DardaillonSmallWrongFileName/vector/plots_wrongname.shp"
                                                   .format(self.TestExecutionDataPath))

    self.assertNotEqual(returncode,0)


if __name__ == '__main__':
    unittest.main()
