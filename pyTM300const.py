#
# ---------- CONSTANTS FOR pyTM300 ----------
#

# Print commands
#
LF = b'\x0A' # Print and line feed [p. 72]
CR = b'\x0D' # Print and carriage return [p. 78]
ESC_J = b'\x1B\x4A' # Print and feed paper [p. 82]
ESC_d = b'\x1B\x64' # Print and feed n lines [p. 88]

# Line spacing commands
#
ESC_2 = b'\x1B\x32' # Select default line spacing [p. 95]
ESC_3 = b'\x1B\x33' # Set line spacing [p. 97]

# Character commands
#
ESC_SP = b'\x1B\x20' # Set right-side character spacing [p. 103]
ESC_em = b'\x1B\x21' # Select print mode(s) [p. 106] {was ESC-!}
ESC_pc = b'\x1B\x25' # Select/cancel user-defined character set [p. 112] {was ESC-%}
ESC_nd = b'\x1B\x26' # Define user-defined characters [p. 113] {was ESC-&}
ESC_hy = b'\x1B\x2D' # Turn underline mode on/off [p. 118] {was ESC--}
ESC_E = b'\x1B\x45' # Turn emphasized mode on/off [p. 122]
ESC_G = b'\x1B\x47' # Turn double-strike mode on/off [p. 123]
ESC_R = b'\x1B\x52' # Select an international character set [p. 128]
ESC_r = b'\x1B\x72' # Select print color [p. 133]
ESC_t = b'\x1B\x74' # Select character code table [p. 135]
ESC_cb = b'\x1B\x7B' # Turn upside-down print mode on/off [p. 139] {was ESC-{}

# Panel button commands
#
ESC_c_5 = b'\x1B\x63\x35' # Enable/disable panel buttons [p. 156]

# Paper sensor commands
#
ESC_c_3 = b'\x1B\x63\x33' # Select paper sensor(s) to output paper end signals [p. 161]
ESC_c_4 = b'\x1B\x63\x34' # Select paper sensor(S) to stop printing [p. 163]

# Print position commands
#
HT = b'\x09' # Horizontal tab [p. 168]
ESC_D = b'\x1B\x44' # Set horizontal tab positions [p. 171]

# Bit-image commands
#
ESC_st = b'\x1B\x2A' # Select bit-image mode [p. 195] {was ESC-*}

# Status commands
#
ESC_u = b'\x1B\x75' # Transmit peripheral status [p. 313]
ESC_v = b'\x1B\x76' # Transmit paper sensor status [p. 314]

# Mechanism control commands
#
ESC_lt = b'\x1B\x3C' # Return home [p. 367] {was ESC-<}
ESC_U = b'\x1B\x55' # Turn unidirectional print mode on/off [p. 368]
ESC_i = b'\x1B\x69' # Partial cut (one point left uncut) [p. 369]
ESC_m = b'\x1B\x6D' # Partial cut (three points left uncut) [p. 370]

# Miscellaneous commands
#
ESC_at = b'\x1B\x40' # Initialize printer [p. 410] {was ESC-@}
ESC_p = b'\x1B\x70' # Generate pulse [p. 416] {drawer}
GS_E = b'\x1D\x45' # Select print head control method [p. 454]

# Kanji commands
#
FS_hy = b'\x1C\x21' # Select print mode(s) for Kanji characters [p. 487] {was FS-!}
FS_nd = b'\x1C\x26' # Select Kanji character mode [p. 490] {was FS-&}
FS_hy = b'\x1C\x2D' # Turn underline mode on/off for Kanji characters [p. 495] {was FS--}
FS_fs = b'\x1C\x2E' # Cancel Kanji character mode [p. 497] {was FS-.}
FS_2 = b'\x1C\x32' # Define user-defined Kanji characters [p. 499]
FS_C = b'\x1C\x43' # Select Kanji character code system [p. 503]
FS_S = b'\x1C\x53' # Set Kanji character spacing [p. 505]
FS_W = b'\x1C\x57' # Turn quadruple-size mode on/off for Kanji characters [p. 507]

# The vertical motion unit is 1/144 inch(0.5 dots) and the line height is 1/6 inch(12 dots)
