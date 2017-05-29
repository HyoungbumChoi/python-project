import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='menu')
        
        self.menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        fileNewMenu = fileMenu.Append(wx.ID_ANY, "새파일")
        fileOpenMenu = fileMenu.Append(wx.ID_ANY, "열기")
        fileMenu.AppendSeparator()
        fileExitMenu = fileMenu.Append(wx.ID_ANY, "끝내기")
        
        customMenu = wx.Menu()
        customHelloMenu = customMenu.Append(wx.ID_ANY, "&Hello")
        
        self.menuBar.Append(fileMenu, "&File")
        self.menuBar.Append(customMenu, "&Test")
        self.SetMenuBar(self.menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnNewFile, fileNewMenu)
        self.Bind(wx.EVT_MENU, self.OnOpenFile, fileOpenMenu)
        self.Bind(wx.EVT_MENU, self.OnExit, fileExitMenu)
        self.Bind(wx.EVT_MENU, self.OnHello, customHelloMenu)
    
    def OnNewFile(self, e):
        wx.MessageBox("New File menu clicked!!")
    
    def OnOpenFile(self, e):
        wx.MessageBox("Open File menu clicked!!")
    
    def OnExit(self, e):
        self.Close()
    
    def OnHello(self, e):
        wx.MessageBox("Hello~~~")

        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    
    app.MainLoop()