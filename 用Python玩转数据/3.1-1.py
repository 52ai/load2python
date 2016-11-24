# coding:utf-8
aDict = {}.fromkeys(('wang', 'zhao', 'qian'),3000)
print aDict

# aList, bList  利用　zip函数可以一步生成字典　aDict = dict(zip(aList, bList))

names = ['yuwenyan', 'billcode', 'yunzhongbuyi']
salaries = ['10000', '12000', '20000']
aDict = dict(zip(names, salaries))
print aDict

