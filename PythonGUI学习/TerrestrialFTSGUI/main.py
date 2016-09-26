# coding=utf-8
# Author：Wenyan Yu
# Date：2016.3.18
# Name:main.py
import wx


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Main Page(TERRESTRIAL FILE TRANSFER SYSTEM)', size=(670, 364))
        self.SetBackgroundColour(wx.Colour(204, 153, 102))
        font_title = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL)
        font_text = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, "CCSDS TERRESTRIAL FILE TRANSFER SYSTEM",
                      pos=(10, 10), size=(150, 25)).SetFont(font_text)
        openBtn = wx.Button(self, label='OPEN', pos=(10, 50), size=(80, 25))
        userBtn = wx.Button(self, label='USER', pos=(150, 50), size=(80, 25))
        #Body Button
        listBtn = wx.Button(self, label='list', pos=(10, 100), size=(80, 25))
        putBtn = wx.Button(self, label='put', pos=(150, 100), size=(80, 25))
        getBtn = wx.Button(self, label='get', pos=(10, 140), size=(80, 25))
        deleteBtn = wx.Button(self, label='delete', pos=(150, 140), size=(80, 25))
        regetBtn = wx.Button(self, label='reget', pos=(10, 180), size=(80, 25))
        cdBtn = wx.Button(self, label='cd', pos=(150, 180), size=(80, 25))
        mkdirBtn = wx.Button(self, label='mkdir', pos=(10, 220), size=(80, 25))
        clearBtn = wx.Button(self, label='clear', pos=(150, 220), size=(80, 25))
        #The Right Task List
        tasklist = wx.TextCtrl(self, pos=(300, 50), size=(300, 195))
        wx.StaticText(self, -1, "Local address:XXX.XXX.XXX.XXX    Peer IP address:XXX.XXX.XXX.XXX  Connetion Status:ON", pos=(10, 300), size=(150, 25)).SetFont(font_text)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()