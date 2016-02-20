from PIL import Image

config = dict(line.strip().split('=') for line in open('config.txt'))

if config["DEBUG"]:
    from matrixtoolkit import Adafruit_RGBmatrix
else:
    from rgbmatrix import Adafruit_RGBmatrix


def main():
    image = Image.open('resources/invertocat.png')
    matrix.SetImage(image, 48, 0)


def kill():
    pass

if __name__ == '__main__':
    matrix = Adafruit_RGBmatrix(32, 4)
    matrix.start(main, kill)
