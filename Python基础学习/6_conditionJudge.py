'''
Created on 2016年3月1日

@author: Wenyan Yu
'''

age = 3
if age >= 18:
    print("your age is %d" %(age))
    print('adult')
elif age >= 6:
    print("your age is %d" %(age))
    print('teenager')
else:
    print("your age is %d" %(age))
    print('kid')
    
'''
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''    
#有一个问题：int()函数发现一个字符串不是合法的数字时会报错，程序就退出了。因此需要检查并捕获程序运行期的错误

#练习
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
weight = input('请输入你的体重(kg):')
height = input('请输入你的身高(m):')
w = float(weight)
h = float(height)

bmi = w / (h**2)

print('你的BMI值为：%.2f' %bmi)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi <= 32:
    print('肥胖')
elif 32 < bmi:
    print('严重肥胖')
else:
    print('你输入错误的数值！')