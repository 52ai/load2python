# coding:utf-8
"""
tuple(不变)
list
dict
set
frozenset（不变）

array(无法保存对象的引用，但是可以保存特定类型的数字)

"""

seta = set(("yu", "wen", "yan"))
print seta
seta.add("yu")
print seta

setb = set(("wen","yan"))

print seta >= setb # seta.issuperset(setb) setb.issubset(seta)
print seta | setb # seta.union(setb)
print seta & setb # seta.intersection(setb)
print seta - setb # seta.difference(setb)

print "way" not in seta
print "yu" in setb

print dir(seta) # dir()返回一个对象x的大部分属性列表，包括它的全部的方法名
help(seta.issubset) #help可以查看该对象某个方法的帮助说明
#help(seta.union)
#help(seta)

"""
setc = seta.copy() # 默认情况下set的=赋值是深复制，但是可以通过s.copy()获得set s 的一个浅赋值(shallow copying)
setc.clear()
print seta
print id(seta) # 返回对象引用seta的唯一ID 
print id(setc)
"""
"""
lista = ["yu", "wen", "yan"]
listb = lista
listb[0]=[""]
print lista
print id(lista)
print id(listb) # 通过带一个由整个列表构成的切片可以强迫python执行深复制(deep copying)
"""
print isinstance(seta, set) #如果a是类C的一个实例，或者是类C的一个子类，则返回True
print type(seta) # 返回seta的类型
a=1
b=1
print eval("a+b+a*b+a+1000") # 返回计算字符串s后的结果，s可以包含任意的python　表达式

'''
与数学相关的函数
'''
print divmod(100,33) # 返回一个元组，商和余数

print hex(100) # 将数字转换为16进制
print oct(18) # 数字转化为8进制

print round(100.5999) # 对小数点后面的数字四舍五入取整，也就是做简单的圆整

c=5
d=c
print id(c)
print id(d)
d=6
print c
print id(c)
print id(d)

#对于变量的赋值，默认为浅复制，就如上所示最开始c和d引用同一个对象id相同，但是当需要改变d的值时由于默认是浅复制，因此id号也随之改变