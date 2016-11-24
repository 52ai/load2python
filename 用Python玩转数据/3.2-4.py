# coding:utf-8

# DataFrame 一个表格型的数据结构　含有一组有序的列（类似于index） 大致可以看成共享同一个index的Series集合

import pandas

data = {'name':['wangdachui','linning','Niuyun'], 'pay':[4000,5000,6000]}
frame = pandas.DataFrame(data)
print frame
frame['name'] = 'admin'
print '=========================='
print  frame['name']
print '=========================='
print frame.pay
