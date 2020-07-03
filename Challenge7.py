# Import Dependency
import base64
from Crypto.Cipher import AES

# Read base64 encoded contents
b64_text = ""
with open("7.txt", 'r') as text_file:
    for line in text_file.readlines():
        b64_text += line.rstrip('\n')

# Pre-process the cipher_text
base64_bytes = b64_text.encode('ascii')
ascii_bytes = base64.b64decode(base64_bytes)

key = "YELLOW SUBMARINE"

# Decrypt equivalent bytes  
decipher = AES.new(key, AES.MODE_ECB)
decipher_bytes = decipher.decrypt(ascii_bytes)
plain_text = decipher_bytes.decode('ascii')
print(plain_text)