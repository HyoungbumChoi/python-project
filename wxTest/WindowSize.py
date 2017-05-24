import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='window size')
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftButtonDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightButtonDown)
    
    def OnMouseLeftButtonDown(self, event):
        frame.SetSize(wx.Size(400,200))
        self.SetBackgroundColour(wx.Colour(0,0,255,0)) #파랑
        self.Refresh()
        
    def OnMouseRightButtonDown(self, event):
        frame.SetSize(wx.Size(200,400))
        self.SetBackgroundColour(wx.Colour(255,0,0,0)) #빨강
        self.Refresh()
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    
    app.MainLoop()