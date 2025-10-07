import re

with open("data.txt", "r") as f:
    contents = f.read()
    
    pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}') # 123-456-7890, 123.456.7890 -> [] = character set --> matches with only the characters inside the set
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)