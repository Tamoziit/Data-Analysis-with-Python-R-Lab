import sys

if len(sys.argv) != 2:
    print("Usage: p10.py <num>")
    sys.exit(1)

num = int(sys.argv[1])
sum = 0

while num > 0:
    d = num % 10
    sum += d
    num //= 10

print(sum)