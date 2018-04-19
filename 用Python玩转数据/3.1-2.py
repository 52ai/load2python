# coding:utf-8

names = ['yuwenyan', 'billcode', 'yunzhongbuyi']
salaries = ['10000', '12000', '20000']
aDict = dict(zip(names, salaries))
print aDict

for key in aDict.keys():
	print 'name=%s, salary=%s' %(key, aDict[key])

print "yuwenyan's salary is %(yuwenyan) s." % aDict # %(keys)s

# 输出模板

template = '''
	Welcome to the pay wall.
	yuwenyan's salary is %(yuwenyan)s.
	billcode's salary is %(billcode)s.
	...

'''

print template % aDict

print aDict.keys()
print aDict.values()

print aDict.get('wenyan') # This methods is more friendly!It can return error information.
# print aDict['wenyan']

# a very stronger function update()

bDict = {"yuwenyan": 15000, "billcode": 16000, "wayne": 50000}
aDict.update(bDict)
print aDict


# 1.dict = {} 2.dcit.clear() function is more effective

cDict = bDict
# bDict = {}
print cDict
bDict.clear()
print cDict


"""
Some function about Dict

clear()
fromkeys()
get()
has_key()
items()
keys()
iter()
pop()
setdefault()
update()
values()

"""

# 字典作为函数的形式参数

def func(args1, *argst, **argsd):
	print args1
	print argst
	print argsd

func('hello,', 'yuwenyan','billcode', 'wayne', a=1,b=2,c=3) # －－－可变长位置参数，可变长关键字参数

