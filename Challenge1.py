# Import Dependancies
import base64

# Ascii string representing some Hex Value
hex_value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Conversion of Hex value string to bytes 
hex_bytes = bytes.fromhex(hex_value)

# Conversion of bytes to base64 bytes
base64_value = base64.b64encode(hex_bytes)

print(base64_value)












