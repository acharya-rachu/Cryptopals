# Brute Force Decryption Using Frequency Analysis

# Fuction that Returns Weighted Score of a Decrypted Text
def frequency_calculator(decrypted_text):
    # Character:Occurrence Pair
    metric = {'E':0.11162 , 'T':0.09356, 'A':0.08497,'I':0.0754,'O':0.07507,' ':0.17,'S':0.0652, 'H':0.06094,'R':0.0758,  'D':0.04253, 'L':0.04025, 'U':0.02578 } 
    score = 0.0
    for char, occurrence in metric.items() :
        # Weighted Score = Sum of  char_count * occurrence in english language 
        score =round( score + decrypted_text.upper().count(char) * occurrence, 5)
    return score    

# Decryption Function 
def decryption_function(cipher_bytes, key):
    decrypted_string = ''
    
    for i in range(len(cipher_bytes)):
        decrypted_string = decrypted_string + chr(cipher_bytes[i] ^ key)
 
    return decrypted_string

def main():
    # Cipher Text
    cipher_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736" 
    cipher_bytes = bytes.fromhex(cipher_hex)
    score = []
    keys = []

    # Iterate through All possible ASCII Value Keys
    for i in range(0, 128):
        decrypted_text = decryption_function(cipher_bytes, i)
        score.append(frequency_calculator(decrypted_text))
        keys.append(chr(i))

    # Zip score and corresponding key to sort descendinly
    zipped_list = sorted(zip(score, keys), key = lambda x:x[0], reverse = True)   

    # Key, score tuple with the hightest score
    key_score, key = zipped_list[0]

    # Final Decryption of the Cipher Text 
    plain_text = decryption_function(cipher_bytes, ord(key))
    print(plain_text)

if __name__ == "__main__":
    main()