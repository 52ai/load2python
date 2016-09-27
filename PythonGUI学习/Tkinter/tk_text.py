# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Scale")
root.minsize(400, 300)

text = Text(root, width = 40, height=10)
text.pack()

# 设置tag
text.tag_config("tag_1", background="yellow", foreground="red")

# INSERT 索引表示插入光标当前位置

text.insert(INSERT, "我喜欢")
text.insert(END, "Python!", "tag_1")

mainloop()
