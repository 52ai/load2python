# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 在python中，一个.py文件就称之为一个模块(Module)
# using module

'a test module'
import sys



__author__ = 'Michael Liao'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
    print(__doc__)


'''
在python中
__XXX__这样的变量是特殊变量，可以直接引用，但是有特殊用途，比如__author__ __name__  __doc__
_XXX和__XXX这样的函数或者变量就是非公开的(private)，不应该被直接引用

'''


