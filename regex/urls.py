import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?\w+\.\w+') # all urls
matches = pattern.finditer(urls) 
for match in matches:
    print(match)
    
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') #separating domains & domain names in groups
matches = pattern.finditer(urls) 
for match in matches:
    print(match.group(0)) # whole match
    print(match.group(1)) # optional www.
    print(match.group(2)) # domains (google, youtube, etc [(\w+)])
    print(match.group(3)) # domain names (.com, .gov, etc [(\.\w+)])
    
subbed_urls = pattern.sub(r'\2\3', urls) # substitutes the matches of urls for the pattern by group 2 & 3 of the pattern (back-referencing)
print(subbed_urls)