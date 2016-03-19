'''
Created on 2016年3月7日

@author: Wenyan Yu
'''

#列表生成式 List Comprehensions

print(list(range(1,11)))


L = []
for x in range(1,11):
    L.append(x**2)
    
print(L)

#使用列表生成式

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2 == 0])

#使用两层循环，可以生成全排列

print([m + n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下所有的文件和目录名

import os #导入os模块

print([d for d in os.listdir('.')]) # os.listdir 可以列出文件和目录

#for 循环可以同时使用两个甚至多个变量比如dict的items()可以同时迭代key和value

d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

print([k + '=' + v for k,v in d.items()])


LL = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in LL])
 

#练习

L2 = ['Hello', 'World', 18, 'Apple', None]
L3 = [s.lower() for s in L2 if isinstance(s,str)]
print(L3)

