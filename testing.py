#!/usr/bin/env python3

import pyTM300

pyTM300.open("COM5")
pyTM300.initialize()

bitmap = b'\x11\x23\x65\x87\x76\x34'

pyTM300.bitmap(bitmap)

pyTM300.ser.write(b'\n\n\n\n\n\n\n\n')
pyTM300.cut()

pyTM300.close()