# coding:utf-8
from PyQt4.QtCore import *
now = QDate.currentDate()
never = QDate()
print now 
print never
print bool(now),bool(never) # bool可以将对象转换为布尔类型

'''
Python 风格指南建议，关于缩进每个层次用４个空格,不要使用table键。
'''
x=1
if x>0:
    print x

'''
and 和　or 都是短路逻辑(short-circuit)又称懒惰求值(lazy evaluation)，逻辑表达式x and y ,如果x为假，则表达式了返回x的值，而不去计算y的值，否则就返回y的值。

'''
print "x is zero or positive" if x>=0 else "x is negative"

for char in "yuwenyan":
	print "%s=%d" %(char,ord(char)),
print ""
for i in range(3,11,2): # 从3开始小于11,步长为2
	print i,
# Python提供了和range有相同语意的xrange，他是一个生成器，每次调用进行一次简单的计算，内存利用效率比较高
print ""
p=2**16 -1
q=7L
print p
print q
print type(p)
print type(q)
# 列表解析
fives = [x for x in range(50) if x%5==0]
print fives
print type(fives)

# 生成器  同样的表达式，只不过是把方括号，变成了圆括号
sixs = (x for x in range(50) if x % 6 ==0)
print sixs
print type(sixs)
# 又因为生成器（generator）也是迭代器
for x in (x for x in range(50) if x%6==0):
	print x,

# 函数
print ""
def frange(start, stop, step=1.0):# 默认参数必须放在后面
	"""
	doc-string 文档字符串，用于描述函数或者类
	"""
	result=[]
	while start < (stop - step/2.0):
		result.append(start)
		start+=step
	return result

print frange(1, 5, 0.5)

# 生成器函数
def frange_g(start, stop, step=1.0):# 默认参数必须放在后面
	"""
	doc-string 文档字符串，用于描述函数或者类
	"""
	result=[]
	while start < (stop - step/2.0):
		yield start #yield和return语句比较相似，区别在于使用yield的生成器函数
		start+=step
print list(frange_g(1,5,0.5)) # 强制将生成器对象放在列表中
for i in frange_g(1,5,0.5):
	print i,

# 有一个问题需要注意，当生成器函数完成时，并没有返回值，而是抛出一个StopIteration异常，而for和list都会自动处理这个异常
# 可以通过next()函数进行交互式研究frange_g()的抛出异常
print ""
gen = frange_g(1,2,0.5)
print gen.next()
print gen.next()
# print gen.next() 这个语句会抛出StopIteration的异常

# 匿名函数lambda函数

cube = lambda x: pow(x,3)
print cube(3)

lista = [1,2,4,5]
listb= [2,1,3,4]
print lista >= listb # Python 可以比较数据结构

# 偏函数应用程序　python 2.5版本以后　
# buttonOneFunc=functools.partial(action,"one")
# buttonTwoFunc=functools.partial(action,"Two")
# 例如在GUI编程中，或许会有数个需要调用同一个函数的按钮，不过参数化的形式是由能够发起这一调用的那个特定按钮决定的。


# 异常处理

