# coding:utf-8

"""
Matplotlib 图像属性控制如颜色、线条类型、样式(加标题，横轴和纵轴标题)
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
# 绘制图例
# plt.figure(figsize=(8,6), dpi=100)
t = np.arange(0.,4.,0.1)
plt.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line 1')
plt.plot(t,t+2,color='green',linestyle='',marker='+',linewidth=3,label='Line 2')
plt.plot(t,t**2,color='blue',linestyle='',marker='v',linewidth=3,label='Line 3')
plt.legend(loc='upper left')
plt.show()
'''
# 分别绘制子图区域
plt.subplot(211) # 两行一列第一个图
plt.plot(listAXPIndex,listAXP,color='r',linestyle='--',marker='v')
plt.subplot(212)
plt.plot(listAXPIndex,listAXP,color='g',marker='o')
plt.show()

# 子图axes

# plt.axes([left,bottom,width,height])  参数范围是[0,1]

