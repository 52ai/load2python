'''
Created on 2016年3月9日

@author: Wenyan Yu
'''


#因为一个《大秦帝国》，让我荒废了三天的时间,此时需要好好的反省

def now():
    print('2016-3-13')

f = now
print(f())

#函数对象有一个_name_属性，可以拿到函数的名字

print(now.__name__)
print(f.__name__)

#今天跑步，欠下一天~~~~~~2016.3.14

