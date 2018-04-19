# coding:utf-8
import numpy as np
from pandas import Series, DataFrame
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print a[2].sum()
print sorted(set('You need Python.'))

sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])
print sa.equals(sc)
print sb.equals(sa)


data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print frame['IDE']
aList = ['VS','Sublime']

print  'VS' in frame['IDE'] # frame['IED']是一个Series 
print 'VS' in aList