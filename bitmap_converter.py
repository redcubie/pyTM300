#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys

image = Image.open(sys.argv[1])
image_array = np.array(image)

if image_array.shape[0] % 8:
    fill_height = 8 - (image_array.shape[0] % 8)
    fill_width = image_array.shape[1]
    
    fill_array = np.zeros((fill_height, fill_width))
    image_array = np.hstack(image_array, fill_array)

image_out = b''

for i in range(int(image_array.shape[0]/8)):
    for j in range(image_array.shape[1]):
        column = 0
        for k in range(i*8, (i+1)*8):
            index = (8-(k % 8) if k % 8 else 0)
            column += image_array[k, j] << index
        image_out += bytes(column)


print("length: "+str(len(image_out)))

print("data: "+str(image_out))
input()
