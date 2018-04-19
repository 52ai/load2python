# coding:utf-8
"""
create by Wayne on Dec.16 2016

"""

import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		date=self.getdata()
		# print date
		rates=sorted(self.rates.keys())
		print rates
		dateLabel = QLabel(date)
		self.fromComboBox=QComboBox()
		self.fromComboBox.addItems(rates)

		self.fromSpinBox=QDoubleSpinBox()
		self.fromSpinBox.setRange(0.01,100000.00)
		self.fromSpinBox.setValue(1.00)

		self.toComboBox = QComboBox()
		self.toComboBox.addItems(rates)
		self.toLabel=QLabel("1.00")
		#使用网格布局
		grid = QGridLayout()
		grid.addWidget(dateLabel, 0, 0)
		grid.addWidget(self.fromComboBox, 1, 0)
		grid.addWidget(self.fromSpinBox, 1, 1)
		grid.addWidget(self.toComboBox, 2, 0)
		grid.addWidget(self.toLabel, 2, 1)
		self.setLayout(grid)

		self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
		self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
		self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
		self.setWindowTitle("Currency")

	def updateUi(self):
		to = unicode(self.toComboBox.currentText())
		from_ = unicode(self.fromComboBox.currentText())
		amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
		self.toLabel.setText("%0.2f" % amount)

	def getdata(self):
		self.rates = {} #python允许在任何需要的情况下创造实例属性
		try:
			date = "Unknown"
			fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
			for line in fh:
				if not line or line.startswith(("#", "Closing ")):
					continue
				fields = line.split(",")
				if line.startswith("Date "):
					date = fields[-1] # 取最近一日的汇率
				else:
					try:
						value = float(fields[-1])
						self.rates[unicode(fields[0])] = value
					except ValueError:
						pass
			return "Exchange Rates Date:" + date
		except Exception, e:
			return "Failed to download:\n%s" %e


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	app.exec_()



