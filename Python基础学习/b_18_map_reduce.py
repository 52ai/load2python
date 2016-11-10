'''
Created on 2016年3月7日

@author: Wenyan Yu
'''
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上

def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])

print(r)
print(list(r))


print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce()：把一个函数作用在一个序列[x1,x2,x3,x4,x5,x6,x7,x8....]上，这个函数必须接受两个参数
#reduce()把结果继续和序列的下一个元素做累积计算

#效果如右边：reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

#用reduce() 实现对一个序列求和   

from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))

#求和运算其实可以直接使用sum()函数，但是要把序列[1,3,5,7,9]变换成整数13579,reduce就派上用场了
def fn(x,y):
    return x*10 + y
print(reduce(fn,[1,3,5,7,9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn,map(char2num,'13579')))


#整理成一个str2int函数

def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('123456789'))
#print(str2int('qwe')) 这样写会出错，函数内部没有做异常处理

#还可以使用lambda函数进行进一步简化

def char_2_num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str_2_int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str_2_int('123456789'))


#练习一

def normalize(name):
    
    return name[0].upper()+name[1:len(name)].lower()

L1 = ['adam', 'LISA', 'barT'] 
L2 = list(map(normalize,L1))
print(L2)

#练习二


def prod(L):
    
    def subprod(x,y):
        return x*y
    return reduce(subprod,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#练习三

def str2float(s):
    
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s] 
    def fn(x,y):
        return x*10 + y
    if s.find(".") == -1:
        return reduce(fn,(map(char2num,s)))
    else:
        return reduce(fn,(map(char2num,s[:s.find(".")])))+reduce(fn,(map(char2num,s[s.find(".")+1:])))/10**s.find(".")
    return reduce(fn,map(char2num,s))   
print('str2float(\'123.456\')=',str2float('123.456'))