# -*- coding:utf-8 -*-
# ##################################################
# 函数：LU分解，QR分解， Householder约减，Givens约减
# 作者：余文艳(2015E8007361074)
# 日期：2016.5.17
# 输入：矩阵A
# 输出：所选择矩阵A对应分解或约减后的结果
# 实例：A=[2 0 -1; -1 1 1; -1 2 2]
#       A=[1 2 -3 4; 4 8 12 -8; 2 3 2 1; -3 -1 1 -4]
#
# 支持特性：1.支持n*n矩阵 2.支持浮点型运算
# ###################################################
from numpy import matrix


def lu_factor(data):
    print "----------LU----------"
    [n,n] = data.shape
    # print n
    L = matrix([[0.0] * n for i in xrange(n)])
    U = matrix([[0.0] * n for i in xrange(n)])

    print L
    print U
    



def qr_factor(data):
    print "QR"
    print data


def householder_reduction(data):
    print "Householder"
    print data


def givens_reduction(data):
    print "Givens"
    print data

"""

print "温馨提示：1.请保证您正处于英文输入状态 2.请您参照下面给出的说明进行相应操作"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print "请您选择所需要进行的变换：（输入变换前的阿拉伯数字即可1、2、3、4）"
print "【1】LU 分解"
print "【2】QR 分解"
print "【3】Householder 约简"
print "【4】Givens 约简"

inputNum = int(raw_input("请选择："))
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
# print inputNum

inputMatrix = raw_input("请输入一个矩阵：（同一行元素用空格隔开，不用行用分号隔开，例如：1 2 3; 3 4 5; 6 7 8）>")
if not inputMatrix.strip():
    inputMatrix = raw_input("输入矩阵不能为空,请重新输入> ")

inputMatrix = inputMatrix.split(';')

data = []
for ele in inputMatrix:
    data.append(map(float, ele.strip().split(' ')))

data = matrix(data)

if inputNum == 1:
    lu_factor(data)
elif inputNum == 2:
    qr_factor(data)
elif inputNum == 3:
    householder_reduction(data)
elif inputNum == 4:
    givens_reduction(data)
"""

data = matrix('2 2 2; 4 7 7; 6 18 22') 
lu_factor(data)

print data
