#!/usr/bin/env python

__license__ = "GPLv3"
__author__ = "Jean-Christophe Fabre <jean-christophe.fabre@inra.fr>"


#=============================================================================
#=============================================================================


import argparse
import sys

from bvservice import Manager as BVsManager
from bvservice import Environment as BVsEnv


## Configuration of argument parser

Parser = argparse.ArgumentParser(description="Execute BVservice simulations")
Parser.add_argument("--exec-data-path",help="Root path to BVservice local data")
SubParsers = Parser.add_subparsers(dest="command_name")

ParserPrep = SubParsers.add_parser("preparation")
ParserPrep.add_argument("--zone-name",required=True)
ParserPrep.add_argument("--DEM-url",required=True)
ParserPrep.add_argument("--plots-url",required=True)
ParserPrep.add_argument("--EPSG-code")
ParserPrep.add_argument("--landuse-field")
ParserPrep.add_argument("--min-ent-size")

ParserScen = SubParsers.add_parser("scenario")
ParserScen.add_argument("--zone-name",required=True)
ParserScen.add_argument("--scenario-name")
ParserScen.add_argument("--rivers-url")
ParserScen.add_argument("--ditches-url")
ParserScen.add_argument("--hedges-url")
ParserScen.add_argument("--benches-url")
ParserScen.add_argument("--grassbands-url")
ParserScen.add_argument("--thalwegs-url")
ParserScen.add_argument("--snap-dist")

Args = vars(Parser.parse_args())


## Processing of arguments

Env = None

if Args["exec_data_path"] is not None or Args["exec_data_path"]:
  Env = BVsEnv.Environment(Args["zone_name"],Args["exec_data_path"])
else:
  Env = BVsEnv.Environment(Args["zone_name"])

Man = BVsManager.Manager(Env)

Context = Args.copy()

# Replace None values in Context by blank string
del Context["command_name"]
del Context["exec_data_path"]

print("Work path: {0}".format(Env.CurrentZonePath))
print("Context: {0}".format(Context))

try:
  Env.initializeGlobalStorage()

  if Args["command_name"] == "preparation":
    Man.runPreparation(Context)
  elif Args["command_name"] == "scenario":
    Man.runScenario(Context)
except Exception as e:
  print str(e)
  sys.exit(1)
else:
  sys.exit(0)
