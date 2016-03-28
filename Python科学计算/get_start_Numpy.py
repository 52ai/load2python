# /usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import array

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



