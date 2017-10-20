#!/uer/bin/env python
# coding=utf-8
class Employee:
	# 员工基类
	# empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。
	# 可以在内部类或外部类使用 Employee.empCount 访问
	empCount = 0
	
	# __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法
	# 当创建了这个类的实例时就会调用该方法
	# self代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Employee.empCount += 1

	def displayCount(self):
		print "Total :", Employee.empCount
	
	def displayEmployee(self):
		print "Name:"+self.name +", Age:"+bytes(self.age)
	
if __name__ == "__main__":
	e1 = Employee("seasonfif", 27)
	e2 = Employee("season", 20)
	# 可以使用以下函数的方式来访问属性：
	# getattr(obj, name[, default]) : 访问对象的属性。
	# hasattr(obj,name) : 检查是否存在一个属性。
	# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
	# delattr(obj, name) : 删除属性。
	# 好像不起作用
	setattr(e1, "sex", "female")
	getattr(e1, "sex")
	hasattr(e1, "sex")
	e1.displayEmployee()
	e2.displayEmployee()
	e1.displayCount()
else:
	print "Employee实例化"