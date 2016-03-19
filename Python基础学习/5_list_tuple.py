'''
Created on 2016年2月29日

@author: Wenyan Yu
'''

#list 是 Python 内置的数据类型

classmates = ['Michael','Bob','Tracy']
print(classmates)

#变量classmates就是一个list。用len()函数可以获得list元素的个数
print(len(classmates))
#用索引来访问list中的每一个位置的元素，索引是从0开始的
print(classmates[0])

#要取最后一个元素，除了计算索引位置以外，还可以用-1做索引，直接获取最后一个元素
#以此类推可以获取，倒数第二个（-2），倒数第三个（-3）
print(classmates[-1])
print(classmates[2])


#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'Jack')
print(classmates)

#要删除list末尾的元素
classmates.pop()
print(classmates)

#要删除指定位置的元素
classmates.pop(1)
print(classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarch'
print(classmates)

#list里面的元素的数据类型也可以不同,list元素也可以是另外一个list
s = ['python','java',['asp','asp.net'],'php','scheme']
print(len(s))
print(s[2][1])

#如果一个list中一个元素也没有，就是一个空的list，它的长度是0
L = []
print(len(L))

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates = ('Michael','Bob','Tracy')

#定义只有一个元素的tuple必须加一个逗号，来消除歧义
t = (1,)
print(t)

t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'

print(t)

#练习
'''
    请用索引取出下面list的指定元素：

# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
'''

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


#小结：list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择他们