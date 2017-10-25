#!/usr/bin/env python
# coding=utf-8
import os
import shutil
import sys
import time
import subprocess
import multiprocessing
from os import path
import json
from Plugin import *
from PackageFailedError import *

def get_repo_dir(name):
	# 初始化各插件代码仓库
	repo_dirs = json.load(open(path.join(path.dirname(__file__), "plugin_path.json")))
	try:
		repo_dir = repo_dirs[name]
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
			plugin.set_repo_mian_dir(get_repo_dir(plugin.name))
			plugin.set_repo_dir(path.dirname(plugin.repo_mian_dir))
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

def analyse_plugins_build_result():
	failed = []
	for res_tup in results:
		return_code = res_tup[1].get()
		print return_code
		if return_code != 0:
			failed.append(res_tup[0])
	
	if len(failed) > 0:
		raise PackageFailedError("package link failed!!!", failed)

def mv_plugin_to_host(host):
	host_plugins_dir = path.join(host.repo_mian_dir, "src", "main", "assets", "plugins") 
	print host_plugins_dir
	for p in plugins:
		# if p.rebuild:
			# 修改host.repo_mian_dir
			plugin_path = path.join(host.repo_mian_dir, "build", "outputs","aar")
			files = os.listdir(plugin_path)
			from_file = path.join(plugin_path, files[0])
			to_file = path.join(path.dirname(__file__), host.name + ".jar")
			shutil.copyfile(from_file, to_file)

def package_host(host):
	package_commands = 'cd %s && gradle assemble%s' % (host.repo_dir, str(host.buildtype).capitalize())
	code = os.system(package_commands)
	if code == 0:
		pass
	return code

if __name__ == "__main__":
	multiprocessing.freeze_support()
	# 所有插件集合
	plugins = []
	# 插件编译结果集
	results = []
	host = Plugin("link", "3.5.0", "master", "newlinkDebug")
	host.set_repo_mian_dir(get_repo_dir(host.name))
	host.set_repo_dir(path.dirname(host.repo_mian_dir))
	init_plugins_by_host(host)
	stored_versions = get_stored_version()
	# 创建进程池执行编译任务
	pool = multiprocessing.Pool(processes=4)
	t = time.time()
	plugins = host.get_build_plugins()
	# for p in plugins:
	# 	p_store_version = get_stored_version_by_plugin(p.name, stored_versions)
	# 	if p_store_version == p.latest_version:
	# 		p.set_rebuild(False)
	# 		print "版本相同，忽略打包"
	# 		pass
	# 	else:
	# 		p.set_rebuild(True)
	# 		stored_versions[p.name] = p.latest_version
	# 		res = pool.apply_async(build_plugin, (p,))
	# 		results.append((p, res))
	# pool.close()
	# pool.join()
	# print "All process done.", time.time()-t
	try:
		analyse_plugins_build_result()
	except PackageFailedError, e:
		e.print_error()
	else:
		# mv_plugin_to_host(host)
		update_stored_version(stored_versions)
	package_host(host)