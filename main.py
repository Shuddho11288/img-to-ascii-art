import sys
from PIL import Image
from tkinter.filedialog import askopenfile
# get image path
image_path = askopenfile().name
print(image_path)
img = Image.open(image_path)

# resizing the image
width, height = img.size
aspect_ratio = height/width
new_width = 300 #How much clear you want to see
new_height = (aspect_ratio*new_width/2)
img = img.resize((new_width, int(new_height)))


# convert image to greyscale format
img = img.convert('L')
#img = img.convert('1') #for lite mode.

pixels = img.getdata()

# replace each pixel with a character from array

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256
import math


def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]
new_pixels = [getChar(pixel) for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)
