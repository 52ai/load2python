'''
Created on 2016年3月6日

@author: Wenyan Yu
'''

#回顾 构造一个1,3,5,7,....,99的列表

L = []
n = 1
count = 0
while n < 99:
    L.append(n)
    n = n + 2
    count = count + 1

print(L)
print(count)

# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环

r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

#使用切片完成上述操作
print(L[0:3])#如果第一个索引是0，可以直接简写为L[:3]

print(L[-2:])
print(L[-2:-1])#记住倒数第一个元素的索引是-1

#切片实例

L = list(range(100))
print(L)

print(L[:10])#取前10个数
print(L[-10:])#取后10个数
print(L[10:20])#取前11到20个数
print(L[:10:2])#前10个数每两个取一个
print(L[::5])#所有的数每5个取一个

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作
s = "ABCDEFGHIJKLMNOPQRSPUVWXYZ"
print(s[:18])

#迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(d[key])
for value in d.values():
    print(value)
for a,b in d.items():
    print(a,b)



from collections import Iterable
print(isinstance('abc', Iterable))#判断str是否可以迭代


#Python内置的enumerate函数可以把一个list变成索引-元素对

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)


#总结：任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。




