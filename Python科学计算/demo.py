# /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

print(a)
print(b)
print(c)
print(c.dtype)  # 获取数组元素的类型
print(c.shape)  # 获得数组的大小

