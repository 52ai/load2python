# coding:utf-8
"""
Matplotlib最著名的Python绘图库，主要用于二维绘图。
绘图API--pyplot模块
集成库--pylab模块(包含numpy和pyplot中常用函数)

"""
from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
import numpy as np 
import time
import matplotlib.pyplot as plt # 使用pylab 就直接import pylab as pl


today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today) #美国运通公司最近一年股票代码
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
list1 = []
for i in range(0,len(quotes)):
	x = date.fromordinal(int(quotes[i][0]))
	y = datetime.strftime(x, "%Y-%m-%d")
	list1.append(y)

qutoesdf = pd.DataFrame(quotes, index=list1, columns=fields) # 利用index属性可以将索引改变。　日期为格里高利时间，用函数改变
qutoesdf = qutoesdf.drop(['date'], axis = 1)
# print qutoesdf

# 统计近一年每个月的股票开盘天数

listtemp = []
for i in range(0, len(qutoesdf)):
	temp = time.strptime(qutoesdf.index[i], "%Y-%m-%d")
	listtemp.append(temp.tm_mon)
# print listtemp
tempdf = qutoesdf.copy()
tempdf['month'] = listtemp
# print tempdf['month'].value_counts()
#help(temp)
closeMeansAXP = tempdf.groupby('month').close.mean()
print closeMeansAXP

listAXP = []
for i in range(1,13):
	listAXP.append(closeMeansAXP[i])
listAXPIndex = closeMeansAXP.index

# 绘制折线图
plt.plot(listAXPIndex, listAXP)
plt.show()
# 绘制散点图
plt.plot(listAXPIndex, listAXP,'o')
plt.show()
# 绘制柱状图
plt.bar(listAXPIndex,listAXP)
plt.show()


'''
t = np.arange(0.,4.,0.1)
print t
plt.plot(t,t,t,t+2,t,t**2)
plt.show()
'''
