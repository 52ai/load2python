# coding:utf-8

from Tkinter import *
import tkMessageBox
import tkFileDialog
import tkColorChooser


def file_dialog_callback():
    file_name = tkFileDialog.askopenfilename()
    print file_name


def message_dialog_callback():
    return_mesg=tkMessageBox.askquestion("请确认动作！", "是否发射核弹？")
    print return_mesg
    if return_mesg == 'yes':
        return_mesg = tkMessageBox.showwarning("请确认动作！", "警告：你正准备发射核弹！")
        print return_mesg
        return_mesg = tkMessageBox.showinfo("消息提示！", "核弹准备就绪，正准备发射！")
        print return_mesg
        return_mesg = tkMessageBox.showerror("ERROR!", "核弹发射出错，即将自爆！")
        print return_mesg


root = Tk()
root.title("Dialogs")
root.minsize(400, 300)

Button(root, text="选择文件", command=file_dialog_callback).pack()
Button(root, text="消息对话", command=message_dialog_callback).pack()


mainloop()