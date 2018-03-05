import numpy as np
import re
from PIL import Image, ImageEnhance

# https://pillow.readthedocs.io/en/latest/reference/ImageEnhance.html

def kabuki_kidpix( image_filename, size, thresh ):

    thumb_filename = re.sub('\.jpg','_thumb.jpg',image_filename)
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
    
    # save thumbnail
    concolim.thumbnail(size)
    concolim.save("ghlogox_thumb.jpg")
    
    # make binary mask
    thresh = BRIGHTNESS_THRESHOLD
    arr = np.array(concolim)
    arr[arr<thresh] = 0
    arr[arr>=thresh] = 255
    
    # save binary mask
    im2 = Image.fromarray(arr)
    im2.save("ghlogox_mask.jpg")


if __name__=="__main__":

    FINAL_SIZE = 100,100
    BRIGHTNESS_THRESHOLD = 150

    kabuki_kidpix("ghlogo.jpg",FINAL_SIZE,BRIGHTNESS_THRESHOLD)

    kabuki_kidpix("ghlogox.jpg",FINAL_SIZE,BRIGHTNESS_THRESHOLD)

