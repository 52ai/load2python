'''
Created on 2016年3月4日

@author: Wenyan Yu
'''

#函数的调用

print(abs(100))
print(abs(-20))

print(max(1,2))
print(max(2,3,1,-5))#max()可以接受任意多个参数，并返回最大的那个)
#print(max(2,a,1,-5)) 这种写法是错误的，max接受的参数必须是类型一致的才可以比较

print(int('123'),'--',int(12.34),)
print(float('12.34'))
print(str(123))
print(bool(1))
print(bool(''))

#练习
n1 = 255
n2 = 1000

print("十进制数255的十六进制表示为 ：%s" %hex(n1))
print("十进制数1000的十六进制表示为 ：%s" %hex(n2))