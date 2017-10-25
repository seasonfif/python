#!/usr/bin/env python
# coding=utf-8

import urllib
resp = urllib.urlopen("http://www.baidu.com").read()
print resp