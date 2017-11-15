#!usr/bin/env python
# coding=utf-8
import os
import time
import subprocess
import multiprocessing

results = []

def cal(index = 0):
	name = multiprocessing.current_process().name
  	print name,'starting %d' % index
	total = 0
	for i in range(50000000):
		total += i
	print "%s finished %d:%d" % (name, index, total)
	return total

def shellgo(i):
	commands = "git ss > /dev/null 2>&1"
	code = os.system(commands)
	return code

def test1():
	# 进程同步等待，还是很耗时
	for k in range(2):
		p = multiprocessing.Process(target=cal, args=(k,))
		p.start()
		p.join()

def test2():
	pool = multiprocessing.Pool(processes=3)
	for i in range(3):
		res = pool.apply_async(cal, (i,))
		results.append(res)
	pool.close()
	pool.join()
	for res in results:
		print res.get()

def test3():
	pool = multiprocessing.Pool(processes=3)
	for i in range(3):
		res = pool.apply(shellgo, (i,))
		results.append(res)
	pool.close()
	pool.join()
	for res in results:
		print res

if __name__ == '__main__':
	multiprocessing.freeze_support()
	t = time.time()
	# test1()
	#test2()
	test3()
	print "All process done.", time.time() - t