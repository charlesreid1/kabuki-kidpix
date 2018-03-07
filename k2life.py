import re
import numpy as np
from kabuki import kabuki_mask

# We want to use the output 
# of kabuki kidpix to initialize
# a Game of Life grid.
#
# Here is the format that Life expects:
# 
# initialState : '[{"39":[60]},{"40":[62]},{"41":[59,60,63,64,65]}]',
#
# '[ 
#       { "<row-id>" : [<col-id>, <col-id>, <col-id>],
#         "<row-id>" : [<col-id>, <col-id>],
#         "<row-id>" : [<col-id>, <col-id>, <col-id>, <col-id>]
#       }
#  ]'
#
# . * . . . . . . 
# . . . * . . . . 
# * * . . * * * .
# . . . . . . . .

def cocacola():
    kabuki_js("cocacola.png")

def github():
    kabuki_js("ghlogo.jpg")

def kabuki_js(img_filename, **kwargs):

    if('final_size' not in kwargs.keys()):
        kwargs['final_size'] = (100,100)
    if('brightness_threshold' not in kwargs.keys()):
        kwargs['brightness_threshold'] = 200
    if('padding_left' not in kwargs.keys()):
        kwargs['padding_left'] = 0
    if('padding_top' not in kwargs.keys()):
        kwargs['padding_top'] = 0

    mask = kabuki_mask(img_filename,kwargs['final_size'],kwargs['brightness_threshold'])
    arr = np.array(mask)

    # We are constructing a list of dictionaries
    # One key per dictionary, one row per dictionary
    # Each row of the image is one key of the dictionary
    initdicts = []
    for row in range(np.shape(arr)[0]):

        columns_in_this_row = []

        # Check each column in this row 
        # to see if it is bright (switched on)
        for col in range(np.shape(arr)[1]):
            px = arr[row][col][3]
            if(px>kwargs['brightness_threshold']):
                columns_in_this_row.append(col + kwargs['padding_left'])

        # Assemble the dictionary
        if(len(columns_in_this_row)>0):
            d = {}
            d[str(row + kwargs['padding_top'])] = columns_in_this_row
            initdicts.append(d)


    result_badquotes = ",".join([str(d) for d in initdicts])
    result_goodquotes = re.sub("'","\"",result_badquotes)
    
    print()
    print("Here is your final string:")
    print()
    print("GOL.initialState = '[%s]';"%(result_goodquotes) )


if __name__=="__main__":
    cocacola()
    github()

