# coding:utf-8

"""
GUI常用组件

静态文本，列表框，输入框，按钮


按钮：wx.Button wx.BitmapButton wx.ToggleButton

菜单：wx.MenuBar(菜单栏) wx.Menu（菜单） wx.MenuItem（菜单项命令）

静态文本框 wx.StaticText 文本框 wx.TextCtrl

列表（ListCtrl）wx.LC_ICON wx.LC_SMALL_ICON wx.LC_LIST wx.LC_REPORT

单选(RadioBox)与复选框(CheckBox)


"""

from wx import *

# 采用面向对象的方法设计GUI

class MyFrame(wx.Frame):
	'define Class MyFrame '
	def __init__(self,superior):
		wx.Frame.__init__(self, parent=superior, title="Hello,World in wxPython!", pos=(100,200),size=(200,100))
		panel = wx.Panel(self)
		self.text1 = wx.TextCtrl(panel, value="Hello, world!", size=(200,180), style=wx.TE_MULTILINE)
		button = wx.Button(panel, label="Click Me")
		self.Bind(wx.EVT_BUTTON, self.OnClick, button)

	def OnClick(self,text):
		self.text1.AppendText("\nHello, World!")


class MyApp(wx.App):
	def OnInit(self): # 在初始化的时候，wxPython 会首先调用这个函数，并返回一个bool值
		frame = MyFrame(None)
		frame.Show()
		return True

if __name__ == '__main__':
	app = MyApp() # 实例化MyApp()类
	app.MainLoop()
