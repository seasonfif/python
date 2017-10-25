#!usr/bin/env python
# coding=utf-8
from os import path
from PackageFailedError import *

results = [("login", 0),("platform", 1)]

def analyse_plugins_build_result():
	failed = []
	for res_tup in results:
		return_code = res_tup[1]
		print return_code
		if return_code != 0:
			failed.append(res_tup[0])
	
	if failed.count > 0:
		raise PackageFailedError("package link failed!!!", failed)

print path.dirname("d:\\lianjia\\newlink-plugin2\\im\\")
try:
	analyse_plugins_build_result()
except PackageFailedError, e:
	print e.msg
else:
	pass