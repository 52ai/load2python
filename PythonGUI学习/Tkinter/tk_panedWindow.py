# coding:utf-8

from Tkinter import *


root = Tk()

root.minsize(300, 240)

m = PanedWindow(root, orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)


mainloop()