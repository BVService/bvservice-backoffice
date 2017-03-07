# Overview

This set of scripts is for backoffice management of the BVservice web app, mainly for execution of simulations. It can be used as a python package or using the provided command line tool from a terminal.

# Requirements

These scripts requires __Python 2.7+__ and the following python packages:
* shutil
* glob
* argparse

It also requires that the following bvservice components are correctly installed:
* LandProcessor library and simulators
* OpenFLUID simulators for computation of indicators (bvservice-simulation)

# Usage

## Command line

To get more informations on how to use the command line tool, you can display the help:
```
python BVservice-cli.py --help
```

Specific help can be obtained for both preparation and scenario subcommands
```
python BVservice-cli.py preparation --help
```
or
```
python BVservice-cli.py scenario --help
```

## Python package

For using these scripts as a python package, the main entry point is the Manager class that can be imported using the following instructions in your python source code:
```python
from bvservice import Manager
```


# Development

## Source code organization

The package source code is located in the `bvservice` directory.  
The tests source code is located in the `tests` directory.  
The command line tool is located in the root directory.

## Tests

Run the [nosetests](http://nose.readthedocs.io) tool from the source code root directory:
```
nosetests
```
For a more detailed execution of tests, you can add verbosity and stdout options:
```
nosetests --verbosity=3 -s
```
