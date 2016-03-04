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



