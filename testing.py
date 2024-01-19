#!/usr/bin/env python3

from pyTM300 import TM300, const

printer = TM300("COM5")
printer.initialize()

bitmap = b'\x11\x23\x65\x87\x76\x34'

printer.bitmap(bitmap)

printer.write(b'\n\n\n\n\n\n\n\n')
printer.cut()

printer.close()