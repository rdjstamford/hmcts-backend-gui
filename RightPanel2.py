import wx

class RightPanel2(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent=parent)

        self.frame = frame

        self.SetBackgroundColour("Red")
        