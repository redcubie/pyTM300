#
# ---------- Main pyTM300 library ---------
#

import pyTM300const as const # Import constants as const
import serial # Import (py)serial

ser = serial.Serial() # Make Serial object

def open(port):
    ser.port = port # Set serial port
    ser.xonxoff = True # Set XON/XOFF flow control
    ser.open() # Open serial port

def close():
    ser.close() # Close serial port

def initialize():
    ser.write(const.ESC_at) # Send initialize command

def home():
    ser.write(const.ESC_lt) # Send return home command

def unidirectional(data):
    if(data):
        value = b'\x01' # If true, set unidirectional print mode to on
    else:
        value = b'\x00' # Otherwise set uniderictional print mode to off
    ser.write(const.ESC_U+value) # Send command

def panel_buttons(data):
    if(data):
        value = b'\x00' # If true, enable panel buttons
    else:
        value = b'\x01' # Otherwise disable panel buttons
    ser.write(const.ESC_c_5+value) # Send command

def upside_down(data):
    if(data):
        value = b'\x01' # If true, enable upside-down print mode
    else:
        value = b'\x00' # Otherwise disable upside-down print mode
    ser.write(const.ESC_cb+value) # Send command

def double_strike(data):
    if(data):
        value = b'\x01' # If true, enable double-strike mode
    else:
        value = b'\x00' # Otherwise disable double-srike mode
    ser.write(const.ESC_G+value) # Send command

def emphasized(data):
    if(data):
        value = b'\x01' # If true, enable emphasized mode
    else:
        value = b'\x00' # Otherwise disable emphasized mode
    ser.write(const.ESC_E+value) # Send command

def underline(data):
    if(data):
        value = b'\x01' # If true, enable underline mode
    else:
        value = b'\x00' # Otherwise disable underline mode
    ser.write(const.ESC_hy+value) # Send command

def cut(data=0):
    if(data):
        ser.write(const.ESC_i) # If true, cut with 1 point uncut
    else:
        ser.write(const.ESC_m) # Otherwise cut with 3 points uncut (default)

def status():
    ser.write(const.ESC_u) # Sends command to retrieve status
    read = ser.read() # Reads reply
    return(ord(read) & ord(b'\x01')) # Does bitwise operation to determine if the drawer is open
