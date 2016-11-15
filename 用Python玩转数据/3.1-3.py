# coding:utf-8

# set 

# create set

aSet = set('hello')
print aSet

fSet = frozenset('hello')
print fSet

print type(aSet)
print type(fSet)


print 'a' in aSet

print aSet == fSet

print aSet <= fSet
print aSet < fSet

# & | - ^(亦或)

setA = set('Hello, World!')
setB = set('Hello, Python!')
print setA - setB
print setA ^ setB

# function 
# 1.面向所有集合 s.issubset(t) issuperset(t) union(t) intersection(t) difference(t) symmetric_difference(t) copy()
# 2.面向可变集合 update(t) intersection_update(t) add(obj) remove(obj) discard(obj) pop() clear

print help(set.remove)
print help(set.discard)

'''
remove(...)
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

None
Help on method_descriptor:

discard(...)
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.
'''


