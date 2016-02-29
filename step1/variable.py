'''
Created on 2016年2月29日

@author: Wenyan Yu
'''

a = 123 #a is a Integer
print(a)
a = 'ABC' # a is a String
print(a)
'''
    在Python中，同一个变量可以反复赋值，而且可以是不同类型的变量。这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言，如java.
'''

a = 'ABC'
b = a
a = 'XYZ'
print(a)
print(b)

#在Python中，通常用全部大写的变量名表示常量

PI = 3.14159265359
print(PI)