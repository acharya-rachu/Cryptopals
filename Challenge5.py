# Cryptopals Set1 Crehallenge 5

# Repeatinf XOR encryption function 
def repeating_xor(plain_text, key):
    key_len = len(key)
    text_len = len(plain_text)
    encrypted_line = ''

    # List comprehension to create list of indices that point to the beginning of each block 
    block_indices = [i for i in range(text_len) if i % key_len == 0]

    # Iterate through Each blocks
    for i in block_indices:
        # Iterate through each char of block
        for j in range(key_len): 
            if(i + j < text_len):
                encrypted_line = encrypted_line + (chr(ord(plain_text[i + j]) ^ ord(key[j])))
                    
    # ASCII character encoded to hex 
    hex_encoded_cipher = bytes(encrypted_line, 'ascii').hex()

    return hex_encoded_cipher

def main():
    plain_text = '''Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal'''
    key = "ICE"
    cipher_text = repeating_xor(plain_text, key)
    print(cipher_text)

if __name__ == "__main__":
    main()
