import wx

class MyFrame(wx.Frame):    
	def __init__(self):
		super().__init__(parent=None, title='Hello World')
		panel = wx.Panel(self)

		
		A1 = wx.Button(panel, pos=(55, 55), size=(50, 50))
		A1.SetBackgroundColour((127, 127, 127))
		
		A2 = wx.Button(panel, pos=(110, 55), size=(50, 50))
		A2.SetBackgroundColour((127, 127, 127))
		
		A3 = wx.Button(panel, pos=(165, 55), size=(50, 50))
		A3.SetBackgroundColour((127, 127, 127))
		
		B1 = wx.Button(panel, pos=(55, 110), size=(50, 50))
		B1.SetBackgroundColour((127, 127, 127))
		
		B2 = wx.Button(panel, pos=(110, 110), size=(50, 50))
		B2.SetBackgroundColour((127, 127, 127))
		
		B3 = wx.Button(panel, pos=(165, 110), size=(50, 50))
		B3.SetBackgroundColour((127, 127, 127))
		
		C1 = wx.Button(panel, pos=(55, 165), size=(50, 50))
		C1.SetBackgroundColour((127, 127, 127))
		
		C2 = wx.Button(panel, pos=(110, 165), size=(50, 50))
		C2.SetBackgroundColour((127, 127, 127))
		
		C3 = wx.Button(panel, pos=(165, 165), size=(50, 50))
		C3.SetBackgroundColour((127, 127, 127))

		# Col0 = wx.Panel(panel, pos=(50, 270), size=(170, 115))
		Col1 = wx.Button(panel, pos=(55, 275), size=(50, 50))
		Col2 = wx.Button(panel, pos=(110, 275), size=(50, 50))
		Col3 = wx.Button(panel, pos=(165, 275), size=(50, 50))
		Col4 = wx.Button(panel, pos=(55, 330), size=(50, 50))
		Col5 = wx.Button(panel, pos=(110, 330), size=(50, 50))
		Col6 = wx.Button(panel, pos=(165, 330), size=(50, 50))

		# Col0.SetBackgroundColour((0, 0, 0))
		Col1.SetBackgroundColour((255, 0, 0, 255))
		Col1.SetForegroundColour((255, 0, 0, 255))
		Col2.SetBackgroundColour((255, 255, 0))
		Col3.SetBackgroundColour((0, 255, 0))
		Col4.SetBackgroundColour((0, 0, 255))
		Col5.SetBackgroundColour((255, 127, 0))
		Col6.SetBackgroundColour(wx.Colour(255,0,0))
		

		self.Show()

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()