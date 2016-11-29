# coding:utf-8
"""
数据存取　Data Access

直接使用file的读入读出txt文件，但是对表格数据不太擅长

csv 逗号分割值
excel

"""
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd 
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('IBM', start, today)
df = pd.DataFrame(quotes)

# 写CSV文件
# df.to_csv('stockIBM.csv') # write info in csv file 

# 读CSV文件
#result = pd.read_csv('stockIBM.csv')
# print result
#print result['2']

# 写入excel文件

df.to_excel('stockIBM.xls',sheet_name='IBM')

# 读excel文件
result = pd.read_excel('stockIBM.xls')
print result
