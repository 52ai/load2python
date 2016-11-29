# coding:utf-8

"""
GUI Basic Framework of GUI
"""

import wx
app = wx.App()
frame = wx.Frame(None, title="Hello, World!")
frame.Show(True)
app.MainLoop()