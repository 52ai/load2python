# coding:utf-8

from Tkinter import *


def callback():
    print "我被调用啦！"


root = Tk()
root.title("Menu Button")
root.geometry("400x300+400+400")

mb = Menubutton(root, text="点我", relief=RAISED)
mb.pack()

filemenu = Menu(mb, tearoff=False)
filemenu.add_checkbutton(label="打开", command=callback, selectcolor="yellow")
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
mb.config(menu= filemenu)

mainloop()