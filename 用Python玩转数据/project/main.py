# coding:utf-8

"""
Main.py
author: Wayne
date:2016-11-30

"""

import wx
import urllib2
import re
from custom_dialogs import ConfigureData

class StockFrame(wx.Frame):
	'define main Frame of Stock Tools'
	def __init__(self,superior):
		wx.Frame.__init__(self,parent=superior,title='Dow Jones Industrial Stock Tools',pos=(400,400),size=(500,600))

		# 创建自动调用尺寸的容器panel
		panel = wx.Panel(self)
		# 创建Sizer
		codeSizer = wx.BoxSizer(wx.HORIZONTAL)
		# 创建子窗口（窗体部件）
		labelText = wx.StaticText(panel, label = "股票代码:")
		# 使用sizer的Add()方法将每个子窗口添加给sizer
		codeSizer.Add(labelText, 0, wx.ALIGN_BOTTOM)
		codeSizer.Add((10, 10))
		# 添加文本输入框
		self.addressText = wx.TextCtrl(panel, value='APPL')
		self.addressText.SetSize(self.addressText.GetEffectiveMinSize())
		codeSizer.Add(self.addressText)

		self.list = wx.ListCtrl(panel, wx.NewId(), style= wx.LC_REPORT)
		self.list.InsertColumn(0, "Symbol")
		self.list.InsertColumn(1, "Name")
		self.list.InsertColumn(2, "Last Trade")

		pos = self.list.InsertStringItem(0, "--")
		self.list.SetStringItem(pos, 1, "loading...")
		self.list.SetStringItem(pos, 2, "--")
		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.list)

		vsizer = wx.BoxSizer(wx.VERTICAL)
		vsizer.Add(codeSizer, 0, wx.ALL, 10)
		vsizer.Add(self.list, -1, wx.ALL | wx.EXPAND, 10)

		hsizer = wx.BoxSizer(wx.HORIZONTAL)
		hsizer.Add((10, 10))
		button_quit = wx.Button(panel, -1, "退出")
		self.Bind(wx.EVT_BUTTON, self.OnQuit, button_quit)
		button_quit.SetDefault()
		hsizer.Add(button_quit, 1)

		button_refresh = wx.Button(panel, -1, "获取数据")
		self.Bind(wx.EVT_BUTTON, self.OnRefresh, button_refresh)
		hsizer.Add(button_refresh,1)

		vsizer.Add(hsizer, 0, wx.ALIGN_BOTTOM)

		# 调用容器的SetSizer(sizer)方法
		panel.SetSizerAndFit(vsizer)
		panel.Layout()

		# help(addressText)

	def GetAllSelected(self):
		selection = []
		current = -1
		while True:
			next = self.GetNextSelected(current)
			if next == -1:
				return selection
			selection.append(self.list.GetItemText(next))
			current = next 


	def GetNextSelected(self, current):
		return self.list.GetNextItem(current,
					wx.LIST_NEXT_ALL,
					wx.LIST_STATE_SELECTED)

	def OnClick(self, event):
		codes = self.GetAllSelected()
		print "code in DJI",codes 
		ConfigureData(codes)

	def OnQuit(self, event):
		self.Close()
		self.Destroy()
	def OnRefresh(self, event):
		# 获取数据
		dStr = urllib2.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
		m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)
		if m:
			print m
			print len(m)
			self.SetData(m)
		else:
			wx.MessageBox('数据获取失败，请检查网络链接情况！', 'Message', wx.OK | wx.ICON_INFORMATION)

	def SetData(self, data):
		self.list.ClearAll()
		self.list.InsertColumn(0, "Symbol")
		self.list.InsertColumn(1, "Name")
		self.list.InsertColumn(2, "Last Trade")
		pos = 0
		for row in data:
			pos = self.list.InsertStringItem(pos+1, row[0])
			self.list.SetStringItem(pos, 1, row[1].replace("&amp;","&"))
			self.list.SetColumnWidth(1, -1)
			self.list.SetStringItem(pos, 2, row[2])
			if (pos % 2 == 0):
				self.list.SetItemBackgroundColour(pos, (134, 255, 249))
		self.FitInside()

class StockApp(wx.App):
	'define StockApp Class'
	def OnInit(self):
		frame = StockFrame(None)
		frame.Show()		
		return True

if __name__ =='__main__':
	app = StockApp()
	app.MainLoop()

