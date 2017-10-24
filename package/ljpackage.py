#!/usr/bin/env python
# coding=utf-8
import os
from os import path
import json
from Plugin import *

def init_plugins_by_host(host):
	try:
		config_path = path.join(path.dirname(__file__), "config_local.json")
		f = open(config_path)
		config = json.load(f)
		plugin_list = config[host.version]
	except BaseException, e:
		print e
		plugin_list = []
	else:
		for p in plugin_list:
			plugin = Plugin(p["name"], p["version"], 
					p["branch"], p["buildtype"],)
			
			# 初始化各插件代码仓库
			repo_dirs = json.load(open(path.join(path.dirname(__file__), "plugin_path.json")))
			try:
				dir = repo_dirs[plugin.name]
			except BaseException, e:
				dir = None
			else:
				pass
			plugin.setRepoDir(dir)

			# 获取各插件git最新版本
			commands = 'git reset --hard && git pull && git checkout --track origin/'+str(plugin.branch) +' && git rev-parse HEAD'
			print os.system(commands)
			# latest_version
			# plugin.setLatestVersion(latest_version)
			host.append_build_plugin(plugin)

host = Plugin("link", "3.5.0", "feature/link-3.5.0", "debug")
init_plugins_by_host(host)

for p in host.get_build_plugins():
	p.display()


