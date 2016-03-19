'''
Created on 2016年3月6日

@author: Wenyan Yu
'''

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(10))


#练习 汉诺塔问题

mycount = 0
def move(n,a,b,c):
    global mycount
    if n == 1:
        mycount = mycount + 1
        print("#第%d次移动： %s -- > %s" %(mycount,a,c))
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(3,'A','B','C')
    