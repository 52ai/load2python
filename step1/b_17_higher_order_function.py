'''
Created on 2016年3月7日

@author: Wenyan Yu
'''

#变量可以指向函数

x = abs(-10)
print(abs(-10))#abs()表示的是函数调用
print(abs) #abs表示的是函数本身
print(x)#要获得函数调用结果，可以把结果赋值给变量

f = abs #函数本身也可以赋值给变量，即：变量可以指向函数
print(f(-10))


#函数名也是变量

#传入函数

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))

#把函数作为参数传入，这样的函数成为高阶函数，函数式编程指的这种高度抽象的编程范式


#评论团练习

from math import sqrt

def same(x,*fs):
    s = [f(x) for f in fs]
    return s 
print(same(2,sqrt,abs))


