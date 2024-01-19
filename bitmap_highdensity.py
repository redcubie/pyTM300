# HIGH DENSITY
from pyTM300 import TM300, const
import cv2
import time

printer = TM300('com4')
printer.initialize()
printer.home()
printer.unidirectional(True)
printer.write(const.ESC_3 + int(16).to_bytes(1,"big"))

imageorg = cv2.imread(input("filename: ").strip('"'))
imagegray = cv2.cvtColor(imageorg, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(imagegray, 127, 1, cv2.THRESH_BINARY_INV)
rows, cols = img.shape

for i in range(rows//8):
    bytestring = b""
    row = i*8
    for j in range(cols):
        pixels = 0
        for k in range(8):
            pixels = (pixels<<1)+img[row+k, j]
        bytestring += int(pixels).to_bytes(1, "big")
    # print(bytestring)
    printer.bitmap(bytestring, density=1)
    time.sleep(0.5)

# pyTM300.write(b"\n")
printer.write(b"\n\n\n\n\n\n\n\n\n")
printer.write(b"\n\n\n\n\n\n\n\n\n")
printer.write(const.ESC_2)
