# coding:utf-8

"""
数据合并　merge

append（追加）, concat, join(sql类型的链接)
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

p = qutoesdf[:2]　　
print p
q = qutoesdf[u'2016-01-01':u'2016-01-05']
print q

print p.append(q)

# 将美国运通公司近一年股票数据中前五个和后五个合并
print '------------------------------------------------'
pieces = [qutoesdf[:5], qutoesdf[len(qutoesdf)-5:]]
print pd.concat(pieces)

# 两个不同逻辑结构对象也能链接　　pd.concat([piece1, piece2], ignore_index=True)

listtemp = []
for i in range(0, len(qutoesdf)):
	temp = time.strptime(qutoesdf.index[i], "%Y-%m-%d") # 取出每一行的日期
	listtemp.append(temp.tm_mon)　# 将每一行的日期中的月份添加到listtemp中
# print listtemp
tempdf = qutoesdf.copy()　# 拷贝一份qutoesdf
tempdf['month'] = listtemp　# 将拷贝新增一列month属性

piece1 = qutoesdf[:3]
piece2 = tempdf[:3]
print pd.concat([piece1, piece2], ignore_index=True)

# join   
# 使用pd.merge(djidf, AKdf, on='code')
# pd.,merge(djidf, AKdf, on='code').drop(['lasttrade'], axis=1)

