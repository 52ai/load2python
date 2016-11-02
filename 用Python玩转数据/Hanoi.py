# coding:utf-8

"""
create on Oct.25,2016 by Wayne
Function:solute the hanoi problem using recursion method
"""


def hanoi(a, b, c, n):
    """将a上n个盘子，经由b,　移动到c上,每次只能移动一个盘子，任何时刻都不能将一个较大的圆盘压在较小的圆盘之上。"""

    if n == 1:
        print a, '->', c
    else:
        hanoi(a, c, b, n-1)
        print a, '->', c
        hanoi(b, a, c, n-1)
hanoi('a', 'b', 'c', 3)