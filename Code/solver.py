import wx

last = -1



class MyFrame(wx.Frame):  
	
	def OnToggled(self, event):
		btn = event.GetEventObject().GetLabel()
		match btn:
			case 'R': color = (255, 0, 0)
			case 'G': color = (0, 255, 0)
			case 'B': color = (0, 0, 255)
			case 'Y': color = (255, 255, 0)
			case 'O': color = (255, 127, 0)
			case 'W': color = (255, 255, 255)

		match last:
			case 0: A1.SetBackgroundColour(color)
			case 1: A2.SetBackgroundColour(color)
			case 2: A3.SetBackgroundColour(color)
			case 3: B1.SetBackgroundColour(color)
			case 4: B2.SetBackgroundColour(color)
			case 5: B3.SetBackgroundColour(color)
			case 6: C1.SetBackgroundColour(color)
			case 7: C2.SetBackgroundColour(color)
			case 8: C3.SetBackgroundColour(color)  
	
	def OnClicked(self, event): 
		btn = event.GetEventObject().GetId()
		print("Label of pressed button = ",btn)
		last = btn
		print(last)

		


	def __init__(self):
		super().__init__(parent=None, title='Hello World')
		panel = wx.Panel(self)

		global A1, A2, A3, B1, B2, B3, C1, C2, C3
		A1 = wx.Button(panel, id=0, pos=(55, 55), size=(50, 50))
		A1.SetBackgroundColour((127, 127, 127))
		
		A2 = wx.Button(panel, id=1, pos=(110, 55), size=(50, 50))
		A2.SetBackgroundColour((127, 127, 127))
		
		A3 = wx.Button(panel, id=2, pos=(165, 55), size=(50, 50))
		A3.SetBackgroundColour((127, 127, 127))
		
		B1 = wx.Button(panel, id=3, pos=(55, 110), size=(50, 50))
		B1.SetBackgroundColour((127, 127, 127))
		
		B2 = wx.Button(panel, id=4, pos=(110, 110), size=(50, 50))
		B2.SetBackgroundColour((127, 127, 127))
		
		B3 = wx.Button(panel, id=5, pos=(165, 110), size=(50, 50))
		B3.SetBackgroundColour((127, 127, 127))
		
		C1 = wx.Button(panel, id=6, pos=(55, 165), size=(50, 50))
		C1.SetBackgroundColour((127, 127, 127))
		
		C2 = wx.Button(panel, id=7, pos=(110, 165), size=(50, 50))
		C2.SetBackgroundColour((127, 127, 127))
		
		C3 = wx.Button(panel, id=8, pos=(165, 165), size=(50, 50))
		C3.SetBackgroundColour((127, 127, 127))

		Col1 = wx.Button(panel, label="R", pos=(55, 275), size=(50, 50))
		Col2 = wx.Button(panel, label="Y", pos=(110, 275), size=(50, 50))
		Col3 = wx.Button(panel, label="G", pos=(165, 275), size=(50, 50))
		Col4 = wx.Button(panel, label="B", pos=(55, 330), size=(50, 50))
		Col5 = wx.Button(panel, label="O", pos=(110, 330), size=(50, 50))
		Col6 = wx.Button(panel, label="W", pos=(165, 330), size=(50, 50))

		Col1.SetBackgroundColour((255, 0, 0))
		Col2.SetBackgroundColour((255, 255, 0))
		Col3.SetBackgroundColour((0, 255, 0))
		Col4.SetBackgroundColour((0, 0, 255))
		Col5.SetBackgroundColour((255, 127, 0))
		Col6.SetBackgroundColour((255, 255, 255))

		Col1.SetForegroundColour((255, 0, 0))
		Col2.SetForegroundColour((255, 255, 0))
		Col3.SetForegroundColour((0, 255, 0))
		Col4.SetForegroundColour((0, 0, 255))
		Col5.SetForegroundColour((255, 127, 0))
		Col6.SetForegroundColour((255, 255, 255))
		
		A1.Bind(wx.EVT_BUTTON, self.OnClicked)
		A2.Bind(wx.EVT_BUTTON, self.OnClicked)
		A3.Bind(wx.EVT_BUTTON, self.OnClicked)

		B1.Bind(wx.EVT_BUTTON, self.OnClicked)
		B2.Bind(wx.EVT_BUTTON, self.OnClicked)
		B3.Bind(wx.EVT_BUTTON, self.OnClicked)

		C1.Bind(wx.EVT_BUTTON, self.OnClicked)
		C2.Bind(wx.EVT_BUTTON, self.OnClicked)
		C3.Bind(wx.EVT_BUTTON, self.OnClicked)

		Col1.Bind(wx.EVT_BUTTON, self.OnToggled)
		Col2.Bind(wx.EVT_BUTTON, self.OnToggled)
		Col3.Bind(wx.EVT_BUTTON, self.OnToggled)
		Col4.Bind(wx.EVT_BUTTON, self.OnToggled)
		Col5.Bind(wx.EVT_BUTTON, self.OnToggled)
		Col6.Bind(wx.EVT_BUTTON, self.OnToggled)

		self.Show()


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()
