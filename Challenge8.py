# Challenge 8.py

lines = []
with open("8.txt", "r") as text_file:
    for line in text_file.readlines():
        lines.append(line.rstrip('\n'))
        

line_number = 0
repeated_block = None

for line in lines:
    bytes_block = [line[i : i + 32] for i in range(len(line)) if i % 32 == 0]
    for j in range(len(bytes_block)):
        for k in range(len(bytes_block)):
            if (k != j and  bytes_block[k]== bytes_block[j]):
                repeated_block = bytes_block[k]
                line_number = lines.index(line) + 1
                break; 

print(repeated_block)
print(line_number)

verification = False
if repeated_block in lines[line_number - 1]:
    verification = True

print(f"Verification Status: {verification}")