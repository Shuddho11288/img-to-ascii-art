import sys
from PIL import Image
from tkinter.filedialog import askopenfile
import rich
# get image path
class ImageToAscii:
    def __init__(self):
        image_path = askopenfile().name
        print(image_path)
        img = Image.open(image_path)

        # resizing the image
        width, height = img.size
        aspect_ratio = height/width
        new_width = int(input())
        new_height = (aspect_ratio*new_width/2)
        img = img.resize((new_width, int(new_height)))

        lista = []
        pixels = img.getdata()
        for pixel in pixels:
            lista.append(pixel)
        #print(lista)
        #rich.print(lista)
        # convert image to greyscale format
        img = img.convert('L')
        #img = img.convert('1') #for lite mode.

        pixels = img.getdata()

        # replace each pixel with a character from array

        chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?+<>_-~i!lI;:,\"^`'."
        charArray = list(chars)
        charArray.append("<span style='background-color:rgba(0,0,0,0)'>H</span>")
        charArray = charArray[::-1]
        charLength = len(charArray)
        interval = charLength/256
        import math

        chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft. "
        chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft_-~i!lI;:,\"^`'."
        charArray = list(chars)
        charLength = len(charArray)
        interval = charLength/256
        import math




        def getChar(inputInt,col):
            #rich.print(f"[rgb{col}]"+charArray[math.floor(inputInt*interval)]+f"[/rgb{col}]")
            try:
                r,g,b,a  = col
            except Exception:
                r,g,b  = col
            print("[rgb{}]{}[/]".format((r,g,b),charArray[math.floor(inputInt*interval)]))
            return "[rgb({},{},{})]{}[/]".format(r,g,b,charArray[math.floor(inputInt*interval)])
        new_pixels = [getChar(pixel,col) for pixel,col in zip(pixels,lista)]
        
        #rich.print(new_pixels)

        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)+len(str(lista))
        self.ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        final_res = []
        for x in self.ascii_image:
            final_res.append("".join(x))
        while True:
            try:
                final_res.remove("")
            except Exception:
                break
        final_res = "\n".join(final_res)
        self.ascii_image = final_res
        #self.ascii_image = "<br>".join(self.ascii_image)
    
    def show(self):
        rich.print(self.ascii_image)
    def saveText(self):
        with open("output.html","w") as fp:
            fp.write(self.ascii_image)

img = ImageToAscii()
img.show()
