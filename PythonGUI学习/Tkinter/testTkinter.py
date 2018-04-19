# !/usr/bin/python
# coding:utf-8

from Tkinter import *


def process_ok():
        print "OK button is clicked."


def process_cancel():
        print "Cancel button is clicked"


# 创建一个窗口
top = Tk()

# 创建两个列表
li = ['C', 'python', 'php', 'html', 'sql', 'java']
movie = ['CSS', 'jQuery', 'Bootstrp']
# 创建两个列表组件
listbox1= Listbox(top)
listbox2= Listbox(top)

btn1 = Button(top)

for item in li:
    listbox1.insert(0,item)

for item in movie:
    listbox2.insert(0,item)

listbox1.pack()
listbox2.pack()

btn1.pack()
# 创建一个事件循环，监测事件的发生，直到窗口关闭
top.mainloop()

