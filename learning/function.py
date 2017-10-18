#!/usr/bin/python
# coding=utf-8
# strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象

# 传不可变对象
def changeInt(a):
	a = 10
def changeString(s):
	s = "hello"

b=2
changeInt(b)
print b

ss = "hello world"
changeString(ss)
print ss

# 传可变对象
def changeList(list):
	list[2] = [1, 2, 3]

ll = [1, 2, 3]
changeList(ll)
print ll

# 关键字函数，与参数顺序无关，参数关键字匹配
# age为缺省参数
def printinfo(name, age=28):
	print "Name: ", name
	print "Age ", age
 
# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")

# 不定长参数
def nolenghtparams(arg1, *args):
	# print arg1
	for var in args:
		print var

nolenghtparams(9)
tuple = (2,3,4,5)
nolenghtparams(1,tuple)
nolenghtparams(1,2,3,4,5)

# lambda函数
sum = lambda arg1,arg2:arg1+arg2
print sum(10, 10)