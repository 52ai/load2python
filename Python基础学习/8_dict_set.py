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


#set 是一组key的集合，但是不存储value.由于key不能重复，所以，在set中，没有重复的key
s = set([1,2,3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)