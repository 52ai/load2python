# coding:utf-8
# coding:utf-8

"""
数据分组groupby

"""
from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
import numpy as np 
import time


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
print listtemp
tempdf = qutoesdf.copy()
tempdf['month'] = listtemp
# print tempdf['month'].value_counts()
#help(temp)
print tempdf.groupby('month').count().loc[:,['open',]]

# 统计近一年每个月的总成交量

# print tempdf.groupby('month').sum().volume  
print tempdf.groupby('month').volume.sum()  # 先分组再计算，可以减少很多无用的计算

# sum() mean() min() man()
# help(tempdf)

a = np.array([[1,2,3],[4,5,6]])
print a.mean()
print a.min()
print a.sum()
print a.max()
