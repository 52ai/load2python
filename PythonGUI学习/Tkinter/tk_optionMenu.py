# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Option Menu")
root.geometry("400x300+400+400")

variable = StringVar()
variable.set("one")

w = OptionMenu(root, variable, "one", "two", "three")
w.pack()

mainloop()