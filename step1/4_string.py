#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016年2月29日

@author: Wenyan Yu
'''

print('包含中文的str')

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('余'))
print(chr(66))
print(chr(25991))

#如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')

#要计算str包含多少个字符，可以用len()函数)

print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

#格式化输出

print('Hello,%s' %'word')
print('%2d-%02d' %(3,1))
print('%06.2f' %3.1415926)
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age:%s. Gender:%s' %(25,True))
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate:%d%%' % 7)

#练习

'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
'''

s1 = 72
s2 = 85

r = 100*(s2 - s1) / s1 #计算小明成绩提升的百分点

print("小明的成绩提升了：","%.1f%%" % r)