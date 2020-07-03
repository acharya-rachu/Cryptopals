# Cryptopals Set1 Crehallenge 5
# Repeating XOR encryption function 
def repeating_xor(plain_text_bytes, key):
    key_len = len(key)
    encrypted_line = ''

    # List comprehension to create blocks of bytes 
    block_indices = [i for i in range(len(plain_text_bytes))if i % key_len == 0]

    # Iterate through each blocks of bytes
    for i in block_indices:
        # Iterate through each byte
        for j in range(key_len): 
            if(i + j < len(plain_text_bytes)):
                encrypted_line = encrypted_line + (chr(plain_text_bytes[i + j] ^ ord(key[j])))

    return encrypted_line
    
def main():
    plain_text = '''Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal'''
    key = "ICE"
    plain_text_bytes = bytes(plain_text, 'ascii')
    cipher_text = repeating_xor(plain_text_bytes, key)
    hex_encoded_cipher = bytes(cipher_text, 'ascii').hex()

    print(hex_encoded_cipher)

if __name__ == "__main__":
    main()
