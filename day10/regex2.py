import re

s1 = "he, hello, hi, hello25, hellllo, hellllllo"

res = re.findall(r'he\w\w\w?\w?o', s1)
print(res)