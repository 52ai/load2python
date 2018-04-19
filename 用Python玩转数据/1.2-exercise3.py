# coding:utf-8


def proc(n):
    if (n < 0):
        print '-',
        n = -n
    if (n / 10):
        proc(n / 10)
    print n % 10,

proc(-345)