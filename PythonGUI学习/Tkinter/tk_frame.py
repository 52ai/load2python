# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Frame")
root.minsize(400, 300)

Label(root, text="天王盖地虎").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(root, text="小鸡炖蘑菇").pack()
mainloop()