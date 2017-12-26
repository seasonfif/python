#!/usr/bin/env python
# coding=utf-8

import urllib
resp = urllib.urlopen("https://github.com/trending?l=abap&since=weekly").read()
print resp