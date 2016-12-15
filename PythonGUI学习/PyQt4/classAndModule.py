# coding:utf-8

class Chair(object):
	"""
	This class represents chairs.
	"""

	def __init__(self, name, legs=4): #self 是一个指向对象自身的变量，必须放在每个（非static）方法参数列表的第一个位置
		self.name = name
		self.legs = legs

chair1 = Chair("Barselona")
chair2 = Chair("Bar Stool", 1)
print chair1.name, chair1.legs
print chair2.name, chair2.legs

# 静态数据，静态方法，装饰器

print 3/2.0
print 3//2.0 #截断除法与精准除法