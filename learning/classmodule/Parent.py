# coding=utf-8
class Parent(object):
	__parentAttr = 100
	_parentAttr = 100
	parentAttr = 100

	def __init__(self):
		print "父类构造函数"
	
	def parentMethod(self):
		print "父类方法"

	def _protectedMethod(self):
		print "我是protected方法"
	
	def __privateMethod(self):
		print "我是private方法"

	def overWriteMethod(self):
		print "父类方法重写"

class Father(object):
	__parentAttr = 200
	_parentAttr = 200
	parentAttr = 200

	def __init__(self):
		print "Father类构造函数"
	
	def parentMethod(self):
		print "Father类方法"

	def _protectedMethod(self):
		print "Father protected方法"
	
	def __privateMethod(self):
		print "Father private方法"

	def overWriteMethod(self):
		print "Father类方法重写"

class Child (Father,Parent):
	childAttr = "100"

	def __init__(self):
		# 调用父类构造函数 老写法
		# Parent.__init__(self)
		# 新写法（父类需要继承object）
		super(Child, self).__init__()
		print "子类构造函数"

	def childMethod(self):
		print "子类方法"
	
	def overWriteMethod(self):
		# 每个父类单独调用
		# Parent.overWriteMethod(self)
		# 广度优先查找父类overWriteMethod方法，不会调用所有父类方法
		super(Child, self).overWriteMethod()
		print "子类方法重写"

c = Child()
c.parentMethod()
c.childMethod()
c._protectedMethod()
# 私有方法子类调用运行会报错
# c.__privateMethod()
# 通过以下方式访问私有方法
c._Parent__privateMethod()
print "访问父类公开变量：" + bytes(c.parentAttr)
print "访问父类保护变量：" + bytes(c._parentAttr)
# 子类调用父类私有变量运行会报错
# print "访问父类私有变量：" + bytes(c.__parentAttr)
# 通过以下方式访问私有变量
print "访问父类私有变量：" + bytes(c._Parent__parentAttr)

c.overWriteMethod()