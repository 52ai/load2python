# coding:utf-8
"""
author: wayne
website: mryu.top
last edited: Dec.09 2016

Hello PyQt
"""

from os import sys
from PyQt4 import QtGui

def main():    
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget() # QWidget是所有UI对象的基类
    w.resize(400, 300) # 定义控件的长和宽
    w.move(800, 300) # 初始化窗口控件的位置
    w.setWindowTitle(u'这是一个标题！') # 设置标题栏文字
    w.show() # 将控件显示在屏幕上
    
    sys.exit(app.exec_()) # 调用app.exec_()会开始执行QApplication对象的事件循环


if __name__ == '__main__':
    main()
