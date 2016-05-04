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

print(10 / 3)
print(9 / 3)
print(10 // 3) #//除法只取结果的整数部分
print(10 % 3) #取余运算，很多语言里都有，就不要多说了



#练习

print('n = 123')
print('f = 456.789')
print("s1 = \'Hello,world\'")
print("s2 = \'Hello,\\\'Adam\\\'\'")
print("s3 = r\'Hello,\"Bart\"\'")
print('''s4 = r\'\'\'Hello,
Lisa!\'\'\'''')

'''
    Python的整数没有大小限制，Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf(无限大)
'''

