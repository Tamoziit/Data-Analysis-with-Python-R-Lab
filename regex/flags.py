import re

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.IGNORECASE) # ignoring case sensitivity
match = pattern.search(sentence)
print(match)