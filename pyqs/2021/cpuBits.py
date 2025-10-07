import math

class InsuffReg(Exception):
    pass

class MinReg(Exception):
    pass

def find_n(n):
    res = math.ceil(math.log2(n))
    return res

def check_range(n):
    if n > 255:
        raise InsuffReg("Too high")
    elif n < 1:
        raise MinReg("Too Low")
    else:
        return find_n(n)
    
while(True):
    try:
        reg = int(input("Enter no. of reg.: "))
        res = check_range(reg)
        print("No. of bits:", res)
        break
    except ValueError as e:
        print("Enter integer")
    except InsuffReg as e:
        print(e)
    except MinReg as e:
        print(e)
    except Exception as e:
        print("Unknown Error:", e)