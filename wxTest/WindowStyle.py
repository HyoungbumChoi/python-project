import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='window style')
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftButtonDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightButtonDown)
    
    def OnMouseLeftButtonDown(self, event):
        self.SetWindowStyle(wx.RESIZE_BORDER | wx.CAPTION)
        
    def OnMouseRightButtonDown(self, event):
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    
    app.MainLoop()