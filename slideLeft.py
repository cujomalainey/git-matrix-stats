from drawable import drawable
from PIL import Image, ImageDraw
import time


class slideLeft(drawable):
    """
    slides text in from left
    """

    def __init__(self, feed, font):
        self.image = Image.new('RGB', (128, 32))
        self.drw = ImageDraw.Draw(self.image)
        self.done = False
        self.font = font
        self.delay = 80
        self.feed = feed
        self.data = []
        self.data_list = []
        self.update()

    def nextFrame(self):
        self.drw.rectangle([(0, 0), (128, 32)], fill=(0, 0, 0))
        i = 0
        self.done = True
        for line in self.data:
            if line["x"] > (int(i/4))*64:
                self.done = False
                self.time = time.time()
                line["x"] -= 1
                break
            i += 1
        if self.done is True and time.time() - self.time < 10:
            self.done = False
        i = 1
        for line in self.data:
            self.drw.text((line["x"], line["y"] + drawable.fontYoffset),
                          str(i) + "." + line["text"] + " ",
                          font=self.font, fill=(255, 255, 255))
            i += 1

    def update(self):
        self.data_list = self.feed.fetch()
        self.data = [{"text": text[0:16], "x": 129} for text in self.data_list]
        i = 0
        for line in self.data:
            line["y"] = 8 * (i % 4)
            i += 1

    def draw(self):
        self.nextFrame()
        return self.image if not self.done else None
