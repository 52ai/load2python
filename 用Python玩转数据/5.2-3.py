# coding:utf-8

"""
布局管理

绝对定位-每个窗口部件被创建时可以显式地制定它的位置和大小
缺点：定位不灵活，调整大小困难，受设备、操作系统甚至字体的影响


灵活布局的解决方案-sizer

sizer本身不是一个容器或一个窗口部件。它只是一个屏幕布局的算法
sizer允许嵌套

wxPython常用的sizer

wx.BoxSizer (垂直或水平)
wx.FlexGridSizer（行高和列宽由最大的组件决定）
wx.GridSizer（所有组件大小一致）
wx.GridBagSizer
wx.StaticBoxSizer

使用sizer的步骤

1.创建自动调用尺寸的容器，例如panel
2.创建sizer
3.创建子窗口（窗体部件）
4.使用sizer的Add()方法将每个子窗口添加给sizer
5.调用容器的SetSizer(sizer)方法

"""

from wx import *

# 采用面向对象的方法设计GUI

class MyFrame(wx.Frame):
	'define Class MyFrame '
	def __init__(self,superior):
		wx.Frame.__init__(self, parent=superior, title="Hello,World in wxPython!", pos=(600,400),size=(600,400))
		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.text1 = wx.TextCtrl(panel, value="Hello, world!", size=(200,180), style=wx.TE_MULTILINE)
		sizer.Add(self.text1,0,wx.ALIGN_TOP | wx.EXPAND)
		button = wx.Button(panel, label="Click Me")
		sizer.Add(button)
		panel.SetSizerAndFit(sizer)
		panel.Layout()
		self.Bind(wx.EVT_BUTTON, self.OnClick, button)

	def OnClick(self,text):
		self.text1.AppendText("\nHello, World!")


class MyApp(wx.App):
	def OnInit(self): # 在初始化的时候，wxPython 会首先调用这个函数，并返回一个bool值
		frame = MyFrame(None)
		frame.Show()
		return True
'''
if __name__ == '__main__':
	app = MyApp() # 实例化MyApp()类
	app.MainLoop()
'''
help(wx.Button)