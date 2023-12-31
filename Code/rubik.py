from PIL import Image 				# Importing the Image module from the PIL library to 
import sys							# Importing the sys module to stop the code if an error occurs.
from datetime import datetime		# Importing the datetime module to get the date and time of the launch of the code.
import wx	# Importing the wxPython library to create a GUI.



def finder(cube):

	# Selecting input image.
	im = Image.open("./final.png")

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
		cubes_width = int(im.width/3)
		cubes_height = int(im.height/3)

		# Getting size's exceptions.
		if cubes_height > 26:
			first = cubes_height/26
			second = cubes_height%26
			first = int(first)
			row = (chr((64+first)) + chr(64+second))
		else:
			row = str(chr(64+cubes_height))

		# Displaying the range of the slots of the fresco.
		f.write("cubes from A1 to " + str(row + str(cubes_width)) + "\n")


		# Check if a cube has been selected.
		if cube == "":
			f.write("No cube selected.\n")


		# Check if the selected cube has a classic format (e.g. A1, B2, C3, etc.)
		if len(cube) > 2:

			# Creating temporary strings to separate the letters and the numbers.
			temp_string = str()
			temp_int = str()

			cube = cube.upper()

			# Separate the letters and the numbers.
			for i in cube:
				if 65 <= ord(i) <= 90:	# Get the letters
					temp_string = temp_string + i
				else: 					# Get the numbers
					temp_int = temp_int + i

			# Transform the letters to an int in order to get the height in pixels.
			if len(temp_string) > 1:
				h = (((ord(temp_string[0])-64) * 26) + (ord(temp_string[1])-64))
			else:
				h = ord(temp_string)-64

			# Transform the numbers to an int in order to get the width in pixels.
			if len(temp_int) > 1:
				w = (((ord(temp_int[0])-48) * 10) + (ord(temp_int[1])-48))
			else:
				w = ord(temp_int)-48

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

def part(cube):
	
	# Selecting input image.
	im = Image.open("./final.png")


	# Get the number of Rubik's cube by dividing the size by 3.
	cubes_height = int(im.height/3)

	# Getting size's exceptions.
	if cubes_height > 26:
		first = cubes_height/26
		second = cubes_height%26
		first = int(first)
		row = (chr((64+first)) + chr(64+second))
	else:
		row = str(chr(64+cubes_height))

		# Check if the selected cube has a classic format (e.g. A1, B2, C3, etc.)
	if len(cube) > 2:

		# Creating temporary strings to separate the letters and the numbers.
		temp_string = str()
		temp_int = str()

		cube = cube.upper()

		# Separate the letters and the numbers.
		for i in cube:
			if 65 <= ord(i) <= 90:	# Get the letters
				temp_string = temp_string + i
			else: 					# Get the numbers
				temp_int = temp_int + i

		# Transform the letters to an int in order to get the height in pixels.
		if len(temp_string) > 1:
			h = (((ord(temp_string[0])-64) * 26) + (ord(temp_string[1])-64))
		else:
			h = ord(temp_string)-64

		# Transform the numbers to an int in order to get the width in pixels.
		if len(temp_int) > 1:
			w = (((ord(temp_int[0])-48) * 10) + (ord(temp_int[1])-48))
		else:
			w = ord(temp_int)-48

	else:

		# Transform the string to an int.
		h = ord(cube[0])-64
		w = ord(cube[1])-48


	# Convert the image to RGB to get the colors.
	im_rgb = im.convert('RGB')

	# Get the list of colors for each pixel.
	pixels = list(im_rgb.getdata())

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
				if count == 1:
					one.append((0, 0, 0))
				elif count == 2:
					two.append((0, 0, 0))
				elif count == 3:
					three.append((0, 0, 0))
				elif count == 4:
					four.append((0, 0, 0))
				elif count == 5:
					five.append((0, 0, 0))
				elif count == 6:
					six.append((0, 0, 0))
				elif count == 7:
					seven.append((0, 0, 0))
				elif count == 8:
					eight.append((0, 0, 0))
				elif count == 9:
					nine.append((0, 0, 0))
				elif count == 10:
					ten.append((0, 0, 0))
				elif count == 11:
					eleven.append((0, 0, 0))
				elif count == 12:
					twelve.append((0, 0, 0))
				elif count == 13:
					thirteen.append((0, 0, 0))
				elif count == 14:
					fourteen.append((0, 0, 0))
				elif count == 15:
					fifteen.append((0, 0, 0))
				else:
					print("Error")

			else:
				if count == 1:
					one.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 2:
					two.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 3:
					three.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 4:
					four.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 5:
					five.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 6:
					six.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 7:
					seven.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 8:
					eight.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 9:
					nine.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 10:
					ten.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 11:
					eleven.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 12:
					twelve.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 13:
					thirteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 14:
					fourteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				elif count == 15:
					fifteen.append(pixels[(h-1)*3+j][((w-1)*3+i)])
				else:
					print("Error")
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
part("A1")

# GUI

# Creating a class to create the GUI.
class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title='Rubik\'s finder', size=(1200, 675))
		text_label = wx.StaticText(self, label="Input", pos=(0, 0))

		global text_input
		text_input = wx.TextCtrl(self,  pos=(80, 0), size=(100,22))
		text_input.SetMaxLength(4)
		submit_button = wx.Button(self, label="Submit", pos=(0, 100))
		submit_button.Bind(wx.EVT_BUTTON, self.OnClicked)
		output_cube = wx.Image("cube.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		output_part = wx.Image("part.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()

		self.bitmap1 = wx.StaticBitmap(self, -1, output_cube, (200, 0))
		self.bitmap2 = wx.StaticBitmap(self, -1, output_part, (600, 0))

		self.Show()


	def OnClicked(self, event):
		out = (text_input.GetValue())
		print(out.upper())
		finder(out)
		part(out)
		self.Destroy()
		MyFrame()


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()