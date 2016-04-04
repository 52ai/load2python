# /usr/bin/env python
# -*- coding=utf-8 -*-


from numpy import array, mat, matrix, shape, multiply

A = matrix([[1, 1, 1],
            [1, 2, 2],
            [1, 2, 3]])

a_inverse = matrix([[2, -1, 0],
                   [-1, 2, -1],
                   [0, -1, 1]])

print(A*a_inverse)

print(A**-1)


b = matrix([[2, 0, -1],
            [-1, 1, 1],
            [-1, 2, 1]])

print(b**-1)


c = matrix([[1, 4, 5],
            [4, 18, 26],
            [3, 16, 30]])
d = matrix([112, -39, 10]).T
print(c*d)
e = matrix([[1, 3, 1, -4], [-1, -3, 1, 0], [2, 6, 2, -8]])

print(e*e.T)