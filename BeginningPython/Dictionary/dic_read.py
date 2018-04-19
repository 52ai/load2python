# -*- coding:utf-8 -*-
"""
Create on July 4,2016
Function: dictionary reading of python
@author:Wayne

<。)#)))≦
"""

# define dictionary
dic = {'a': "hello", 'b': "how", 'c': "are", 'd': "you"}

# The First Method to read dictionary

for key in dic:
    print key, dic[key]
    # print key + str(dic[key])

# The Secondly Method to read dictionary

for (k, v) in dic.items():
    print "dic[%s]=%s" % (k, v)

# The Thirdly Method to read dictionary

for (k, v) in dic.iteritems():
    print "dic[%s]=%s" % (k, v)

print dic.items()
print dic.iteritems()
"""
方法二和方法三的区别在于：
items()返回的是列表对象，而iteritems()返回的是iterator对象。
print dic.items():  [('a', 'hello'), ('c', 'are'), ('b', 'how'), ('d', 'you')]
print dic.iteritems():  <dictionary-itemiterator object at 0x029BFB70>

注意：iteritor是迭代器，一次返回一个数据项，直到没有为止
"""
for i in dic.items():
    print i
"""
('a', 'hello')
('c', 'are')
('b', 'how')
('d', 'you')

"""
for i in dic.iteritems():  # iteritems() iterkeys itervalues
    print i
"""
('a', 'hello')
('c', 'are')
('b', 'how')
('d', 'you')
"""