from PIL import Image 				# Importing the Image module from the PIL library to 
import sys							# Importing the sys module to stop the code if an error occurs.
from datetime import datetime		# Importing the datetime module to get the date and time of the launch of the code.
import wx	# Importing the wxPython library to create a GUI.



def finder(cube):

	# Selecting input image.
	im = Image.open("./final.png")

	print("Image is", im.width, "x", im.height)

	# Checking if the size of the image correspond to a Rubik's cube fresco.
	if int(im.width%3) != 0 or int(im.height%3) != 0:

		# Creating a log file with an error message if the size is not made for Rubik's cubes.
		f = open("./lastest.log", "w")
		f.write("launched on "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S" + "\n"))
		f.write("Image is not a Rubik's sized\n")
		f.close()

		# Stop the code with an error's code 0.
		sys.exit(0)

	else:

		# Creating a log file with the size of the image in pixels.
		f = open("./lastest.log", "w")
		f.write("launched on "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S" + "\n"))
		f.write("Asked : " + cube + "\n")
		f.write("Image is a Rubik's sized\n")
		f.write("Image is " + str(im.width) + "px x " + str(im.height) + "px\n")


		# Get the number of Rubik's cube by dividing the size by 3.
		cubesWidth = int(im.width/3)
		cubesHeight = int(im.height/3)

		# Displaying the number of pixels transformed in Rubik's cubes.
		print(str("Width is " + str(im.width) + "px and it's equal to " + str(cubesWidth) + "rc"))
		print(str("Height is " + str(im.height) + "px and it's equal to " + str(cubesHeight) + "rc"))

		# Getting size's exceptions.
		if cubesHeight > 26:
			first = cubesHeight/26
			second = cubesHeight%26
			first = int(first)
			row = (chr((64+first)) + chr(64+second))
		else:
			row = str(chr(64+cubesHeight))

		# Displaying the range of the slots of the fresco.
		f.write("cubes from A1 to " + str(row + str(cubesWidth)) + "\n")
		print("cubes from A1 to " + str(row + str(cubesWidth)))


		# Check if a cube has been selected.
		if cube == "":
			f.write("No cube selected.\n")


		# Check if the selected cube has a classic format (e.g. A1, B2, C3, etc.)
		if len(cube) > 2:

			# Creating temporary strings to separate the letters and the numbers.
			tempS = str()
			tempI = str()

			cube = cube.upper()

			# Separate the letters and the numbers.
			for i in cube:
				if 65 <= ord(i) <= 90:	# Get the letters
					tempS = tempS + i
				else: 					# Get the numbers
					tempI = tempI + i

			# Transform the letters to an int in order to get the height in pixels.
			if len(tempS) > 1:
				h = (((ord(tempS[0])-64) * 26) + (ord(tempS[1])-64))
			else:
				h = ord(tempS)-64

			# Transform the numbers to an int in order to get the width in pixels.
			if len(tempI) > 1:
				w = (((ord(tempI[0])-48) * 10) + (ord(tempI[1])-48))
			else:
				w = ord(tempI)-48

		else:

			# Transform the string to an int.
			h = ord(cube[0])-64
			w = ord(cube[1])-48


		# Convert the image to RGB to get the colors.
		imRGB = im.convert('RGB')

		# Get the list of colors for each pixel.
		pixels = list(imRGB.getdata())

		# Get the size of the image.
		width, height = im.size

		pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

		# Make an array with the selected pixels.
		rubik = [
					pixels[(h-1)*3+2][((w-1)*3):w*3], 
					pixels[(h-1)*3+1][((w-1)*3):w*3],
					pixels[(h-1)*3][((w-1)*3):w*3]
				]

		# Create a new image with colors.
		# Load all the pixels from this new image as well.
		new_image = Image.new('RGB', (300, 300))
		new_pixel_map = new_image.load()

		# Modify each pixel in the new image.
		for x in range(300):
			for y in range(300):
				# Copy the original pixel to the new pixel map.
				new_pixel_map[x, y] = rubik[int(x/100)][int(y/100)]

		# Rotate the image to have it in the right direction.
		new_image = new_image.rotate(90)

		# Save the image in the parent directory.
		new_image.save('cube.png')

		f.close()

def Part(cube):
	
	# Selecting input image.
	im = Image.open("./final.png")


	# Get the number of Rubik's cube by dividing the size by 3.
	cubesWidth = int(im.width/3)
	cubesHeight = int(im.height/3)

	# Getting size's exceptions.
	if cubesHeight > 26:
		first = cubesHeight/26
		second = cubesHeight%26
		first = int(first)
		row = (chr((64+first)) + chr(64+second))
	else:
		row = str(chr(64+cubesHeight))

		# Check if the selected cube has a classic format (e.g. A1, B2, C3, etc.)
	if len(cube) > 2:

		# Creating temporary strings to separate the letters and the numbers.
		tempS = str()
		tempI = str()

		cube = cube.upper()

		# Separate the letters and the numbers.
		for i in cube:
			if 65 <= ord(i) <= 90:	# Get the letters
				tempS = tempS + i
			else: 					# Get the numbers
				tempI = tempI + i

		# Transform the letters to an int in order to get the height in pixels.
		if len(tempS) > 1:
			h = (((ord(tempS[0])-64) * 26) + (ord(tempS[1])-64))
		else:
			h = ord(tempS)-64

		# Transform the numbers to an int in order to get the width in pixels.
		if len(tempI) > 1:
			w = (((ord(tempI[0])-48) * 10) + (ord(tempI[1])-48))
		else:
			w = ord(tempI)-48

	else:

		# Transform the string to an int.
		h = ord(cube[0])-64
		w = ord(cube[1])-48


	# Convert the image to RGB to get the colors.
	imRGB = im.convert('RGB')

	# Get the list of colors for each pixel.
	pixels = list(imRGB.getdata())

	# Get the size of the image.
	width, height = im.size

	pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

	# Make an array with the selected pixels.
	one = []
	two = []
	three = []
	four = []
	five = []
	six = []
	seven = []
	eight = []
	nine = []
	ten = []
	eleven = []
	twelve = []
	thirteen = []
	fourteen = []
	fifteen = []
	count = 1
	for j in range(-6, 9):
		for i in range(-6, 9):
			if ((h-1)*3+j) < 0 or ((h-1)*3+j) >= 99 or ((w-1)*3+i) >= 261 or ((w-1)*3+i) < 0:
				match count:
					case 1: one.append((0, 0, 0))
					case 2: two.append((0, 0, 0))
					case 3: three.append((0, 0, 0))
					case 4: four.append((0, 0, 0))
					case 5: five.append((0, 0, 0))
					case 6: six.append((0, 0, 0))
					case 7: seven.append((0, 0, 0))
					case 8: eight.append((0, 0, 0))
					case 9: nine.append((0, 0, 0))
					case 10: ten.append((0, 0, 0))
					case 11: eleven.append((0, 0, 0))
					case 12: twelve.append((0, 0, 0))
					case 13: thirteen.append((0, 0, 0))
					case 14: fourteen.append((0, 0, 0))
					case 15: fifteen.append((0, 0, 0))
					case _: print("Error")
			else:
				match count:
					case 1: one.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 2: two.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 3: three.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 4: four.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 5: five.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 6: six.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 7: seven.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 8: eight.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 9: nine.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 10: ten.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 11: eleven.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 12: twelve.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 13: thirteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 14: fourteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case 15: fifteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
					case _: print("Error")
		count += 1


	rubik = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen]
	

	# Create a new image with colors.
	# Load all the pixels from this new image as well.
	new_image = Image.new('RGB', (375, 375))
	new_pixel_map = new_image.load()

	# Modify each pixel in the new image.
	for x in range(0, 374):
		for y in range(0, 374):
			if x == 150 and 224 >= y >= 150 or x == 224 and 150 <= y <= 224 or y == 150 and 224 >= x >= 150 or y == 224 and 150 <= x <= 224 or x == 149 and 225 >= y >= 149 or x == 225 and 149 <= y <= 225 or y == 149 and 225 >= x >= 149 or y == 225 and 149 <= x <= 225 :
				new_pixel_map[x, y] = (0, 0, 0)
			else:
				# Copy the original pixel to the new pixel map.
				new_pixel_map[x, y] = rubik[int(x/25)][int(y/25)]

	# Rotate the image to have it in the right direction.
	new_image = new_image.rotate(-90)
	new_image = new_image.transpose(Image.FLIP_LEFT_RIGHT)

	# Save the image in the parent directory.
	new_image.save('part.png')

new_image = Image.new('RGB', (300, 300))
new_image2 = Image.new('RGB', (375, 375))
new_image.save('./cube.png')
new_image2.save('./part.png')
finder("A1")
Part("A1")

# GUI

# Creating a class to create the GUI.
class MyFrame(wx.Frame):
	def __init__(self):
		letters = Letters("AG")
		numbers = Numbers("87")
		global l1
		global l2
		super().__init__(parent=None, title='Rubik\'s finder')
		inp1 = wx.StaticText(self, label="Input", pos=(0, 0))
		l1 = wx.TextCtrl(self,  pos=(80, 0))
		l1.SetMaxLength(4)
		Submit = wx.Button(self, label="Submit", pos=(0, 100))
		Submit.Bind(wx.EVT_BUTTON, self.OnClicked)
		global img
		img = wx.Image("cube.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		img2 = wx.Image("part.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()

		self.bitmap1 = wx.StaticBitmap(self, -1, img, (200, 0))
		self.bitmap2 = wx.StaticBitmap(self, -1, img2, (600, 0))

		self.ShowFullScreen(True, style=wx.FULLSCREEN_NOTOOLBAR)

		self.Show()





	def OnClicked(self, event):
		out = (l1.GetValue())
		print(out)
		finder(out)
		Part(out)
		self.Destroy()
		MyFrame()



def Letters(inp):
	out = list()
	if len(inp) > 1:
		tot = (((ord(inp[0])-64) * 26) + (ord(inp[1])-64))
	else:
		tot = ord(inp)-64
	for i in range(1, tot+1):
		if i > 26:
			first = i/26
			second = i%26
			first = int(first)
			out.append(chr((64+first)) + chr(64+second))
		else:
			out.append(chr(i+64))
	return out

def Numbers(inp):
	out = list()
	if len(inp) > 1:
		tot = (((ord(inp[0])-48) * 10) + (ord(inp[1])-48))
	for i in range(1, tot+1):
		out.append(str(i))
	return out

def CreateCube():
	new_image = Image.new('RGB', (300, 300))
	new_image.save('./cube.png')
	new_image2 = Image.new('RGB', (375, 375))
	new_image2.save('./part.png')


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()