import sys

if len(sys.argv) != 3:
    print("Usage: python p1.py <num1> <num2>")
    sys.exit(1)
    
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print("Sum =", num1 + num2)