'''
Created on 2016年3月8日

@author: Wenyan Yu
'''
#Python内建的filter()函数用于过滤序列
from _ast import Str
from locale import str



def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A B ','','B',None,'C',' '])))

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算，需要用list()函数获取所有结果并返回list

#用filter求素数(使用埃氏筛法)

#先构造一个从3开始的奇数序列（使用生成器）

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

#定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n >0
#最后定义一个生成器，不断返回下一个素数

def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it) #构造新的序列
        
#打印1000以内的素数

for n in primes():
    if n < 1000:
        print(n)
    else:
        break



#练习 请用filter()过滤掉非回数
'''
def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):  
        if s[i] != s[len(s)-i-1]:
            return False
    return True
'''
def is_palindrome(n):
    return  str(n) == str(n)[::-1]
   
output = filter(is_palindrome,range(1,1000))
print(list(output))


