import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="list combo")
        
        self.SetSize(420,250)
        self.mainPanel = wx.Panel(self)
        
        colors = ["red","orange","green","blue","yellow"]
        self.colorCombo = wx.ComboBox(self.mainPanel, choices=colors, style=wx.CB_READONLY)
        
        self.colorListBox = wx.ListBox(self.mainPanel, size=wx.Size(100,200))
        
        self.hzBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hzBoxSizer.Add(self.colorCombo, 0, wx.ALL, 5)
        self.hzBoxSizer.Add(self.colorListBox, 0, wx.ALL, 5)
        self.mainPanel.SetSizer(self.hzBoxSizer)
        
        self.Bind(wx.EVT_COMBOBOX, self.OnComboBox, self.colorCombo)
        self.Bind(wx.EVT_LISTBOX, self.OnComboList, self.colorListBox)
        
    def OnComboBox(self, e):
        idx = self.colorCombo.GetCurrentSelection()
        self.colorListBox.Append(self.colorCombo.Items[idx])
    
    def OnComboList(self, e):
        idx = self.colorListBox.GetSelection()
        wx.MessageBox(self.colorListBox.Items[idx])
    
        
        
           
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    
    app.MainLoop()