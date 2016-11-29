# coding:utf-8

"""
数据的选择

选择行，选择列，选取区域，筛选（条件选择）
"""

from matplotlib.finance import quotes_historical_yahoo_ochl  # 注matplotlib包里已经没有了quotes_historical_yahoo方法了，改为quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 


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
print qutoesdf
#print qutoesdf['2015-12-02':'2015-12-06']  # 选择行
#print qutoesdf['open'] # 选择列
#print qutoesdf.open # 选择列

# 使用label(loc)来选择行
print qutoesdf.loc['2015-12-02':'2015-12-06']
#使用label(loc)来选择列
print qutoesdf.loc[:,['open','close']]
# 使用label(loc)来选择区域
print qutoesdf.loc['2015-12-02':'2015-12-06',['open','close']]
# 使用label(loc)来选择单个数据
print qutoesdf.loc['2015-12-02','open']
# 使用label(at)来选择单个数据
print qutoesdf.at['2015-12-02','open']


# 使用iloc 基于位置来选择

print qutoesdf.iloc[len(qutoesdf)-1:len(qutoesdf),[0,1,2]]

# 使用iat 基于位置来选择单个值
print qutoesdf.iat[len(qutoesdf)-1,0] # 记得计数从0开始

# 条件筛选

print qutoesdf[(qutoesdf.index >= u'2014-11-23') & (qutoesdf.close >= 80)]

