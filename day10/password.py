import re

password = input("Enter a password: ")
count = 0

if len(password) < 8:
    print("Password should be atleast 8 characters long")
else:
    count += 1
    
if re.search(r'[A-Z]', password):
    count += 1
else:
    print("There should be atleast 1 capital letter")
    
if re.search(r'[a-z]', password):
    count += 1
else:
    print("There should be atleast 1 small letter")
    
if re.search(r'[0-9]', password):
    count += 1
else:
    print("There should be atleast 1 digit")
    
if re.search(r'\w', password):
    count += 1
else:
    print("There should be atleast 1 special character")
    
if re.search(r'\s', password):
    print("There should not be any spaces")
else:
    count += 1
    
if count == 6:
    print("Password is valid")
else:
    print("Password is invalid")