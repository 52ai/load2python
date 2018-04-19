# coding:utf-8

from Tkinter import *


def callback():
    print "我被调用啦！好开心～"


def myhelp():
    print "这是一个帮助选项哦！"


root = Tk()
# 创建一个顶级菜单

menubar = Menu(root)
menubar.add_command(label="File", command=callback)
menubar.add_command(label="Help", command=myhelp)
menubar.add_command(label="Quit", command=root.quit)

# 显示菜单

root.config(menu=menubar)

mainloop()