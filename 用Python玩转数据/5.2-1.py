# coding:utf-8

"""
GUI Basic Framework of GUI
"""
from wx import *

"""
app = wx.App()
frame = wx.Frame(None, title="Hello, World!")
frame.Show(True)
app.MainLoop()
"""
# 采用面向对象的方法设计GUI

class MyFrame(wx.Frame):
	'define Class MyFrame '
	def __init__(self,superior):
		wx.Frame.__init__(self, parent=superior, title="Example", pos=(100,200),size=(200,100))
		# panel = wx.Panel(self)
		# text1 = wx.TextCtrl(panel, value="Hello, World!", size=(200,100))
		self.Bind(wx.EVT_LEFT_UP,self.OnClick) # 鼠标左键的抬起事件绑在Frame的OnClick()事件上

	def OnClick(self,event):
		posm = event.GetPosition()
		wx.StaticText(parent = self, label="Hello, world", pos=(posm.x, posm.y))


class MyApp(wx.App):
	def OnInit(self): # 在初始化的时候，wxPython 会首先调用这个函数，并返回一个bool值
		frame = MyFrame(None)
		frame.Show()
		return True

if __name__ == '__main__':
	app = MyApp() # 实例化MyApp()类
	app.MainLoop()



"""
组件

组件容器（Containers）---用于容纳其他组件
例如:wx.Panel

动态组件（Dynamic Widgets）---可以被用户编辑
例如:wx.Button,wx.TextCtrl,wx.ListBox

静态组件（Static Widgets）----显示信息用，不能被用户编辑
例如：wx.StaticBitmap,wx.StaticText,wx.StaticLine等

其他组件
例如:wx.ToolBar, wxMenuBar,wxStatusBar

"""
"""
事件处理机制（Event Handing）

GUI程序工作的基本机制之一----事件处理

事件：移动鼠标，鼠标点击，可以由用户操作触发产生，也可以在程序中创建对象产生
wxPython程序将特定类型的事件关联到特定的一块代码（方法），当该类型的事件产生时，相关代码将响应事件被自动执行
例如：当产生鼠标移动事件时，OnMove()方法将被自动调用

"""