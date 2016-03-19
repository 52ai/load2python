'''
Created on 2016年3月7日

@author: Wenyan Yu
'''
from collections import Iterator

print([x for x in range(10)])
print(isinstance((x for x in range(10)), Iterator)) 

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数


print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

#Python 的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。

#Iterator甚是可以表示一个无限大的数据流，例如全体自然数，而使用list是永远不可能存储全体自然数的

'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

'''
#Python的for循环本质上就是通过不断调用next()函数实现的

for x in list(range(5)):
    print(x)

#等价于


it = iter(list(range(5)))

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
    
    
    
#输出全体整数

def iterator():
    i=1
    while True:
        yield i
        i += 1
o = iterator()

while True:
    try:
        x = next(o)
        print(x)
    except StopIteration:
        break

