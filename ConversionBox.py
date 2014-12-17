#! /usr/bin/env python
import wx

isRound = False # current: need rounding

def fl(string): # "float"
	if(str(string) == ''): return 0 # default: 0. Use str() to transfer Unicode to string. I don't know if Linux or Mac uses u'...' also.
	if(float(string) < 0): raise ValueError("Can't be negative.")
	return float(string)
	
class wxFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title = "Converter")
		
		self.panel = wx.Panel(self)
		self.cbRound = wx.CheckBox(self.panel, label='Round to 2 decimal places', pos=(20, 150)) # checkbox
		self.cbRound.Bind(wx.EVT_CHECKBOX, self.OnRound)
		self.Center()
		self.prompt = wx.StaticText(self.panel, label="This program can convert between inches and meters.")
		self.mLabel = wx.StaticText(self.panel, label="m", pos=(115,50))# labels
		self.cmLabel = wx.StaticText(self.panel, label="cm", pos=(265,50))
		self.ftLabel = wx.StaticText(self.panel, label="ft", pos=(115,100))
		self.inLabel = wx.StaticText(self.panel, label="inch", pos=(265,100))
		
		self.mBox = wx.TextCtrl(self.panel, value="0", pos=(0,50))
		self.cmBox = wx.TextCtrl(self.panel, value="0.0", pos=(150,50))
		self.ftBox = wx.TextCtrl(self.panel, value="0", pos=(0,100))
		self.inBox = wx.TextCtrl(self.panel, value="0.0", pos=(150,100))
		
		self.mBox.Bind(wx.EVT_TEXT, self.OnConvert) # Bind to the same event
		self.cmBox.Bind(wx.EVT_TEXT, self.OnConvert)
		self.ftBox.Bind(wx.EVT_TEXT, self.OnConvert)
		self.inBox.Bind(wx.EVT_TEXT, self.OnConvert)

	def OnRound(self, e):
		global isRound # let it round
		isRound = self.cbRound.GetValue()
		self.OnConvert(e) # GetEventObject will return a checkbox. When the program detects this, it will round the answer automatically.
	
	def OnConvert(self, e): # invisible "convert" button. Triggered by text changing.
		currentBox = e.GetEventObject()
		if(currentBox == self.mBox or currentBox == self.cmBox): # SI -> Eng
			cm = self.cmBox.GetValue()
			m = self.mBox.GetValue()
			cm = fl(cm) + 100.0 * fl(m)
			inch = cm / 2.54 # convert
			ft = int(inch // 12) # "aliquot" int
			inch -= 12 * ft
			if(isRound): inch = round(inch, 2) # round if needed
			self.ftBox.ChangeValue(str(ft)) # SetValue without generating EVT_TEXT
			self.inBox.ChangeValue(str(inch))
		elif(currentBox == self.ftBox or currentBox == self.inBox): # Eng -> SI
			inch = self.inBox.GetValue()
			ft = self.ftBox.GetValue()
			inch = fl(inch) + 12.0 * fl(ft)
			cm = inch * 2.54
			m = int(cm // 100)
			cm -= 100 * m
			if(isRound): cm = round(cm, 2)
			self.mBox.ChangeValue(str(m))
			self.cmBox.ChangeValue(str(cm))
		else: # checkbox clicked
			inch = fl(self.inBox.GetValue()); cm = fl(self.cmBox.GetValue())
			if(isRound): inch = round(inch, 2); cm = round(cm, 2)
			self.inBox.ChangeValue(str(inch)); self.cmBox.ChangeValue(str(cm))

# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = wxFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()