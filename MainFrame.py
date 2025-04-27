import wx
from LeftPanel import LeftPanel
from RightPanel import RightPanel
from RightPanel2 import RightPanel2

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "hmcts", size=(1200,500))

        #self.Maximize(True)

        self.splitter = wx.SplitterWindow(self)

        self.leftPanel = LeftPanel(self.splitter, self)
        self.RightPanel = RightPanel(self.splitter, self.leftPanel)

        self.splitter.SplitVertically(self.leftPanel, self.RightPanel)
        self.splitter.SetMinimumPaneSize(250)

        
    
    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)
    
    def outputToRightPanel(self, text):
        self.RightPanel.changeTextField(text)
    
    def switch(self, btn):
        #int btn
        self.RightPanel.switchFields(btn)
            



