# coding:utf-8

'''
ndarry

'''

from numpy import *

aArray = array([1, 2, 3])
print aArray
bArray = array([(1, 2, 3), (4, 5, 6)])
print bArray

print zeros((3, 3))

print arange(1,1000, 10)

aArray = array([(1,2,3),(4,5,6),])
print aArray

print sin(aArray)

print aArray.shape
bArray = aArray.reshape(3, 2)
print bArray

print aArray.sum()
print aArray.sum(axis = 0)
print aArray.sum(axis = 1)

cArray = array([1,3,5])
print cArray
print cArray[:1]
dArray = array([2,4,6])
eArray = array([7,8,9])
print where(cArray > 2, dArray, eArray) # 条件成立则取dArray条件，条件不成立，则取eArray的值。

def fun(x,y):    # Construct an array by executing a function over each coordinate.
	return (x+1)*(y+1)

arr = fromfunction(fun, (9,9))

print arr

"""
ufunc（universal function） 函数是一种可以对数组每个元素都进行操作的函数。NumPy内置的许多ufunc函数都是在C语言级别实现的，计算速度非常的快

"""
print help(ufunc) 

print list(range(1, 49, 2))
# print np.linspace(1, 50, 25, dtype=int)