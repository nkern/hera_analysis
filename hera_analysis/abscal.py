#!/usr/bin/env python2.7
"""
Routines for absolute calibration
"""
import os
import sys
import glob
import shutil
from pyuvdata import UVData, UVCal
from pyuvdata import utils as uvutils
from hera_cal import utils, datacontainer



