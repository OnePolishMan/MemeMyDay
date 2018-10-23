from io import BytesIO
from PIL import Image, ImageTk
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen, urlretrieve


class Img:
    global_index = 0

    def __init__(self, url):
        self.img = Img.create_image_from_url(url)
        self.index = Img.global_index
        Img.global_index += 1

    def create_image_from_url(url):
        file = BytesIO(urlopen(url).read())
        _img = ImageTk.PhotoImage(Image.open(file))

        return _img
