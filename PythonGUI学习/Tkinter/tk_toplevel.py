# coding:utf-8

from Tkinter import *


def create():
    top = Toplevel()
    top.title("新的窗口哦！")
    top.geometry("200x100+450+450")
    msg = Message(top, text="我喜欢Python!", width=200)
    msg.pack()

root = Tk()
root.title("TopLevel")
root.geometry("400x300+300+300")
Button(root, text="创建顶级窗口", command=create).pack()

mainloop()