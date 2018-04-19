# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Spinbox")
root.minsize(400, 300)

w = Spinbox(root, from_=0, to=10)
w.pack()

mainloop()