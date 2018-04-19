# coding:utf-8
aStr = "Hello, World!"
bStr = aStr[:7]+ "Python!"
print bStr
count = 0 
for ch in bStr:
	if ch in ',.!?':
		count += 1
print 'There are %d punctuation marks.' %(count)

n = 23.3333333333
print  '%5.2f' %(n)

sStr = 'acdhdca'
if (sStr == ''.join(reversed(sStr))):
	print 'Yes'
else:
	print 'No'

if cmp(sStr,''.join(reversed(sStr))) == 0:
	print 'Yes'
else:
	print 'No'

aStr = 'Abc,Def,ghi'
print aStr.istitle()
bStr = aStr.title()
print bStr
print bStr.istitle()
print '\a'
print ord('a')
print chr(97)
print ord('e')
print '\x65'
print '\145'
print 'e'

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weeken = ['saturday', 'Sunday']
week.extend(weeken)
for i,j in enumerate(week, start = 1):
	print i,j

# 列表解析
# 动态创建列表，简单灵活有用
print [x **2  for x in range(10) if x **2 < 50]
print [(x+1, y+1) for x in range(2) for y in range(2)]

#　需要改变列表的时候可以使用列表解析

print [x for x in range(1,101) if x%5 == 0]

# 列表的元素可以改变，元组的元素不可以改变

# 元组作为函数的形式参数

def func(args1, *argst):
	print args1
	print argst

func('hello', 'Bob', 'Marry', 'Jack')

# 元组作为函数的常见返回类型　
# enumerate() coerce()

def func():
	return 1,2,3
print func()

