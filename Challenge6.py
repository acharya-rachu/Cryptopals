# Import Dependancies 
import base64
from itertools import zip_longest
from Challenge3 import decryption_function, frequency_calculator
from Challenge5 import repeating_xor

# Function that returns list of ascii values for all char in plain_text
def get_string_ascii(plain_text):
    string_ascii = []
    for char in plain_text:
        string_ascii.append(ord(char))
    return string_ascii

# Function that normalizes list for xor-ing
def pad(list1, list2):
    len1 =len(list1)  
    len2 = len(list2)
    diff_len = len1 - len2
    padding = [0 for i in range(abs(diff_len))]
    if(diff_len < 0 ):
        list1.extend(padding)
    elif(diff_len > 0):
        list2.extend(padding)
    return list1, list2

# Fucntion to calculate the hamming distance
def hamming_distance(string1, string2):
    ascii_list1, ascii_list2 = pad(get_string_ascii(string1), get_string_ascii(string2))
    ascii_difference = []
    
    # Performing xor between two int ascii values
    for i in range(len(ascii_list1)):
        ascii_difference.append(ascii_list1[i] ^ ascii_list2[i])

    distance = 0
    for difference in ascii_difference:
        weight = 0
        # Calculate weight until difference = 0
        while(difference):
            # For every right shift if last bit is 1, increment weight
            if difference & 1 == 1:
                weight += 1 
            difference = difference >> 1
        
        # Add weight of individual differences 
        distance += weight
    return distance

# Function to sort list1 and list2 in ascending or descending order based on reverse
def cross_sort(list1, list2, reverse):
    zipped_list = sorted(zip(list1, list2), key = lambda x:x[0], reverse = reverse)
    return zipped_list[0] 

# Function that returns the optimum keysize for a cipher_text
def calculate_keysize(lower_limit, upper_limit, cipher_text):
    mean_distances = []
    size = []
    for key_size in range(lower_limit, upper_limit + 1):
        
        size.append(key_size)
        all_distances = []
        text_blocks = [cipher_text[i: i + key_size] for i in range(len(cipher_text)) if i % key_size == 0]
       
        for i in range(len(text_blocks)): 
            if i + 1 < len(text_blocks):
                all_distances.append(hamming_distance(text_blocks[i], text_blocks[i + 1]))

        # Normalized mean
        mean = sum(all_distances) / (len(all_distances) * key_size)
        mean_distances.append(round(mean, 5))
       
    # Sort in ascending order and get top result
    distance, optimum_size = cross_sort(mean_distances, size, False)
    
    return optimum_size

# Funtion that returns list of strings encrypted by same key 
def transpose_text(cipher_text, key_size):
    text_blocks = [cipher_text[i: i + key_size] for i in range(len(cipher_text)) if i % key_size == 0]
    trans_text_temp = list(map(list, zip_longest(*text_blocks, fillvalue= '\0')))
    trans_text_blocks = []

    for block in trans_text_temp:
        trans_text_blocks.append("".join(block))
    return trans_text_blocks

# Main Function     
def main():  

    with open("6.txt", 'r') as text_file:
        b64_text = ""
        for line in text_file.readlines():
            b64_text += "" + line.rstrip('\n')
    
    # Pre-processing encoded text 
    base64_bytes = b64_text.encode('ascii')
    ascii_bytes = base64.b64decode(base64_bytes)
    cipher_text = ascii_bytes.decode('ascii')
    
    # Get optimum key_size for the cipher_text
    opt_key_size = calculate_keysize(2, 40, cipher_text)
    
    # List of Strings encrypted by same keys
    text_list = transpose_text(cipher_text, opt_key_size)
   
    final_key = ""

    # Perfrom Frequency Analysis on string to guess corrsponding key
    for line in text_list:
        cipher_bytes = bytes(line, 'ascii')
        
        # Initialize lists to store scores for all possible keys
        key_scores = []
        keys = []
    
        # For a given line, decrypt it with all possible keys
        for i in range(0, 128):
            decrypted_text = decryption_function(cipher_bytes, i)
            key_scores.append(frequency_calculator(decrypted_text))
            keys.append(chr(i))
        
        # Store the key with the highest score
        top_key_score, key = cross_sort(key_scores, keys, True)
        
        # Combine individual keys to string
        final_key += key

    print("Key Cracked -\n", final_key, sep="")   
    # Extract Plain Text:
    plain_text = repeating_xor(ascii_bytes, final_key)
    print("Decrypted Text -\n", plain_text, sep="")
    
if __name__ == "__main__":
    main()
