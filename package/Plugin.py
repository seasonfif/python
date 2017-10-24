#!/usr/bin/env python
# coding=utf-8

class Plugin(object):

	__plugins_need_build = []

	def __init__(self, name, version, branch, buildtype):
		self.name = name
		self.version = version
		self.branch = branch
		self.buildtype = buildtype
	
	def setRepoDir(self, dir):
		self.dir = dir

	def setLatestVersion(self, latest_version):
		self.latest_version = latest_version

	def append_build_plugin(self, plugin):
		self.__plugins_need_build.append(plugin)
	
	def get_build_plugins(self):
		return self.__plugins_need_build

	def display(self):
		print str(self.name) + " " + str(self.dir) + " " + str(self.latest_version)