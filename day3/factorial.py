def factorialIterative(n):
    if(n == 0):
        return 1
    
    fact = 1
    for i in range (1, n + 1):
        fact *= i
        
    return fact

def factorialRecursive(n):
    if (n == 0):
        return 1
    
    if(n == 1):
        return 1
    else:
        return n * factorialRecursive(n - 1)
    
n = int(input("Enter a no.: "))
res1 = factorialIterative(n)
res2 = factorialRecursive(n)

print(f"Factorial of {n} by Iterative method = {res1}")
print(f"Factorial of {n} by Recursive method = {res2}")