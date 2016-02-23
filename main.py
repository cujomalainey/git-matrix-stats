from PIL import Image, ImageDraw, ImageFont
import sys
import os
from config import config
from time import sleep
from slideLeft import slideLeft

try:
    conf = config('config.txt')
except IOError as e:
    print("No config.txt file found, please make one")
    exit()


if conf.off_target():
    from matrixtoolkit import Adafruit_RGBmatrix
else:
    from rgbmatrix import Adafruit_RGBmatrix


class drawer():
    """
    handles controls what is being drawn
    """

    def __init__(self, conf):
        self.matrix = Adafruit_RGBmatrix(32, 4)
        self.conf = conf
        self.alive = True

    def run(self):
        if conf.off_target():
            self.matrix.start(self.main, self.kill)
        else:
            self.main()

    def main(self):
        self.image = Image.new('RGB', (128, 32))
        image = Image.open('resources/invertocat.png')
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) +
                              '/helvR08.pil')
        s = slideLeft(None, font)
        # draw.text((45, 0 + fontYoffset), "Tamarabyte", font=font,
        #           fill=(50, 50, 50))
        # draw.text((0, 0 + fontYoffset), "cujomalainey ", font=font,
        #           fill=(50, 50, 50))
        # draw.text((0, 16 + fontYoffset), "gantonious", font=font,
        #           fill=(50, 50, 50))
        # draw.text((0, 24 + fontYoffset), "JesseFarebro", font=font,
        #           fill=(50, 50, 50))
        # for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        #     self.image = Image.new('RGB', (128, 32))
        #     draw = ImageDraw.Draw(self.image)
        #     draw.text((0, 0 + fontYoffset), letter + " " + letter, font=font,
        #               fill=(255, 255, 255))
        #     sleep(0.5)
        try:
            while self.alive:
                img = s.draw()
                if img is not None:
                    self.updateMatrix(img)
                else:
                    self.matrix.Clear()
        except KeyboardInterrupt:
            self.kill()

    def updateMatrix(self, image):
        self.matrix.SetImage(image if self.conf.off_target() else
                             image.im.id, 0, 0)

    def kill(self):
        self.alive = False

if __name__ == '__main__':
    d = drawer(conf)
    d.run()
