#!/usr/bin/python
# coding=utf-8
counter = 100
miles = 100.123
print counter
print miles

str = 'Hello World!'
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

# 列表
print "列表List"
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个的元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
list[2] = "hahah"        # 重新赋值
print list + tinylist    # 打印组合的列表

# 元组
print "元组Tuple"
tuple = ('runoob', 786 , 2.23, 'john', 70.2)
print tuple
# tuple[1] = 111  元组不支持重新赋值
print tuple[1]

# 字典
print "字典Dictionary"
dicty = {}
dicty["one"] = 2
dicty[2] = "one"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dicty
print dicty.keys()
print dicty.values()
print tinydict
print type(dicty)
print isinstance(dicty, dict)

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
c = a & b;        # 12 = 0000 1100
print "a & b =", a & b
print "a | b =", a | b

if True:
	print "true"
else:
	print "false"