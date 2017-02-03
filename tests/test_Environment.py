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

import TestsHelpers


class testEnvironment(unittest.TestCase):

  TestExecutionDataPath = ""


  @classmethod
  def setUpClass(cls):

    cls.TestExecutionDataPath = TestsHelpers.getDataPath("Environment")

    if os.path.isdir(cls.TestExecutionDataPath):
      shutil.rmtree(cls.TestExecutionDataPath)


  #=============================================================================
  #=============================================================================


  def setUp(self):
    self.Env = Environment("My Test Zone",self.TestExecutionDataPath)


  #=============================================================================
  #=============================================================================


  def test01_CodedZoneName(self):

    print
    print(Environment.getCodedName("AnotherTestZone"))
    print(Environment.getCodedName("Another Test Zone"))
    print(Environment.getCodedName('Montluçon'))
    print(Environment.getCodedName('Saint Germain des Près'))


  #=============================================================================
  #=============================================================================


  def test02_Paths(self):

    print
    print(self.Env.TemplatesPath)
    print(self.Env.PreparationTemplatesPath)
    print(self.Env.ScenariosTemplatesPath)
    print(self.Env.CurrentZonePath)


  #=============================================================================
  #=============================================================================


  def test03_InitializeStorage(self):

    self.Env.initializeGlobalStorage()
    self.Env.initializeCurrentZoneStorage()


  #=============================================================================
  #=============================================================================


if __name__ == '__main__':
    unittest.main()
