from PIL import Image
from tkinter.filedialog import askopenfile
import rich


class ImageToAscii:
    def __init__(self):
        image_path = askopenfile().name
        print(image_path)
        self.img = Image.open(image_path)
        self.convertToRGBA()
        self.resize()
        self.main()
        

    def convertToRGBA(self):
        bands = self.img.getbands()
        if len(bands) == 1 or len(bands) == 3:
            self.img = self.img.convert("RGBA")

    def resize(self):
        self.width, self.height = self.img.size
        aspect_ratio = self.height / self.width
        self.new_width = int(input())
        self.new_height = aspect_ratio * self.new_width / 2
        self.img = self.img.resize((self.new_width, int(self.new_height)))

    def main(self):
        lista = []
        pixels = self.img.getdata()
        for pixel in pixels:
            lista.append(pixel)

        img = self.img.convert("L")

        pixels = img.getdata()

        chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft_-~i!lI;:,\"^`'. "[::-1]
        charArray = list(chars)
        charLength = len(charArray)
        interval = charLength / 256
        import math

        def getChar(inputInt, col):

            r, g, b, a = col

            return "[rgb({},{},{})]{}[/]".format(
                r, g, b, charArray[math.floor(inputInt * interval)]
            )

        new_pixels = [getChar(pixel, col) for pixel, col in zip(pixels, lista)]

        new_pixels_count = len(new_pixels) + len(str(lista))
        self.ascii_image = [
            new_pixels[index : index + self.new_width]
            for index in range(0, new_pixels_count, self.new_width)
        ]
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

    def show(self):
        rich.print(self.ascii_image)

    def saveText(self):
        with open("output.html", "w") as fp:
            fp.write(self.ascii_image)


img = ImageToAscii()
img.show()
