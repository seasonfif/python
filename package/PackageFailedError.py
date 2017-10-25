#!usr/bin/env python
# coding=utf-8

class PackageFailedError(RuntimeError):
	def __init__(self, msg, plugin_list):
		self.msg = msg
		self.plugin_list = plugin_list

	def print_error(self):
		print self.msg
		for p in self.plugin_list:
			print p.name
