# coding:utf-8

"""
面向对象　继承　inheritance

父类(基类)　子类(派生类)


对已经定义好的类进行扩展，如车类到小轿车类、公交车类、救护车类　is-a

Control -> Button -> BitmapButton

object 在python 中成为万类之源


子类的定义

class SubClassName(ParentClass1[,ParentClass2,....])
	'optional class documentation string'
	class_suit


继承自一个父类，称为单继承
继承自多个父类，称为多继承

Python 同C++一样支持多继承，但Java只支持单继承


默认情况下，Python类的成员属性和方法都是"public"
但是Python提供了"访问控制符"来限定成员函数的的访问

双下划线（__var）：限定类属性和方法在类内部可见

属性会被__classname_var替换，将防止父类与子类中的同名冲突

单下划线(_var) ：限定类属性和方法在模块内可见

防止模块的属性用 from module import *来加载
"""


class Dog(object): # 创建对象的时候最开始主要做两件事，第一件分配内存，第二件调用__init__()方法，__init__()类似于其他语言中的构造器
	'define a Dog class'
	counter = 0 # 类属性，用于统计使用该类生成的对象个数
	def __init__(self,name):
		self.name = name
		Dog.counter +=1
	def greet(self):
		print "Hi, I am %s.My number is %d" %(self.name, Dog.counter)


class BarkingDog(Dog):
	# define subclass BarkingDog
	# 如果子类重写了父类的初始化方法，父类的初始化方法就不会被自动调用，必须显示的写出来才会被执行。

	def greet(self): # 子类重写父类中的方法称为重载
		"initial subclass"
		print "Woof! I am %s, my number is  %d" %(self.name, Dog.counter)

if __name__ == "__main__":
	dog = BarkingDog('Zoe')
	dog.greet()
	print dog.name
	print 'abc\'d'
	print "abc'd"