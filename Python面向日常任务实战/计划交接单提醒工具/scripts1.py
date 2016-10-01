# coding:utf-8

from Tkinter import *
import tkMessageBox
from os import listdir
from os.path import isfile, join
import tkFileDialog

"""
def start_detecting():
    file_dir = tkFileDialog.askdirectory()
    print file_dir
    files_list = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
    print files_list
    print len(files_list)
    while 1:
        temp_files_list = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
        if len(files_list) < len(temp_files_list):
            print "有新的交接单来了！"
            return_msg = tkMessageBox.showinfo("消息提示", "有新的交接单来了！")
            break

def stop_detecting():
    root.quit()
"""


def file_list():
    file_dir = tkFileDialog.askdirectory()
    print file_dir
    file_list = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
    for item in file_list:
        lb.insert(END,item)

root = Tk()
root.title("计划交接单监测小工具")
root.geometry("400x200+300+300")

Button(root, text="文件列表", command=file_list).pack()
lb = Listbox(root)
lb.pack()

mainloop()







