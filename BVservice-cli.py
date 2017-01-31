#!/usr/bin/env python

__license__ = "GPLv3"

import argparse

from bvservice import Manager as BVsManager
from bvservice import Environment as BVsEnv


## Configuration of argument parser

Parser = argparse.ArgumentParser(description="Execute BVservice simulations")

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
ParserScen.add_argument("--rivers-url")
ParserScen.add_argument("--ditches-url")
ParserScen.add_argument("--hedges-url")
ParserScen.add_argument("--benches-url")
ParserScen.add_argument("--grassbands-url")
ParserScen.add_argument("--thalwegs-url")


Args = vars(Parser.parse_args())


## Processing of arguments

Env = BVsEnv.Environment(Args["zone_name"])
Man = BVsManager.Manager(Env)
Context = Args.copy()
del Context["command_name"]


print("Work path: {0}".format(Env.CurrentZonePath))
print("Context: {0}".format(Context))

if Args["command_name"] == "preparation":
  Man.runPreparation(Context)
elif Args["command_name"] == "scenario":
  Man.runScenario(Context)
