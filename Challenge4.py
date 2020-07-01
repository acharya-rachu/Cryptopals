# Import Functions from Challenge3 code
from Challenge3 import frequency_calculator, decryption_function 

# Function that sorts two lists based on list1 in  descending order
def cross_sort(list1, list2):
    zipped_list = sorted(zip(list1, list2), key = lambda x:x[0], reverse = True)
    return zipped_list[0]

# Initialize Lists
best_scores = []
best_keys = []
all_lines = []

# Open file 4.txt in reading mode
text_file = open("4.txt", 'r')

# Iterate over every line and try and decrypt it
for line in text_file.readlines():
    # Remove \n so that each line could be purely hexadecimal value
    line = line.strip('\n')
    all_lines.append(line)
    
    # Convert each hexadecimal line to corresponding byte object
    cipher_bytes = bytes.fromhex(line)
    
    # Initialize lists to store scores for all possible keys
    key_scores = []
    keys = []
   
    # For a given line, decrypt it with all possible keys
    for i in range(0, 128):
        decrypted_text = decryption_function(cipher_bytes, i)
        key_scores.append(frequency_calculator(decrypted_text))
        keys.append(chr(i))
    
    # Store the key with the highest score
    top_key_score, key = cross_sort(key_scores, keys)
    best_scores.append(top_key_score)
    best_keys.append(key)

# Store highest score and key from all the highest-scoring decryption
top_score, top_key = cross_sort(best_scores, best_keys)

# Find the line corresponding to highest score and decrypt 
position = best_scores.index(top_score)
cipher_line = all_lines[position]
cipher_bytes = bytes.fromhex(cipher_line)
print(cipher_bytes)
plain_text = decryption_function(cipher_bytes, ord(top_key))

print(plain_text)