# coding:utf-8

from Tkinter import *

root = Tk()
root.title("CheckButton")
root.minsize(400, 300)

var = IntVar()
print var
c = Checkbutton(root, text="我很帅！", variable=var)
print var

mainloop()