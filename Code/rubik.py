from PIL import Image 				# Importing the Image module from the PIL library to 
import sys							# Importing the sys module to stop the code if an error occurs.
from datetime import datetime		# Importing the datetime module to get the date and time of the launch of the code.


# Selecting input image.
im = Image.open("./last.jpg")

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
	f.write("Image is a Rubik's sized\n")
	f.write("Image is " + str(im.width) + "px x " + str(im.height) + "px\n")


	# Get the number of Rubik's cube by dividing the size by 3.
	cubesWidth = int(im.width/3)
	cubesHeight = int(im.height/3)

	# Adding the number of pixels in the log file.
	f.write(str("Width is " + str(im.width) + "px and it's equal to " + str(cubesWidth) + "rc\n"))
	f.write(str("Height is " + str(im.height) + "px and it's equal to " + str(cubesHeight) + "rc\n"))

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

	# Asking the cube wanted.
	f.write("choosing a cube...")
	print("Choose a cube :\n")
	cube = str(input())

	# Check if a cube has been selected.
	if cube == "":
		f.write("No cube selected.\n")


	# Check if the selected cube has a classic format (e.g. A1, B2, C3, etc.)
	if len(cube) > 2:

		# Creating temporary strings to separate the letters and the numbers.
		tempS = str()
		tempI = str()

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
	rubik = [pixels[(h-1)*3+2][((w-1)*3):w*3], pixels[(h-1)*3+1][((w-1)*3):w*3],pixels[(h-1)*3][((w-1)*3):w*3]]

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


# GUI

