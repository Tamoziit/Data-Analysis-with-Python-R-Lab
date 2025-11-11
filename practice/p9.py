def fiboIt(start, end):
    fib = []
    
    for i in range(end + 1):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[start:end + 1]

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fiboRecur(start, end):
    return [fibonacci(i) for i in range(start, end + 1)]

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Fibonacci Iterative =", fiboIt(start - 1, end - 1))
print("Fibonacci Recursive =", fiboRecur(start - 1, end - 1))