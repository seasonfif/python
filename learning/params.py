#!/usr/bin/env python
# coding=utf-8
from os import path
from PackageFailedError import *
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], None, ["help","output="])
for name, value in opts:
	print name, value

for item in args:
	print item