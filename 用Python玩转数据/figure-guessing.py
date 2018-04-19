# coding:utf-8
from random import randint

x = randint(0, 300)
print x
print "请输入一个数，范围是0到300:"
# input_number = input()
input_number = randint(0, 300)
while 1:
    if input_number == x:
        print "Bingo!游戏结束"
        break
    elif input_number > x:
        print "Too large, please try again!"
    else:
        print "Too small, please try again!"

    print "请重新输入一个数，范围是0到300:"

    # input_number = input()
    input_number = randint(0, 300)
