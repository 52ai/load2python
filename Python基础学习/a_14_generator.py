'''
Created on 2016年3月7日

@author: Wenyan Yu
'''

#在Python中，有一种一边循环一边计算的机制，称为生成器：generator。

#如何创建一个generator

#方法一：只要把列表生成式的[]改成()
print([x*x for x in range(10)])
g=(x*x for x in range(10))
print(g)#这种方法打不出了

for n in g:
    print(n)


def fib(maxnum):
    n,a,b = 0,0,1
    while n < maxnum:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'

fib(10)

#方法二：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def generator_fib(maxnum):
    n,a,b = 0,0,1
    while n < maxnum:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'


for n in generator_fib(6):
    print(n)
    
#要想拿到generator的return语句的返回值，就需要捕获StopIteration错误


g = generator_fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
    

#练习
'''
杨辉三角定义如下：

          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
'''

def triangles():
    l =[1]
    yield l
    while True:        
        l = [1] +[l[i] + l[i+1] for i in range(len(l) - 1)] + [1]
        yield l
    
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break