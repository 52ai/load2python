# /usr.bin/enc python3
# -*- coding:utf-8 -*-


class Student(object):
    name = 'Student'   # 类属性，这个属性归类所有，但类的所有实例都可以访问到

s = Student()
print(s.name)
