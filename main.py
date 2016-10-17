from PIL import Image, ImageDraw, ImageFont
import sys
import os
from config import config
from time import sleep
from slideLeft import slideLeft
from github import Github
from initials import *

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
        draw = ImageDraw.Draw(image)
        font = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) +
                              '/helvR08.pil')
        g = Github(self.conf.get_github_user(), password=self.conf.get_github_password())
        s = [slideLeft(repos(g), font), slideLeft(commits(g), font)]
        try:
            while self.alive:
                img = s[0].draw()
                if img is not None:
                    self.updateMatrix(img)
                else:
                    self.matrix.Clear()
                    temp = s.pop(0)
                    temp.update()
                    s.insert(len(s), temp)
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
