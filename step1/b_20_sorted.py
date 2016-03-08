'''
Created on 2016年3月8日

@author: Wenyan Yu
'''

#Python 内置的sorted()函数就可以对list进行排序
print(sorted([36,5,-12,9,21]))

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36,5,-12,9,-21],key=abs))


#对字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))