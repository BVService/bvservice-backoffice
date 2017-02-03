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

    os.system("python BVservice-cli.py --exec-data-path={0} preparation --zone-name=\"My CLI zone\" "
                                       "--DEM-url=file://tests/datasets/DardaillonSmall/raster/dem.tif "
                                       "--plots-url=file://tests/datasets/DardaillonSmall/vector/plots.shp"
                                       .format(self.TestExecutionDataPath))


  #=============================================================================
  #=============================================================================


  def test02_Scenario(self):
        os.system("python BVservice-cli.py --exec-data-path={0} scenario --zone-name=\"My CLI zone\" "
                                           "--ditches-url=file://tests/datasets/DardaillonSmall/vector/fosses.shp "
                                           "--hedges-url=file://tests/datasets/DardaillonSmall/vector/haies.shp "
                                           "--benches-url=file://tests/datasets/DardaillonSmall/vector/talus.shp "
                                           "--grassbands-url=file://tests/datasets/DardaillonSmall/vector/bandesenherbees.shp"
                                           .format(self.TestExecutionDataPath))



if __name__ == '__main__':
    unittest.main()
