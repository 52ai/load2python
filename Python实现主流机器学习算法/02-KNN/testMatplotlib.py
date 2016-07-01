# coding = utf-8

import matplotlib.pyplot as plt
from numpy import *
from knn import *

datingDataMat, datingLabels = file_to_matrix('datingTestSet2.txt')
# print datingDataMat
# print datingLabels
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.show()
