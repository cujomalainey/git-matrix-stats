from PIL import Image, ImageDraw, ImageFont
import sys
import os
from config import config

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
        image = Image.open('resources/invertocat.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) +
                              '/helvR08.pil')
        fontYoffset = -2  # Move up a couple lines so descenders aren't cropped
        for i in range(0, 4):
            draw.text((0, i*8 + fontYoffset), "BLOAT!!", font=font,
                      fill=(255, 0, 0))
        self.matrix.SetImage(image, 48, 0)
        try:
            while self.alive:
                pass
        except KeyboardInterrupt:
            self.kill()

    def kill(self):
        self.alive = False

if __name__ == '__main__':
    d = drawer(conf)
    d.run()
