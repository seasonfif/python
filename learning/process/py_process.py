#!usr/bin/env python
# coding=utf-8
import time
import subprocess

# 设置close_fds=True可以并发，此时windows不能将stdin/stdout/stderr通过pipe输出
child = subprocess.Popen("ls -l", shell=True, close_fds=True)
# 子进程通过管道讲stdout输出到主进程
# child = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
while 1:
	ret1 = child.poll()
	if ret1 == 0:  
		print child.pid, 'end'  
		break  
	elif not ret1:  
		print  child.pid + ' is running'
	else:  
		print child.pid, 'term'  
		break  
# child.wait()
# while child.poll() is None:
# 	line = child.stdout.readline()
# 	if line:
# 		sys.stdout.flush()
# 		print str(plugin.name) + ":::" + str(line)
# print child.returncode