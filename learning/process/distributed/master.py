#!/usr/bin/env python
# coding=utf-8
import threading
from Queue import Queue
from multiprocessing.managers import BaseManager
import multiprocessing
import time
from job import Job

# 发送任务的队列:
task_queue = Queue(10)
# 接收结果的队列:
result_queue = Queue()
dispatch_jobs = Queue()


def return_task_queue():
	global task_queue
	return task_queue


def return_result_queue():
	global result_queue
	return result_queue


def add_job(manager):
	global dispatch_jobs
	dispatch_jobs = manager.get_task_queue()
	job_id = 0
	while 1:
		job_id += 1
		if not dispatch_jobs.full():
			job = Job(job_id)
			print 'Dispatch job: %s' % job.job_id
			dispatch_jobs.put(job)
			time.sleep(1)
		else:
			time.sleep(1)
			print 'Task full, please wait',


def handle_job_result(manager):
	finished_jobs = manager.get_result_queue()
	while not dispatch_jobs.empty():
		job = finished_jobs.get()
		print 'Finished Job: %s' % job.job_id
	manager.shutdown()


if __name__ == "__main__":
	multiprocessing.freeze_support()
	BaseManager.register('get_task_queue', callable=return_task_queue)
	BaseManager.register('get_result_queue', callable=return_result_queue)

	manager = BaseManager(address=("127.0.0.1", 5000), authkey="jobs")
	manager.start()

	threading.Thread(target=add_job, args=(manager,)).start()
	threading.Thread(target=handle_job_result, args=(manager,)).start()

