def gcdIterative(n1, n2):
    min = n1 if (n1 < n2) else n2
    gcd = 1
    
    for i in range(2, min + 1):
        if(n1 % i == 0 and n2 % i == 0):
            gcd = i
            
    return gcd

def gcdRecursive(n1, n2):
    if(n1 % n2 == 0):
        return n2
    else:
        return gcdRecursive(n2, n1 % n2)
    
n1 = int(input("Enter 1st no.: "))
n2 = int(input("Enter 2nd no.: "))
gcd1 = gcdIterative(n1, n2)
gcd2 = gcdRecursive(n1, n2)

print(f"GCD of {n1} & {n2} by Iterative method = {gcd1}")
print(f"GCD of {n1} & {n2} by Recursive method = {gcd2}")