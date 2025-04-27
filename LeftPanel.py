import wx
import requests
import json
import urllib.request

class LeftPanel(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent=parent)

        self.btnAllCases = wx.Button(self, label = "All Cases", size=(100,100))
        self.btnAdd = wx.Button(self, label = "Add Case", size=(100,100))
        self.btnDelete = wx.Button(self, label = "Delete Case", size = (100,100))
        self.btnUpdate = wx.Button(self, label = "Update Case", size = (100,100))

        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(10)
        box.Add(self.btnAllCases,2,wx.ALIGN_CENTER)
        box.AddSpacer(10)
        box.Add(self.btnAdd,2,wx.ALIGN_CENTER)
        box.AddSpacer(10)
        box.Add(self.btnDelete,2,wx.ALIGN_CENTER)
        box.AddSpacer(10)
        box.Add(self.btnUpdate,2,wx.ALIGN_CENTER)
        self.SetSizer(box)



        self.frame = frame

        self.btnAllCases.Bind(wx.EVT_BUTTON, lambda event: self.allCases())
        self.btnAdd.Bind(wx.EVT_BUTTON, lambda event: self.addBtn())
        self.btnDelete.Bind(wx.EVT_BUTTON, lambda event: self.deleteBtn())
        self.btnUpdate.Bind(wx.EVT_BUTTON, lambda event: self.updateBtn())

    def allCases(self):
        self.frame.switch(1)
        source = urllib.request.urlopen("http://localhost:4000/allCases").read()
        output = json.loads(source)
        self.frame.outputToRightPanel(output)
    
    def addBtn(self):
        self.frame.switch(2)
    
    def deleteBtn(self):
        self.frame.switch(3)
    
    def updateBtn(self):
        self.frame.switch(4)
        