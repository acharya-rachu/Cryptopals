import base64

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


def cross_sort(list1, list2):
    zipped_list = sorted(zip(list1, list2), key = lambda x:x[0], reverse = False)
    return zipped_list[0] 

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
       
   # print(mean_distances)

    distance, optimum_size = cross_sort(mean_distances, size)
    
    return optimum_size

    
def main():            
    distance = hamming_distance("this is a test", "wokka wokka!!!")
    print(distance)

    text_file = open("6.txt", 'r')
    b64_text = ""
    for line in text_file.readlines():
        b64_text += line.rstrip("\n")
    text_file.close()

    base64_bytes = b64_text.encode('ascii')
    ascii_bytes = base64.b64decode(base64_bytes)
    cipher_text = ascii_bytes.decode('ascii')

    key_size = calculate_keysize(2, 40, cipher_text)

    print(key_size)

if __name__ == "__main__":
    main()
