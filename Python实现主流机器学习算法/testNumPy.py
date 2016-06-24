from numpy import *
randMat = mat(random.rand(4, 4))  # produce a random 4*4 matrix
print randMat

invRandMat = randMat.I
print invRandMat  # deduce inverse of matrix

myEye = randMat * invRandMat
print myEye

print myEye - eye(4)  # seek error value  && eye(4) create a 4*4 identity matrix
