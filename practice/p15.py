import math

class RegTooLow(Exception):
    pass

class RegTooHigh(Exception):
    pass

def find_n(n):
    res = math.ceil(math.log2(n))
    return res

def check_range(n):
    if n < 1:
        raise RegTooLow("Too less reg")
    elif n > 255:
        raise RegTooHigh("Too many reg")
    else:
        return find_n(n)

while True:
    try:
        n = int(input("Enter no. of reg.: "))
        res = check_range(n)
        print("No. of CPU bits:", res)
        
        break
    except ValueError as e:
        print(e)
    except RegTooHigh as e:
        print(e)
    except RegTooLow as e:
        print(e)