# coding:utf-8
import pandas as pd 
import numpy as np 

csv_input = pd.read_csv('4.2-5-exercise.csv')
#print csv_input
csv_input['money']=csv_input.volume * csv_input.price
print csv_input['money']
csv_input.to_csv('4.2-5-exercise.csv')