'''
Created on 2016年3月9日

@author: Wenyan Yu
'''


#函数作为返回值

#实现一个可变参数的求和，通常情况下是这么定义的

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#但是如果不需要立刻求和，而是在后面的代码中，根据需要再计算，则可以不返回求和结果，而是返回求和函数
def lazy_sum(*args):
    def mysum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return mysum


f1 = calc_sum(1,3,5,7,9)
print(f1) #返回的是和

f2 = lazy_sum(1,3,5,7,9)
print(f2) #返回的是和函数

print(f2()) #调用函数f时，才真正计算求和的结果

#上述lazy_sum()的这种程序结构成为“闭包”

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1() == f2())
print(f1 == f2)

#闭包

#返回的函数并没有立刻执行，而是知道调用f()才执行的

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

#返回闭包是要牢记一点就是：返回函数不要引用任何的循环变量，或者后续会发生变化的变量

#如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量的当前值
'''
def mycount():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
'''
def mycount():
    f = lambda j:lambda:j*j    # lambda [input]:[output]
    fs = []
    for i in range(1,4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f3,f4,f5 = mycount()
print(f3(),f4(),f5())