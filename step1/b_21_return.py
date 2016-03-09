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