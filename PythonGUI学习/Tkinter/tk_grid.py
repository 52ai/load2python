# coding:utf-8
from Tkinter import *


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2,(screenheight-height)/2)
    print size
    root.geometry(size)

root = Tk()

root.title('Tkinter Grid 布局')
center_window(root, 300, 240)
root.maxsize(600, 400)
root.minsize(300, 240)

# column 默认值是0

Label(root, text="用户名").grid(row=0)
Label(root, text="密码").grid(row=1)

Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

Label(root, text = '屏幕大小(%sx%s)\n窗口大小(%sx%s)' % (get_screen_size(root) + get_window_size(root))).grid(row=3)
mainloop()