# coding:utf-8
"""
聚类分析　cluster

1.K-means k均值聚类算法，简单够用
"""
from pylab import *
from scipy.cluster.vq import *

list1 = [88, 64, 96, 85]
list2 = [92, 99, 95, 94]
list3 = [91, 87, 99, 95]
list4 = [99, 99, 97, 81]
list5 = [88, 78, 98, 84]
list6 = [100, 95, 100, 92]

data = vstack((list1, list2, list3, list4, list5, list6))
print data
whitened = whiten(data) # normalization data
# print whitened
centroids,dist = kmeans(whitened,2) # obs　必须是使用whiten函数之后的features k表示聚类成类
# print centroids
result,dist = vq(whitened,centroids)
print result

#result,= vq(data, centroids)
# print result