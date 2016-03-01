'''
Created on 2016年3月2日

@author: Wenyan Yu
'''

#dict 使用键-值对(key-value)存储
d = {'Michael':95,'Bob':75,'Tracy':85}

print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])


#两种方法判断key是否存在

print('Thomas' in d)
print(d.get('Thomas','不存在该key'))

#删除一个key
d.pop('Bob')
print(d)