import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc') # r = raw text (without any formatting or escape sequences) --> searching for "abc" text patterns
matches = pattern.finditer(text_to_search) # finding all matches of the pattern
for match in matches:
    print(match)
    
# pattern = re.compile(r'.') # . = matches with everything (ie all patterns are allowed, except new line)
# matches = pattern.finditer(text_to_search) 
# for match in matches:
#     print(match)
    
pattern = re.compile(r'\.') # \. = actual fullstop (.)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\d') # digits (0-9)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'D') # NOT a digit
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\w') # alphanumeric & underscore (0-9, a--z, A-Z, _)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\W') # NOT alphanumeric & underscore (0-9, a--z, A-Z, _)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\s') # whitespaces /(tabs, newlines, etc.)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\S') # NOT whitespaces
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
# Anchors
pattern = re.compile(r'\bHa') # \b = Word boundary (newline, space etc.) --> we are searching for "Ha" that appears after word boundaries
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\BHa') # "Ha"s without a wordboundary (eg: in the middle of a word)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'^Start') # searches for "Start" which is at the beginning (^) of a string
matches = pattern.finditer(sentence) 
for match in matches:
    print(match)
    
pattern = re.compile(r'end$') # searches for "end" which is at the end ($) of a string
matches = pattern.finditer(sentence) 
for match in matches:
    print(match)
    
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # matches phone nos like 234.689.9023, 889-903-9993, etc (. is any charac in between)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'[89]00[.-]\d{3}[.-]\d{4}') # starts with 800 or 900
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'[1-5]') # matches digits b/w 1 & 5
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'[a-zA-Z]') # matches letters b/w a-z & A-Z (all alphabets)
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'[^a-zA-Z]') # matches everything EXCEPT alphabets
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'[^b]at') # all strings with "at" except bat
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # Mr (optional .) Uppercase letter, then 0 or more words (eg. Mr. T(0 words after uppercase T))
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # Mr/Ms/Mrs [specified by group --> ()] (optional .) (space \s) Uppercase letter, then 0 or more words (eg. Mr. T(0 words after uppercase T))
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search) # prints out the groups of the pattern from the matches (iff groups present) (not as object as in finditer)
for match in matches:
    print(match)
    
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}') 
matches = pattern.findall(text_to_search) # if no group present --> prints the matches simply (not as object as in finditer)
for match in matches:
    print(match)
    
pattern = re.compile(r'Start')
match = pattern.match(sentence) # matches the pattern only at the beginning of the string
print(match)

pattern = re.compile(r'sentence')
match = pattern.search(sentence) # searches for the match in the entire string
print(match)