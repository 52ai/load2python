# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Label")
root.minsize(400, 300)

w = Label(root, text="Hello Tkinter")
w.pack()

mainloop()