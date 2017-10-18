#!/usr/bin/python
# coding=utf-8
import time
import calendar

# print time.__doc__
t = time.time()
# print dir(time)
print "stamp :", t
localtime = time.localtime(t)
print "本地时间为 :", localtime
print time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print time.strftime("%a %b %d %H:%M:%S %Y", localtime)

# ab = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime("Sat Mar 28 22:24:24 2016", "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2017, 10)
print cal