#!/usr/bin/env python
# coding=utf-8
from Queue import Queue
from multiprocessing.managers import BaseManager

import time

import os


class Slave:
	def __init__(self):
		self.dispatch_job_queue = Queue()
		self.finished_job_queue = Queue()

	def start(self):
		# 把派发作业队列和完成作业队列注册到网络上
		BaseManager.register('get_task_queue')
		BaseManager.register('get_result_queue')

		# 连接master
		server = '127.0.0.1'
		print('Connect to server %s...' % server)
		manager = BaseManager(address=(server, 5000), authkey='jobs')
		manager.connect()

		# 使用上面注册的方法获取队列
		dispatch_jobs = manager.get_task_queue()
		finished_jobs = manager.get_result_queue()

		while 1:
			job = dispatch_jobs.get()
			print "%s Run job %s" % (os.getpid(), job.job_id)
			time.sleep(2)
			finished_jobs.put(job)


if __name__ == "__main__":
	slave = Slave()
	slave.start()