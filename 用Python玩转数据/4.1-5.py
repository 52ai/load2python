# coding:utf-8

"""
数据的简单处理与筛选

"""
from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
import numpy as np 
import time


today = date.today()
start = (today.year - 5, today.month, today.day)
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

#求平均值
print qutoesdf.mean(columns='close')
#求开盘价大于80的成交量

print qutoesdf[qutoesdf.open >= 80].volume
#求开盘价大于80的日期
print qutoesdf[qutoesdf.open >= 80].index

# 统计运通公司近一年股票涨和跌的天数
print "跌：",len(qutoesdf[qutoesdf.close > qutoesdf.open])
print "涨：",len(qutoesdf[qutoesdf.close < qutoesdf.open])
print "平：",len(qutoesdf[qutoesdf.close == qutoesdf.open])

# 统计运通公司近一年相邻两天收盘价的涨跌情况
status = np.sign(np.diff(qutoesdf.close))
# print status
# print len(status)
print status[np.where(status == 1)].size
print len(status[np.where(status == -1)])

# 排序
# 前三甲
print qutoesdf.sort_values(by='open',ascending=False).loc[:,['open']].head(3)
# help(qutoesdf.sort)

# 统计2016年1月份的股票开盘天数

t = qutoesdf[(qutoesdf.index >= '2016-01-01') & (qutoesdf.index <= '2016-02-01')]
print len(t)

# 统计近一年每个月的股票开盘天数

listtemp = []
for i in range(0, len(qutoesdf)):
	temp = time.strptime(qutoesdf.index[i], "%Y-%m-%d")
	listtemp.append(temp.tm_year)
print listtemp
tempdf = qutoesdf.copy()
tempdf['year'] = listtemp
print tempdf['year'].value_counts()
help(temp)
