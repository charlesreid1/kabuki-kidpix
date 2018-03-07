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

if __name__=="__main__":

    FINAL_SIZE = 75,75
    BRIGHTNESS_THRESHOLD = 150

    mask = kabuki_mask("ghlogo.jpg",FINAL_SIZE,BRIGHTNESS_THRESHOLD)
    arr = np.array(mask)
    print(np.shape(arr))

    # We are constructing a list of dictionaries
    # One key per dictionary, one row per dictionary
    # Each row of the image is one key of the dictionary
    initdicts = []
    for row in range(np.shape(arr)[0]):

        columns_in_this_row = []

        # Check each column in this row 
        # to see if it is bright (switched on)
        for col in range(np.shape(arr)[1]):
            px = arr[row][col][0]
            if(px>BRIGHTNESS_THRESHOLD):
                columns_in_this_row.append(col)

        # Assemble the dictionary
        if(len(columns_in_this_row)>0):
            d = {}
            d[str(row)] = columns_in_this_row
            initdicts.append(d)


    result_badquotes = ",".join([str(d) for d in initdicts])
    result_goodquotes = re.sub("'","\"",result_badquotes)
    
    print()
    print("Here is your final string:")
    print()
    print("initialState : '[%s]',"%(result_goodquotes) )



