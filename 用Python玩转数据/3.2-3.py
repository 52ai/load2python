# coding:utf-8

# series 变长字典 类似于一维数组的对象，由数据和索引组成

from pandas import Series,isnull
aSer = Series([1,2.0,'a'])
print aSer

# 数据对齐

data = {'AXP':'86.40', 'CSCO':'122.64', 'BA':'99.44'}
sindex = ['AXP', 'CSCO', 'BA', 'AAPL']
aSer = Series(data, index=sindex)
aSer.name='cnames'
aSer.index.name='volume'
print aSer
print isnull(aSer)

print 4*1999.5 - 1995-1991-2009


