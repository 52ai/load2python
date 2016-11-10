# /usr/bin/env python
# -*- coding=utf-8 -*-


from numpy import array, mat, matrix, shape, multiply

'''
Sherman-Morrison Formula

if 1 + d.T * A.inverse * c != 0:

(A + cd.T).inverse = A.inverse - (A.inverse * cd.T * A.inverse)/(1 + d.T * A.inverse * c)

'''
A = matrix([[2, 0, -1],
      [-1, 1, 1],
      [-1, 0, 1]])

A_inverse = matrix([[1, 0, 1],
              [0, 1, -1],
              [1, 0, 2]])
'''
for:
B = matrix([[2, 0, -1],
      [-1, 1, 1],
      [-1, 2, 1]])

So:
c = matrix([0, 0, 1]).T
d = matrix([0, 2, 0]).T

B_inverse = A_inverse - (A_inverse*c*d.T*A_inverse) /  (1+d.T*A_inverse*c)

'''
c1 = matrix([0, 0, 1]).T
d1 = matrix([0, 2, 0]).T

B_inverse = A_inverse - (A_inverse*c1*d1.T*A_inverse) / (1 + d1.T*A_inverse*c1)
print("B_inverse:\n %s" % B_inverse)

'''
for:
'''
C = matrix([[2, 0, -1],
            [-1, 1, 1],
            [-1, 2, 2]])
'''
So:
'''
c2 = matrix([0, 0, 1]).T
d2 = matrix([0, 2, 1]).T

C_inverse = A_inverse - (A_inverse*c2*d2.T*A_inverse) / (1 + d2.T*A_inverse*c2)
print("C_inverse:\n %s" % C_inverse)

print("C_-1:\n %s" % C**-1)








