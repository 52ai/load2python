# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Entry")
root.minsize(400, 300)


e=Entry(root)
e.pack(padx=20,pady=20)

e.delete(0, END)
e.insert(0, "默认文本....")

mainloop()