'''
Created on 2016年3月9日

@author: Wenyan Yu
'''


#因为一个《大秦帝国》，让我荒废了三天的时间,此时需要好好的反省

import functools

def log(func):
    @functools.wraps(func)   #需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
    def wrapper(*args,**kw):
        print('call %s:' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log    #now = log(now)
def now():
    print('2016-3-13')

f = now
print(f())

#函数对象有一个_name_属性，可以拿到函数的名字

print(now.__name__)
print(f.__name__)

#今天跑步，欠下一天~~~~~~2016.3.14

#在代码运行期间动态增加功能的方式，称之为装饰器（Decorator）

now()
print(now.__name__)




