text = "himachala sutanatha nigrishthe charanambhuje"

char_count = {}
for ch in text:
    if ch.isalpha():
        char_count[ch] = char_count.get(ch, 0) + 1
        
for ch in sorted(char_count):
    print(f'{ch}: {char_count[ch]}')