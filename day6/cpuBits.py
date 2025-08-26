import math

class InsufficientRegisterError(Exception):
    pass

class MinimumRegisterError(Exception):
    pass

def find_n(n):
    res = math.ceil(math.log2(n))
    return res

def check_range(n):
    if n > 255:
        raise InsufficientRegisterError("Sufficient no. of registers not available")
    elif n < 1:
        raise MinimumRegisterError("Min. 1 Register required")
    else:
        return find_n(n)
    
try:
    reg = int(input("Enter no. of Registers: "))
    res = check_range(reg)
    print("No. of Bits =", res)
except ValueError as e:
    print("Only Integer allowed")
except InsufficientRegisterError as e:
    print(e)
except MinimumRegisterError as e:
    print(e)
except Exception as e:
    print(e)