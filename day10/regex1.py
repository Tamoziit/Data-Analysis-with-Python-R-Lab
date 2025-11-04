import re
str = "Hello we are doing python programming Regular Expression @2025hello;ho"

print(re.findall(r'[b-s]', str), "\n")

print(re.findall(r'[^b-s]', str), "\n")

print(re.findall(r'[abc]', str), "\n")

print(re.findall(r'[^abc]', str), "\n")

print(re.findall(r'[0-9]', str), "\n")

print(re.findall(r'[^0-9]', str), "\n")

print(re.findall(r'a.e', str), "\n")

print(re.findall('a..e', str), "\n")

print(re.findall(r'he*o', str), "\n")