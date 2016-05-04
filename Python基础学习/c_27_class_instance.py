# !/usr/bin/enc python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)


bart.print_score()
lisa.print_score()

print("Bart's grade is \"%s\" " % bart.get_grade())
print("Lisa's grade is \"%s\" " % lisa.get_grade())

# 与静态语言不同，Python允许对实例变量绑定任何的数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但是拥有的变量名称都可能不同
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

# print(bart.__name)
# print(bart._Student__name)

# 总的来说，python本身没有任何机制阻止你干坏事，一切全靠自觉

# 查看所有的实例变量
print(dir(bart))

