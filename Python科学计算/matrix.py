# /usr/bin/env python
# -*- coding=utf-8 -*-

from numpy import array, mat, matrix, shape, multiply

a = matrix([[1, 1, 1],
            [1, 2, 2],
            [1, 2, 3]])

a_inverse = matrix([[2, -1, 0],
                   [-1, 2, -1],
                   [0, -1, 1]])

print(a*a_inverse)

print(a**-1)


b = matrix([[2, 0, -1],
            [-1, 1, 1],
            [-1, 2, 1]])

print(b**-1)
