# coding:utf-8

from Tkinter import *

root = Tk()
root.title("RadioButton")
root.minsize(400, 300)

v = IntVar()
v.set(2)

Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)
Radiobutton(root, text="Three", variable=v, value=3).pack(anchor=W)

mainloop()