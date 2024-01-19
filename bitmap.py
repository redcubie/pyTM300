import pyTM300
import cv2
import time

pyTM300.open('com4')
pyTM300.initialize()
pyTM300.home()
pyTM300.unidirectional(True)
pyTM300.ser.write(pyTM300.const.ESC_3 + int(16).to_bytes(1,"big"))

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
    pyTM300.bitmap(bytestring)
    time.sleep(0.5)

#pyTM300.ser.write(b"\n")
pyTM300.ser.write(b"\n\n\n\n\n\n\n\n\n")
pyTM300.ser.write(b"\n\n\n\n\n\n\n\n\n")
pyTM300.ser.write(pyTM300.const.ESC_2)

sel = input("cut? (Y/n) ")
if not sel or sel in ["y", "Y"]:
    pyTM300.cut(1)
