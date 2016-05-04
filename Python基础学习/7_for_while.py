'''
Created on 2016年3月2日

@author: Wenyan Yu
'''


#for...in

names = ['Michael','Bob','Tracy']
for name in names:
    print(name)

sum1 = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum1 = sum1 +x
print(sum1)

#使用range()函数可以成一个整数的序列
#使用list()函数可以转换成list

l = list(range(101))
print(l)

sum2 = 0
for x in l:
    sum2 = sum2 + x
print(sum2)

#while

sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n = n-2
print(sum3)

sum4 = 0
n = 1
while n < 100:
    if n % 2 != 0:
        sum4 = sum4 + n    
    n = n + 1
print(sum4)


#练习：请利用循环依次对list中的每个名字打印出hello,xxx!:

L = ['Bart','Lisa','Adam']

for name in L:
    print('hello,',name,'!')
