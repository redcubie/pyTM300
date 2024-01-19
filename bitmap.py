#!/usr/bin/env python3

# Instructions:
#   change serial port
#   Run
#   Copy filename of image file to text input
#   see printed image
#
# Image width should be 200 pixels and height divisible by 8, prepare image for monochrome separately.
# Density is 80 DPI horizontally and 72 DPI vertically. (TM300; for other models, see manual)

from pyTM300 import TM300, const
import cv2
import time

PORT = "com4"

# printer initialization
printer = TM300(PORT)
printer.initialize()
printer.home()
printer.unidirectional(True)

# set line feed height for graphics
printer.write(const.ESC_3 + int(16).to_bytes(1,"big"))

# get image from file
imageorg = cv2.imread(input("filename: ").strip('"'))

# convert image to B&W
imagegray = cv2.cvtColor(imageorg, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(imagegray, 127, 1, cv2.THRESH_BINARY_INV)

rows, cols = img.shape
for i in range(rows//8): # for each 8 pixel high chunk of rows
    bytestring = b""
    row = i*8
    for j in range(cols): # for each column in the chunk
        pixels = 0 # byte value for this strip
        for k in range(8): # for each pixel
            pixels = (pixels<<1) | img[row+k, j] # shift previous pixels and add new pixel's value
        bytestring += int(pixels).to_bytes(1, "big") # append strip to datastream
    # print(bytestring)
    printer.bitmap(bytestring) # send chunk to printer
    time.sleep(0.5) # allow time to print (but flow control should handle it??)

# newlines to get printed image above cutter
# if text is to be printed, it will start right below the image
#printer.ser.write(b"\n")
printer.write(b"\n\n\n\n\n\n\n\n\n")
printer.write(b"\n\n\n\n\n\n\n\n\n")
printer.write(const.ESC_2)

sel = input("cut? (Y/n) ")
if not sel or sel in ["y", "Y"]:
    printer.cut(1)
