import wx

class TextFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Login Page(TERRESTRIAL FILE TRANSFER SYSTEM)',
                size=(670, 364))
        self.SetBackgroundColour(wx.Colour(204, 153, 102))
        font = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL)
        wx.StaticText(self, -1, "UserName", pos=(60, 100), size=(150, 25)).SetFont(font)
        user_id = wx.TextCtrl(self, pos=(260, 100), size=(210, 25))
        wx.StaticText(self, -1, "Password", pos=(60, 150), size=(150, 25)).SetFont(font)
        pwd = wx.TextCtrl(self, pos=(260, 150), size=(210, 25), style=wx.TE_PASSWORD)
        loginBtn = wx.Button(self, label='Login', pos=(260, 220), size=(80, 25))
        resetBtn = wx.Button(self, label='Reset', pos=(390, 220), size=(80, 25))


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()