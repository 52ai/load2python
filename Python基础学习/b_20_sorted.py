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

#忽略大小写来实现字符串的排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

#进行反向排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

#练习

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
L2 = sorted(L,key=by_name)
print(L2)

def by_score(t):
    return t[1]

L3 =sorted(L,key=by_score,reverse=True)
print(L3)