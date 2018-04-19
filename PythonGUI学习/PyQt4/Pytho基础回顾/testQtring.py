#coding:utf-8
from PyQt4.QtCore import *
import sys
a= QString("apple")
b=unicode("baker")
print a+b
print type(a+b)
print a,b # print 语句会自动在它输出的参数之间多输出一个空格
sys.stdout.write(a+b)