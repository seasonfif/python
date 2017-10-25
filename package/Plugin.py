#!/usr/bin/env python
# coding=utf-8

class Plugin(object):

	__plugins_need_build = []

	def __init__(self, name, version, branch, buildtype):
		self.name = name
		self.version = version
		self.branch = branch
		self.buildtype = buildtype
	
	def set_repo_dir(self, repo_dir):
		self.repo_dir = repo_dir

	def set_repo_mian_dir(self, repo_mian_dir):
		self.repo_mian_dir = repo_mian_dir

	def set_latest_version(self, latest_version):
		self.latest_version = latest_version

	def append_build_plugin(self, plugin):
		self.__plugins_need_build.append(plugin)
	
	def set_rebuild(self, rebuild):
		self.rebuild = rebuild

	def get_build_plugins(self):
		return self.__plugins_need_build

	def display(self):
		print str(self.name) + " " + str(self.repo_dir) + " " + str(self.latest_version)