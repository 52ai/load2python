# coding:utf-8
"""
create by wayne on Dec.16 2016
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		dial = QDial()
		dial.setNotchesVisible(True)
		spinbox = QSpinBox()

		layout=QHBoxLayout()
		layout.addWidget(dial)
		layout.addWidget(spinbox)
		self.setLayout(layout)
		"""
		self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
		self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
		"""
		self.connect(dial, SIGNAL("valueChanged(int)"), spinbox, SLOT("setValue(int)"))
		self.connect(spinbox, SIGNAL("valueChanged(int)"), dial, SLOT("setValue(int)"))
		self.setWindowTitle("Signals and Slots")

class ZeroSpinBox(QSpinBox):

    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)


    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero"), self.zeros)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	#form = Form()
	form = ZeroSpinBox()
	form.show()
	app.exec_()
