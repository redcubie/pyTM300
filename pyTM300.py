#
# ---------- Main pyTM300 library ---------
#

import pyTM300const as const # Import constants as const
import serial # Import (py)serial

class TM300(serial.Serial):
    def __init__(self, port: str | None = None, baudrate: int = 9600, bytesize: int = 8, parity: str = "N", stopbits: float = 1, timeout: float | None = None, xonxoff: bool = False, rtscts: bool = False, write_timeout: float | None = None, dsrdtr: bool = False, inter_byte_timeout: float | None = None, exclusive: float | None = None) -> None:
        xonxoff = True
        super().__init__(port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, write_timeout, dsrdtr, inter_byte_timeout, exclusive)
    # def open(self, port):
    #     self.port = port # Set serial port
    #     self.xonxoff = True # Set XON/XOFF flow control
    #     self.open() # Open serial port

    # def close(self):
    #     self.close() # Close serial port

    def initialize(self):
        self.write(const.ESC_at) # Send initialize command

    def home(self):
        self.write(const.ESC_lt) # Send return home command

    def unidirectional(self, data):
        if(data):
            value = b'\x01' # If true, set unidirectional print mode to on
        else:
            value = b'\x00' # Otherwise set uniderictional print mode to off
        self.write(const.ESC_U+value) # Send command

    def panel_buttons(self, data):
        if(data):
            value = b'\x00' # If true, enable panel buttons
        else:
            value = b'\x01' # Otherwise disable panel buttons
        self.write(const.ESC_c_5+value) # Send command

    def upside_down(self, data):
        if(data):
            value = b'\x01' # If true, enable upside-down print mode
        else:
            value = b'\x00' # Otherwise disable upside-down print mode
        self.write(const.ESC_cb+value) # Send command

    def double_strike(self, data):
        if(data):
            value = b'\x01' # If true, enable double-strike mode
        else:
            value = b'\x00' # Otherwise disable double-srike mode
        self.write(const.ESC_G+value) # Send command

    def emphasized(self, data):
        if(data):
            value = b'\x01' # If true, enable emphasized mode
        else:
            value = b'\x00' # Otherwise disable emphasized mode
        self.write(const.ESC_E+value) # Send command

    def underline(self, data):
        if(data):
            value = b'\x01' # If true, enable underline mode
        else:
            value = b'\x00' # Otherwise disable underline mode
        self.write(const.ESC_hy+value) # Send command

    def cut(self, data=0):
        if(data):
            self.write(const.ESC_i) # If true, cut with 1 point uncut
        else:
            self.write(const.ESC_m) # Otherwise cut with 3 points uncut (default)

    def status(self):
        self.write(const.ESC_u) # Sends command to retrieve status
        read = self.read() # Reads reply
        return(ord(read) & ord(b'\x01')) # Does bitwise operation to determine if the drawer is open

    def bitmap(self, data, length=0, density=0):
        if length == 0:
            length = len(data)
        if 0 < length < 1023:
            # length_lower = int(length & ord('\xff')).to_bytes()
            # length_higher = int((length & ord('\x03')<<8)>>8).to_bytes()
            
            # self.write(const.ESC_st + bytes(density) + length_lower + length_higher + bytes(data))
            self.write(const.ESC_st + density.to_bytes(1, "little") + length.to_bytes(2, "little") + bytes(data))
        else:
            raise Exception
