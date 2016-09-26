# coding:utf-8

from Tkinter import *
import tkMessageBox
from FileDialog import *

class Aplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.fdButton = Button(self, text='FileDialog', command=self.lfd)
        self.fdButton.pack()


    def hello(self):
        name = self.nameInput.get() or 'word'
        tkMessageBox.showinfo('Message', 'Hello, %s' %name)

    def lfd(self):
        fd = LoadFileDialog(self)
        filename = fd.go()
        print filename
        # tkMessageBox.showinfo('Message', 'FileName is ： %s' %filename)

app = Aplication()
# 设置窗口标题
app.master.title('Hello Tkinter')
# 主消息循环
app.mainloop()


