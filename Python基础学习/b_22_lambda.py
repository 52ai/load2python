'''
Created on 2016年3月9日

@author: Wenyan Yu
'''

#有时候可以不显示的定义函数，直接传入匿名函数更加的方便

#计算f(x)= x**2

print(list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9])))

f = lambda x:x**2
print(f(5))

#python 对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数

#也可以把匿名函数作为返回值返回

def build(x,y):
    return lambda:x*x + y*y

def mybuild(x,y):
    return x*x + y*y


f1 = build(1, 2)
print(f1())
f2 = mybuild(3,4)
print(f2)




