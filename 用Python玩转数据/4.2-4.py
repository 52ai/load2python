# coding:utf-8

"""
pandas 作图
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
'''
# 绘制折线图
# plt.figure(figsize=(8,6), dpi=100)
plt.plot(listAXPIndex, listAXP,'r--')

plt.title('Stock Statistics of AXP')
plt.xlabel('Month')
plt.ylabel('Average Close Price')
plt.show()
help(plt.plot)

'''

'''
plt.plot(closeMeansAXP,'r--')
# closeMeansAXP.plot()
plt.title('Stock Statistics of AXP')
plt.xlabel('Month')
plt.ylabel('Average Close Price')
plt.show()

print type(closeMeansAXP)
'''


qutoesdf.close.plot()
plt.show()

#qutoesdf_temp = pd.DataFrame()
#qutoesdf_temp['open'] = qutoesdf['2016-01-01':'2016-01-16'].open
#qutoesdf_temp['close'] = qutoesdf['2016-01-01':'2016-01-16'].close
# qutoesdf_temp.plot(kind='bar')
# qutoesdf_temp.plot(kind='bar',stacked=True)
# qutoesdf_temp.plot(kind='barh')
# qutoesdf_temp.plot(kind='scatter',x='open',y='close',color='g')
# qutoesdf_temp.plot(kind='kde') # 显示概率分布
# plt.show()
