# coding:utf-8

"""
求微软公司(MSFT)2016年第一季股票收盘价平均值
"""
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

today = date.today() # 获取今天日期
start = (today.year-2, today.month, today.day) # 设置开始时间　2年前
quotesMS = quotes_historical_yahoo_ochl('MSFT', start, today) # 获取数据
attributes=['date','open','close','high','low','volume'] # 添加属性值
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes) # 生成DataFrame格式数据
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0])) # 将格里高利历转换为时间
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfMS.index = list # 将时间变成数据的索引值
quotesdfMS = quotesdfMS.drop(['date'], axis = 1) # 去掉原有的日期项

list = []
quotesdfMS16 = quotesdfMS['16/01/01':'16/04/01'] # 选择第一季度数据

for i in range(0, len(quotesdfMS16)):
    list.append(int(quotesdfMS16.index[i][3:5])) #get month just like '02'

quotesdfMS16['month'] = list
print(quotesdfMS16.groupby('month').mean().close)