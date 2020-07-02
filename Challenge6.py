# Function that returns list of ascii values for all char in plai_text
def get_string_ascii(plain_text):
    string_ascii = []
    for char in plain_text:
        string_ascii.append(ord(char))
    return string_ascii

# Function that normalizes list for xor-ing
def normalize(list1, list2):
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
    ascii_list1, ascii_list2 = normalize(get_string_ascii(string1), get_string_ascii(string2))
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
        
        
        distance += weight
    return distance
             
            

distance = hamming_distance("this is a test", "wokka wokka!!!")
print(distance)
