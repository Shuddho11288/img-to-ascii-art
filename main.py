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
new_width = 120
new_height = (aspect_ratio*new_width/2)
img = img.resize((new_width, int(new_height)))


# convert image to greyscale format
img = img.convert('L')
#img = img.convert('1') #for lite mode.

pixels = img.getdata()

# replace each pixel with a character from array

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

new_pixels = [chars[int(pixel*0.27450980392)] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)
