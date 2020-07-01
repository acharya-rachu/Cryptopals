#Import Dependancies
from sys import exit

# Ascii strings representing HEX Values
hex_value_string1 = "1c0111001f010100061a024b53535009181c"
hex_value_string2 = "686974207468652062756c6c277320657965"

# Convert hex string to integer
hex_value_int1 = int(hex_value_string1, 16)
hex_value_int2= int(hex_value_string2, 16)

# Perform XOR
hex_value_int3 = hex_value_int1 ^ hex_value_int2

# Print hex string without the prefix "Ox"
print(hex(hex_value_int3).strip('0x'))
