import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') 
matches = pattern.finditer(emails) 
for match in matches:
    print(match)
    
# [a-zA-Z0-9.-]+ --> any alphanumeric character & . or -, atleast one
# @ --> literal "@"
# [a-zA-Z-]+ --> atleast one alphabet or -
# \. --> "."
# (com|edu|net) --> any one of com, edu or net