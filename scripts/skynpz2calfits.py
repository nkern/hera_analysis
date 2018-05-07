#!/usr/bin/env python2.7
from hera_analysis import skynpz2calfits
import os
import sys
import shutil
import copy

if __name__ == "__main__":
    a = skynpz2calfits.arg_parser()
    args = a.parse_args()

    gain_convention = 'divide'
    if args.multiply_gains:
        gain_convention = 'multiply'

    kwargs = copy.copy(args).__dict__
    kwargs.pop('fname')
    kwargs.pop('uv_file')
    kwargs.pop('multiply_gains')
    kwargs['verbose'] = args.silence == False
    kwargs.pop('silence')
    kwargs['gain_convention'] = gain_convention
    skynpz2calfits(args.fname, args.uv_file, **kwargs)


