# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Scale")
root.minsize(400, 300)

Scale(root, from_=0, to=42).pack()
Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()

mainloop()