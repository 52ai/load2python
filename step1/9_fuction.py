'''
Created on 2016年3月4日

@author: Wenyan Yu
'''

import math
#函数的调用

print(abs(100))
print(abs(-20))

print(max(1,2))
print(max(2,3,1,-5))#max()可以接受任意多个参数，并返回最大的那个)
#print(max(2,a,1,-5)) 这种写法是错误的，max接受的参数必须是类型一致的才可以比较

print(int('123'),'--',int(12.34),)
print(float('12.34'))
print(str(123))
print(bool(1))
print(bool(''))

#练习
n1 = 255
n2 = 1000

print("十进制数255的十六进制表示为 ：%s" %hex(n1))
print("十进制数1000的十六进制表示为 ：%s" %hex(n2))

#函数的定义

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-100))
#print(my_abs('list'))
'''
可以使用pass语句作为占位符
比如：

if age >= 18:
    pass

如果缺少了pass，代码就会有语法错误

'''

def move(x,y,step,angle):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle) 
    return nx,ny #返回值是一个tuple

r = move(100,100,60,math.pi / 6)
print(r)

print(math.pi)


def quandratic(a,b,c):
    x = (b**2)-(4*a*c)
    
    if a == 0:
        return -(c/b)
    elif x >= 0:
        x1 = (-(b)+math.sqrt(x))/(2*a)
        x2 = (-(b)-math.sqrt(x))/(2*a)
        
        return x1,x2
    else:
        return '该方程无解'


print(quandratic(2,3,1))
print(quandratic(1, 3, -4))

#函数的参数

def power(x,n):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,3))   
    
'''

设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
'''

def enroll(name,gender,age=6,city='beijing'):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)
    
enroll('Sarah','F')
#默认参数降低了函数调用的难度


#调用可变参数

def calc(*numbers):#把函数的参数改为可变参数
    mysum = 0
    for n in numbers:
        mysum = mysum + n * n
    return mysum

#print(calc([1,2,3])) #使用的是list或者tuple作为参数

print(calc(1,2,3)) 

nums = [1,2,3]
print(calc(*nums)) #Python允许在list或tuple前面加一个*号，把list或tuple元素变成可变参数传进去

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数


def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
    
person('Michael',30)
person('Bob',35,city='beijing')
person('Adam',45,gender='M',job='Engineer')


#可以先组装出一个dict,然后把该dict转换为关键字参数传出去

extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra) 
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#命名关键字参数






