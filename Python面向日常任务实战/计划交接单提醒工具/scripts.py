# coding:utf-8

from Tkinter import *
import tkMessageBox
from os import listdir
from os.path import isfile, join
import tkFileDialog
import time


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
        time.sleep(0.01)
        # btn2.bind("KeyPress-P", stop_detecting())


def stop_detecting():
    root.quit()

root = Tk()
root.title("计划交接单监测小工具")
root.geometry("400x200+300+300")


btn1 = Button(root, text="选择目录并开始监测", command=start_detecting)
btn1.grid(row=0, column=0)
btn2 = Button(root, text="停止监测", command=stop_detecting)
btn2.grid(row=0, column=1)

mainloop()







