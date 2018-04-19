'''
Created on 2016.02.29

@author: Wenyan Yu
'''
a = (1.2e-5)*10
print(a)
print('abc')
print("a'bc")
print('I\'m \"OK\"!')
print("I\'m \"OK\"!")

#换行符、制表符以及转义符转义的情况
print('\\\ta\ta\ta\ta\n\\\ta\ta\ta\ta')

#默认不转义的情况
print('\\\t\\')
print(r'\\\t\\')

#Python允许使用'''...'''的格式表示多行内容
print(r'''line1
line2
line3''')

#布尔值
print(3>2)
print(3>5)

print(True and True)
print(not True)

#布尔值也经常用在条件判断中
age = input('请输入年龄：\n')
age = int(age)
if age >= 18:
    print('adult')
else:
    print('teenager')
