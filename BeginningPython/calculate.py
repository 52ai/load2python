# coding=utf-8
from Module.fibo import fib

"""
这里有两种import语句：
第一种：import module_name1 [as name1], module_name2 [as name2]
第二种：from module_name import item1 [as name1], item2 [as name2]
"""

for n in range(10, 50, 5):
    fib(n)
