# -*-coding:Latin-1 -*

__license__ = "GPLv3"

import unittest
import os
import sys
import shutil
from bvservice.Environment import Environment


class testEnvironment(unittest.TestCase):

  @classmethod
  def setUpClass(cls):

    Environment.ExecutionDataPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"_exec")

    if os.path.isdir(Environment.ExecutionDataPath):
      shutil.rmtree(Environment.ExecutionDataPath)


  #=============================================================================
  #=============================================================================


  def setUp(self):
    self.Env = Environment("My Test Zone")


  #=============================================================================
  #=============================================================================


  def test1_CodedZoneName(self):

    print
    print(Environment.getCodedZoneName("AnotherTestZone"))
    print(Environment.getCodedZoneName("Another Test Zone"))
    print(Environment.getCodedZoneName('Montluçon'))
    print(Environment.getCodedZoneName('Saint Germain des Près'))


  #=============================================================================
  #=============================================================================


  def test2_Paths(self):

    print
    print(self.Env.TemplatesPath)
    print(self.Env.PreparationTemplatesPath)
    print(self.Env.ScenariosTemplatesPath)
    print(self.Env.CurrentZonePath)


  #=============================================================================
  #=============================================================================


  def test3_InitializeStorage(self):

    self.Env.initializeGlobalStorage()
    self.Env.initializeCurrentZoneStorage()


  #=============================================================================
  #=============================================================================


if __name__ == '__main__':
    unittest.main()
