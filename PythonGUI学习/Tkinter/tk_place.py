# coding:utf-8

from Tkinter import *


def callback():
    print "正中靶心！"


root = Tk()
Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()

