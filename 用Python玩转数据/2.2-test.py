# coding:utf-8
import math
# ======序列类型函数 ==================

# enumerate() , reversed(), sorted(), zip()

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons, start = 1))

# equivalent to a function 

# reversed() return a reverse iterator.seq
print list(reversed(seasons)) 

seasons = ['abc', 'bc', 'cdefg', 'd']
print sorted(seasons)
print sorted(seasons, key = len)
print sorted(seasons, key = len, reverse=True)

# zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
z = [9, 10, 11]

print zip()
print zip(x) # with a single sequence argument, it return a list of 1-tuples.
print zip(x, z)
print zip(x, y, z)

# ================字符串链接方法=================
#join() strip() replace() split() translate() startswith()

# join() 用于将序列中的元素以指定的字符链接成一个新的字符串

aStr = 'abc'
bStr = 'def'
cStr = '-'.join(aStr)
print cStr

# strip() return a copy of the string with the leading and trailing characters removed.
# The chars argument is a string specifying the set of characters to be remove. if omitted or None, the chars argument defaults to removing whitespace.

print '   wayne   '.strip()
print 'www.mryu.top'.strip('topw.')

aStr = 'i am Wayne, nice to see you Marry.Don\'t call me Wayne, you can call me YanYan!'
print aStr.replace('Wayne', 'Yuwenyan')
print aStr
print aStr.replace('Wayne', 'Yuwenyan', 1) # if the option argument count is give, only the first count occurences are replaced

# split() 
# translate()

print 'read this short text'.translate(None, 'aeiou')

# startswith() return True if string starts with the prefix, otherwise return False.

print aStr.startswith('am', 2)

# ===============列表类型方法=================
# append() count() extend() insert() pop() sort()

aList = ['a', 'b', 'c', 'd','abca', 'a']
print aList.count('abc')
aList.append('abc')
print aList
aList.extend('abc')
print aList

aList.insert(1, '111111111')
print aList
aList.pop(1)
print aList
aList.sort()
print aList

word= 'cloud'
print min(word)

print [5]*2
print 'Merry Xmas' + '12.25'

lan = list('PHP')
lan[1:] = 'ython'
print lan

print '%05.3f' % math.pi

print (1, 2) is zip(range(4), range(2,6))
print range(4)
print range(2, 6)

words = ['life', 'is', 'short', 'you', 'need', 'python']
print words.index('you')

x = [2, 3 ,0, 4, 1]
x.sort()
print x

print 'Life is short, you need Python.'.find('you')
print 'yous' in 'Life is short, you need Python.'
seq = '1234'
sep = '+'
print '+'.join(seq)
my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]
print my_list

print ord(str(0))
print ord('a')
print list('Life is short, you need Python.')