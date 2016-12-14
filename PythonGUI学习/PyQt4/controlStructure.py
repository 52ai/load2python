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

