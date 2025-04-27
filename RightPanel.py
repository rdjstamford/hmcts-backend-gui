import wx
import urllib
import json

class RightPanel(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent=parent)

        self.frame = frame

        self.text = wx.TextCtrl(self, size = (800,400), style=wx.TE_MULTILINE)
        self.text.Hide()
        self.label1 = wx.StaticText(self,label="Case Number:")
        self.text1 = wx.TextCtrl(self, size=(100,50))
        self.label2 = wx.StaticText(self,label="Title:")
        self.text2 = wx.TextCtrl(self, size=(100,50))
        self.label3 = wx.StaticText(self,label="Description:")
        self.text3 = wx.TextCtrl(self, size=(100,50))
        self.label4 = wx.StaticText(self,label="Staus:")
        self.text4 = wx.TextCtrl(self, size=(100,50))
        self.label5 = wx.StaticText(self,label="Due Date (DD-MM-YYYY) :")
        self.text5 = wx.TextCtrl(self, size=(100,50))
        self.btnSubmit = wx.Button(self, label="Submit",size=(100,50))
        self.updateField = wx.TextCtrl(self, size=(100,50), pos = (0,30))
        self.btnUpdate = wx.Button(self, label = "Submit",size=(100,50) , pos=(0,100))

        self.btnDelete = wx.Button(self,label="Delete",size=(100,50), pos=(0,30))

        self.console = wx.StaticText(self, size=(200,200), pos=(200,0))
        #TODO: add error handing and output errors to self.console

        self.dropdown = wx.ComboBox(self, size=(100,100))
        self.dropdown.Hide()
        self.btnDelete.Hide()
        self.btnUpdate.Hide()        

        box = wx.BoxSizer(wx.VERTICAL)
        box.AddSpacer(10)
        box.AddSpacer(10)  
        box.Add(self.label1)
        box.Add(self.text1)
        box.AddSpacer(10) 
        box.Add(self.label2)
        box.Add(self.text2)
        box.AddSpacer(10)
        box.Add(self.label3) 
        box.Add(self.text3)
        box.AddSpacer(10) 
        box.Add(self.label4)
        box.Add(self.text4)
        box.AddSpacer(10)
        box.Add(self.label5) 
        box.Add(self.text5)
        box.AddSpacer(10)
        box.Add(self.btnSubmit)
        self.SetSizer(box)            

        self.btnSubmit.Bind(wx.EVT_BUTTON, lambda event: self.submitCase())
        self.btnDelete.Bind(wx.EVT_BUTTON, lambda event: self.delete())
        self.btnUpdate.Bind(wx.EVT_BUTTON, lambda event: self.update())
    
    
    def switchFields(self,btn):
        #int btn
        if btn == 1:
            self.text.Show()
            self.text.Clear()
            self.hideTxtFields()
            self.btnSubmit.Hide()
            self.dropdown.Hide()
            self.btnDelete.Hide()
            self.btnUpdate.Hide()
            self.console.Hide()
            self.updateField.Hide()
        elif btn == 2:
            self.text.Hide()
            self.dropdown.Hide()
            self.btnDelete.Hide()
            self.btnUpdate.Hide()
            self.text1.Show()
            self.text2.Show()
            self.text3.Show()
            self.text4.Show()
            self.text5.Show()
            self.label1.Show()
            self.label2.Show()
            self.label3.Show()
            self.label4.Show()
            self.label5.Show()
            self.btnSubmit.Show()
            self.console.Show()
            self.console.SetLabelText("")
            self.updateField.Hide()
        elif btn == 3:
            self.text.Hide()
            self.hideTxtFields()
            self.btnSubmit.Hide()
            self.dropdown.Show()
            #self.dropdown.Hide()
            self.btnDelete.Show()
            self.btnUpdate.Hide()
            self.populateDropdown()
            self.updateField.Hide()
            self.console.Show()
            self.console.SetLabelText("")
        elif btn == 4:
            self.text.Hide()
            self.hideTxtFields()
            self.btnSubmit.Hide()
            self.dropdown.Show()
            self.btnDelete.Hide()
            self.btnUpdate.Show()
            self.populateDropdown()
            self.updateField.Show()
            self.console.Show()
            self.console.SetLabelText("")

    def hideTxtFields(self):
        self.text1.Hide()
        self.text2.Hide()
        self.text3.Hide()
        self.text4.Hide()
        self.text5.Hide()
        self.label1.Hide()
        self.label2.Hide()
        self.label3.Hide()
        self.label4.Hide()
        self.label5.Hide()

    def resetFields(self):
        self.text1.Clear()
        self.text2.Clear()
        self.text3.Clear()
        self.text4.Clear()
        self.text5.Clear()

    
    def changeTextField(self, json):
        for i in range(len(json)):
            self.text.WriteText("Id: "+str(json[i]['id'])+" ")
            self.text.WriteText("Case Number: "+json[i]['caseNumber']+" ")
            self.text.WriteText("Title: "+json[i]['title']+" ")
            self.text.WriteText("Description: "+json[i]['description']+" ")
            self.text.WriteText("Status: "+json[i]['status']+" ")
            self.text.WriteText("Due Date: "+json[i]['dueDate']+" ")
            self.text.WriteText("Created Date: "+json[i]['createdDate']+" ")
            self.text.WriteText("\n")
    
    def submitCase(self):
        url = "http://localhost:4000/createCase/"+self.text1.GetValue()+"/"+self.text2.GetValue()+"/"+self.text3.GetValue()+"/"+self.text4.GetValue()+"/"+self.text5.GetValue()
        source = urllib.request.urlopen(url).read()
        self.console.SetLabelText("Case added.")
        self.resetFields()
        #print(source)
    
    def populateDropdown(self):
        self.dropdown.Clear()
        source = urllib.request.urlopen("http://localhost:4000/allCases").read()
        output = json.loads(source)
        for i in range(len(output)):
            self.dropdown.Append(str(output[i]['id']))
    
    def delete(self):
        url = "http://localhost:4000/deleteCase/"+str(self.dropdown.GetCurrentSelection()+1)
        source = urllib.request.urlopen(url).read()
        self.populateDropdown()
        self.console.SetLabelText("Deleted Case")
        self.Refresh()
        self.Update()
    
    def update(self):
        url = "http://localhost:4000/updateCase/"+str(self.dropdown.GetCurrentSelection()+1)+"/"+self.updateField.GetValue()
        source = urllib.request.urlopen(url).read()
        self.console.SetLabelText("Updated Status")
        self.updateField.Clear()
        self.Refresh()
        self.Update()

