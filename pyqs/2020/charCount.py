s = input("Enter a string: ")

char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
for key in sorted(char_count.keys()):
    print(f"{key}: {char_count[key]}")