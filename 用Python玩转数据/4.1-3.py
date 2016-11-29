# coding:utf-8

"""
数据显示　Data Display

索引(index)，列名(columns)，数据的值(values)，数据描述(describe)

"""

# coding:utf-8

"""
数据整理，好的数据整理可以给后面数据分析带来非常大的便利。

"""

# 利用pands DataFrame 给qutoes数据加属性名

from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
import numpy as np 


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
# print qutoesdf.describe
print qutoesdf.head(5) # 查看前五项数据
print qutoesdf.tail(5) # 查看后五项数据

