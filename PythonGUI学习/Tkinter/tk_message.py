# coding:utf-8

from Tkinter import *

root = Tk()

width = 300
height = 240
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size='%dx%d+%d+%d' % (width, height, (screenwidth-width)/2,(screenheight-height)/2)
root.geometry(size)
root.minsize(300, 240)
root.maxsize(600, 800)

w1 = Message(root, text="1.这是一则消息！", width=100)
w1.grid(row=2)

w2 = Message(root, text="2.这是一则非常长长长长长的消息！", width=200)
w2.grid(row=0)

mainloop()