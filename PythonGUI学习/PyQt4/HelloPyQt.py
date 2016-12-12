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
    w = QtGui.QWidget()
    w.resize(400, 300)
    w.move(800, 300)
    w.setWindowTitle(u'这是一个标题！')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
