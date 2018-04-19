# -*- coding:utf-8 -*-
"""
Create on July 4,2016
@author:Wayne
Function:sorted

<。)#)))≦

"""
import operator
"""
Python 内置的排序函数sorted可以对list或者iterator进行排序

sorted(iterable[, cmp[, key[, reverse]]])

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

(1)iterable 指定要排序的list或者iterable
(2)cmp为函数，指定排序时进行比较的函数，可以指定一个函数或者lambda函数
(3)key为函数，指定取待排序元素的哪一项进行排序。可以用operator.itemgetter(2)实现，取第三个域。
(4)reverse参数是个bool变量，表示升序还是降序排列，默认为false（升序排列）
"""
a = [1, 2, 3]
b = operator.itemgetter(1)
print b(a)


students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print sorted(students, key=operator.itemgetter(2), reverse=False)
print sorted(students, key=lambda student:student[2], reverse=False)
