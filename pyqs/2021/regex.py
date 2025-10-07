import re

s = input("Enter a no.: ")

pattern = r'^[+-]?\d+(\.\d+)?$'

if re.match(pattern, s):
    num = float(s)
    print("Square:", num ** 2)
else:
    print("Invalid No.")