# coding=utf-8
class Test:
	def class_func(self, p):
		# self代表的是类的实例对象
		print self 				# <__main__.Test instance at 0x01D98E40>
		print self.__class__	# __main__.Test
		print p

t = Test()
t.class_func("p")