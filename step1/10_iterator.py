'''
Created on 2016年3月6日

@author: Wenyan Yu
'''

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))


#练习

def move(n,a,b,c):
    