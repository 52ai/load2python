# /usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import array, mat, matrix, shape, multiply

mm = array((1, 1, 1))
pp = array((1, 2, 3))

print(mm + pp)
print(pp*2)
print(pp**2)
print(pp[1])

jj = array([[1, 2, 3], [1, 1, 1]])
print(jj[0])
print(jj[0][1])
print(jj[0, 1])

a1 = array([1, 2, 3])
a2 = array([0.3, 0.3, 0.3])
print(a1*a2)


ss = mat([1, 2, 3])
print(ss)

mm = matrix([1, 2, 3])
print(mm)

print(mm[0, 1])  # 可以访问矩阵中的单个元素

pyList = [5, 11, 1605]
mat(pyList)  # 可以把Python列表转换成Numpy矩阵

print(mm*ss.T)  # 这里调用了矩阵的T方法完成矩阵的转置

print(shape(mm))  # 通过shape方法来查看矩阵或者数组的维数

print(multiply(mm, ss))  # 对应元素相乘的方法
