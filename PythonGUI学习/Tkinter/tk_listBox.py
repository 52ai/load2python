# coding:utf-8

from Tkinter import *

root = Tk()
root.title("List Box")
root.minsize(400, 300)

# 创建一个空列表

theLB = Listbox(root)
theLB.pack()

# 往列表里添加数据

for item in ["航天设备故障预测技术","多星任务规划","敏捷运控系统研究","航天数据可视化技术研究"]:
    theLB.insert(END, item)

mainloop()