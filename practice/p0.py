import random

class NumberTooSmall(Exception):
    pass

try:
    num = random.random()
    print("Generated no:", num)
    
    if num < 0.5:
        raise NumberTooSmall("no. < 0.5")
except NumberTooSmall as e:
    print(e)