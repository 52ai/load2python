# coding:utf-8

from Tkinter import *

root = Tk()
root.title("Label Frame")
root.minsize(400, 300)

group = LabelFrame(root, text="我的研究生研究方向有哪些？", padx=5, pady=5)
group.pack(padx=10, pady=10)

v = IntVar()
r1 = Radiobutton(group, text="航天设备故障预测技术", variable=v, value=1).pack(anchor=W)
r2 = Radiobutton(group, text="多星任务规划", variable=v, value=2).pack(anchor=W)
r3 = Radiobutton(group, text="敏捷运控系统的研究", variable=v, value=3).pack(anchor=W)
r4 = Radiobutton(group, text="航天数据可视化研究", variable=v, value=4).pack(anchor=W)

mainloop()