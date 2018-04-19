# coding:utf-8
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	"""
	create From class
	"""
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		self.browser=QTextBrowser()
		self.lineedit = QLineEdit("Type an expression and press Enter")
		self.lineedit.selectAll()
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.setLayout(layout)
		self.lineedit.setFocus()
		self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
		self.setWindowTitle("Calculate")
	def updateUi(self):
		try:
			text = unicode(self.lineedit.text())
			self.browser.append("%s = <b>%s<b>" %(text, eval(text)))
			self.lineedit.setText("")
		except:
			self.browser.append("<font color=red> %s is invalid!</font>" % text)
			self.lineedit.setText("")
app = QApplication(sys.argv)
form=Form()
form.show()
app.exec_()

