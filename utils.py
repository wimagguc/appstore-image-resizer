from PIL import Image, ImageOps
from os import walk
import re

def list_of_files(path=None):
    list = []

    imageregex = re.compile('\.(png|jpg)$', re.IGNORECASE)

    for (dirpath, dirnames, filenames) in walk(path):
        for f in filenames:
            if imageregex.search(f):
                list.append(f)
        break

    return list

def save_to_file(img=None, path=None):
    if not img or not path:
        return None
    img.save(path)

def resize_to_width(imageFile=None, width=100, height=100):
    if not imageFile:
        return None

    img = Image.open(imageFile)

    size = (width, height)
    centering = (0, 0)

    return ImageOps.fit(img, size, method=Image.ANTIALIAS, centering=centering)
