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

"""