import numpy as np
import re
from PIL import Image, ImageEnhance

# https://pillow.readthedocs.io/en/latest/reference/ImageEnhance.html

"""
Kabuki

This blurs and pixelates an image,
and obtains a binary mask for it.

The binary mask can then be converted
to a 2D 0s and 1s array, and passed
to k2life.py to make a Life grid
"""

def kabuki_mask( image_filename, size, thresh ):

    mask_filename  = re.sub('\.jpg','_mask.jpg',image_filename)

    # open image
    im = Image.open(image_filename)

    # high contrast step
    contraster = ImageEnhance.Contrast(im)
    conim = contraster.enhance(1.0)

    # de-colorize step
    colorizer = ImageEnhance.Color(conim)
    concolim = colorizer.enhance(0.0)
    
    # sharpen edges step
    sharpenerizer = ImageEnhance.Sharpness(concolim)
    sconcolim = sharpenerizer.enhance(2.0)
    
    # shrinkify
    concolim.thumbnail(size)
    
    # make binary mask
    arr = np.array(concolim)
    arr[arr<thresh] = 0
    arr[arr>=thresh] = 255
    
    # save binary mask
    im2 = Image.fromarray(arr)
    im2.save(mask_filename)

    return im2


if __name__=="__main__":

    FINAL_SIZE = 100,100
    BRIGHTNESS_THRESHOLD = 150

    _ = kabuki_mask("ghlogo.jpg",FINAL_SIZE,BRIGHTNESS_THRESHOLD)
    _ = kabuki_mask("ghlogox.jpg",FINAL_SIZE,BRIGHTNESS_THRESHOLD)

