import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="radio button")
        
        self.SetSize(380,100)
        self.mainPanel = wx.Panel(self)
        self.mainBox = wx.StaticBox(self.mainPanel, label = "color")
        
        self.radioRed = wx.RadioButton(self.mainBox, label="red", style=wx.RB_GROUP)
        self.radioGreen = wx.RadioButton(self.mainBox, label="green")
        self.radioBlue = wx.RadioButton(self.mainBox, label="blue")
        
        self.radioEnable = wx.RadioButton(self.mainBox, label="enable", style=wx.RB_GROUP)
        self.radioDisable = wx.RadioButton(self.mainBox, label="disable")
        
        self.gridSizer = wx.GridSizer(rows=2, cols=3, hgap=5, vgap=15)
        self.gridSizer.Add(self.radioRed)
        self.gridSizer.Add(self.radioGreen)
        self.gridSizer.Add(self.radioBlue)
        self.gridSizer.Add(self.radioEnable)
        self.gridSizer.Add(self.radioDisable)
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND | wx.ALL, 15)
        self.mainBox.SetSizer(self.vtBoxSizer)
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer.Add(self.mainBox, 1, wx.EXPAND | wx.ALL, 5)
        self.mainPanel.SetSizer(self.mainSizer)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRed, self.radioRed)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnGreen, self.radioGreen)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnBlue, self.radioBlue)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnEnable, self.radioEnable)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDisable, self.radioDisable)
        
    def OnRed(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(255,0,0))
        self.mainBox.Refresh()
    
    def OnGreen(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(0,255,0))
        self.mainBox.Refresh()
    
    def OnBlue(self, e):
        self.mainBox.SetBackgroundColour(wx.Colour(0,0,255))
        self.mainBox.Refresh()
    
    def OnEnable(self, e):
        self.radioRed.Enable(True)
        self.radioGreen.Enable(True)
        self.radioBlue.Enable(True)
    
    def OnDisable(self, e):
        self.radioRed.Enable(False)
        self.radioGreen.Enable(False)
        self.radioBlue.Enable(False)
    
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    
    app.MainLoop()