# coding=utf-8
import wx


app = wx.App()
win = wx.Frame(None, title="CCSDS TERRESTRIAL FILE TRANSFER SYSTEM", size=(820, 660))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='Open')

userButton = wx.Button(bkg, label='User')

listBtn = wx.Button(bkg, label='list')
putBtn = wx.Button(bkg, label='put')
getBtn = wx.Button(bkg, label='get')
deleteBtn = wx.Button(bkg, label='delete')
regetBtn = wx.Button(bkg, label='reget')
cdBtn = wx.Button(bkg, label='cd')
mkdirBtn = wx.Button(bkg, label='mkdir')
clearBtn = wx.Button(bkg,label='clear')


filename = wx.TextCtrl(bkg)

contents2 = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)


hbox = wx.BoxSizer()

hbox.Add(loadButton, proportion=1, flag=wx.LEFT, border=0)
hbox.Add(userButton, proportion=1, flag=wx.LEFT, border=0)


bleftbox = wx.BoxSizer(wx.VERTICAL)
bleftbox.Add(listBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(putBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(getBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(deleteBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(regetBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(cdBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(mkdirBtn,proportion=0,flag=wx.LEFT,border=5)
bleftbox.Add(clearBtn,proportion=0,flag=wx.LEFT,border=5)


bodybox = wx.BoxSizer()
bodybox.Add(bleftbox, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM |wx.RIGHT, border=5)
bodybox.Add(contents2, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM |wx.RIGHT, border=0)

fbox = wx.BoxSizer()
fbox.Add(filename, proportion=1, flag=wx.EXPAND)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(bodybox, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM |wx.RIGHT, border=5)
vbox.Add(fbox, proportion=0, flag=wx.EXPAND)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
