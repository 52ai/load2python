# coding:utf-8

from Tkinter import *


def callback(event):
    print"鼠标点击的位置:", event.x, event.y

root = Tk()
root.title("Events and Bindings")
root.geometry("400x300+400+400")

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)

"""
<Button-1>：鼠标左击事件
<Button-2>：鼠标中击事件
<Button-3>：鼠标右击事件
<Double-Button-1>：双击事件
<Triple-Button-1>：三击事件
"""
frame.pack()

mainloop()