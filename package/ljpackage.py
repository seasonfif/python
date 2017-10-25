#!/usr/bin/env python
# coding=utf-8
import os
import sys
import time
import subprocess
import multiprocessing
from os import path
import json
from Plugin import *

def get_repo_dir(plugin):
	# 初始化各插件代码仓库
	repo_dirs = json.load(open(path.join(path.dirname(__file__), "plugin_path.json")))
	try:
		repo_dir = repo_dirs[plugin.name]
	except BaseException, e:
		repo_dir = None
	else:
		pass
	return repo_dir

def get_latest_version(plugin):
	# 更新插件git仓库
	c = 'cd %s && git reset --hard && git pull && git checkout %s' % (plugin.repo_dir, plugin.branch)
	result = subprocess.call(c, shell=True)
	if result != 0:
		r_c = 'cd %s && git reset --hard && git pull && git checkout --track origin/%s' % (plugin.repo_dir, plugin.branch)
		subprocess.call(r_c, shell=True)
	
	# 获取插件git最新版本
	version_c = 'cd %s && git rev-parse HEAD' % (plugin.repo_dir)
	child = subprocess.Popen(version_c, shell=True, stdout=subprocess.PIPE)
	# 等待执行完毕
	child.wait()
	if child.returncode != 0:
		return None
	else:
		return child.stdout.read().strip()

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
			plugin.set_repo_dir(get_repo_dir(plugin))
			# plugin.set_latest_version(get_latest_version(plugin))
			plugin.set_latest_version("111")
			host.append_build_plugin(plugin)

def get_stored_version():
	try:
		store_file = path.join(path.dirname(__file__), "plugin_git_version.json")
		store_version = json.load(open(store_file))
	except BaseException, e:
		store_version = {}
	else:
		pass	
	return store_version

def update_stored_version(versions):
	jstring = json.dumps(versions, sort_keys=True, indent=4, separators=(',', ': '))
	store_file = path.join(path.dirname(__file__), "plugin_git_version.json")
	f = open(store_file, "w")
	f.write(jstring)
	f.close

def get_stored_version_by_plugin(plugin_name, versions):
	try:
		return versions[plugin_name]
	except BaseException, e:
		return None
	else:
		pass

def build_plugin(plugin):
	print "starting ", multiprocessing.current_process().name
	build_commands = 'cd %s && gradle assemble%s' % (plugin.repo_dir, str(plugin.buildtype).capitalize())
	code = os.system(build_commands)
	return code

if __name__ == "__main__":
	multiprocessing.freeze_support()
	results = []
	host = Plugin("link", "3.5.0", "feature/link-3.5.0", "debug")
	init_plugins_by_host(host)
	stored_versions = get_stored_version()
	# 创建进程池执行编译任务
	pool = multiprocessing.Pool(processes=4)
	t = time.time()
	for p in host.get_build_plugins():
		p_store_version = get_stored_version_by_plugin(p.name, stored_versions)
		if p_store_version == p.latest_version:
			print "版本相同，忽略打包"
			pass
		else:
			stored_versions[p.name] = p.latest_version
			res = pool.apply_async(build_plugin, (p,))
			results.append(res)
	pool.close()
	pool.join()
	print "All process done.", time.time()-t
	for res in results:
		print res.get()
	# update_stored_version(stored_versions)