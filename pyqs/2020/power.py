def power(x, n = 10):
    if n == 0:
        return 1
    elif n > 0:
        res = 1
        for i in range(n):
            res = res * x
            
        return res
    else:
        res = 1
        for i in range(-n):
            res = res * x
            
        return 1 / res
    
print(power(2))
print(power(3, 4))
print(power(5, 0))
print(power(2, -3))