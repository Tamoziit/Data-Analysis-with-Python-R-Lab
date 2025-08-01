def fibonacciIterative(start, end):
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
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciRecursive(start, end):
    return [fibonacci(i) for i in range(start, end + 1)]

start = int(input("Enter start pos: "))
end = int(input("Enter end pos: "))

if(start == 0 or end == 0 or start > end):
    print("Invalid Position")
else:
    res1 = fibonacciIterative(start - 1, end - 1)
    res2 = fibonacciRecursive(start - 1, end - 1)

    print(f"By Iterative method: {res1}")
    print(f"By Recursive method: {res2}")