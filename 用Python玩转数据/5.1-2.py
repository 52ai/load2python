# coding:utf-8
"""
面向对象　抽象　abstraction

类　描述了对象的特征（数据和操作）
对象（实例）　由数据及其能对其实施的操作所构成的封装实体


类的具体化就是对象
对象的抽象就是类

类　模板
对象　值


class ClassName(object):
	'define ClassName class'
	class_suit

1.定义一个类-Dog
2.创建一个实例--dog
3.通过实例使用属性或方法--dog.greet()

对象初始化方法　__init__()

1.当类被调用后，Python将创建实例对象
2.创建完对象以后，Python自动调用的第一个方法为__init__()
3.实例对象作为方法的第一个参数（self）被传递进调用进去，调用类创建实例对象时，参数都传给__init__()


类属性（class attributes）与对象无关，也称静态属性，修改类属性需要用类名
"""

class Dog(object): # 创建对象的时候最开始主要做两件事，第一件分配内存，第二件调用__init__()方法，__init__()类似于其他语言中的构造器
	'define a Dog class'
	counter = 0 # 类属性，用于统计使用该类生成的对象个数
	def __init__(self,name):
		self.name = name
		Dog.counter +=1
	def greet(self):
		print "Hi, I am %s.My number is %d" %(self.name, Dog.counter)


if __name__ == '__main__': # 程序的入口
	dog_Sara = Dog("Sara")
	# dog.setName('Paul')
	dog_Sara.greet()
	dog_Paul = Dog("Paul")
	dog_Paul.greet()


"""
现在来理解GUI控件，以Button为例


Button属性：label,size,pos,Font
Button方法：SetLabel(),SetDefault(),Enable()


"""


