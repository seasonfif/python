#!usr/bin/env python
# coding=utf-8

import time
import multiprocessing

def write(queue):
    vals = [1, 2, 3, 4, 5, 6]
    for v in vals:
        print 'Put %s to queue...' % v
        queue.put(v)
        time.sleep(3)

def read(queue):
    while 1:
        value = queue.get(True)
        print 'Get %s from queue.' % value

pool = multiprocessing.Pool()
queue = multiprocessing.Queue()

pw = multiprocessing.Process(target=write, args=(queue,))
pr = multiprocessing.Process(target=read, args=(queue,))
pw.start()
pr.start()
pw.join()
pr.terminate()
