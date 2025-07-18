# Assuming Real Roots
a = int(input("Enter value of a:\n"))
b = int(input("Enter value of b:\n"))
c = int(input("Enter value of c:\n"))

x = (-b + (b ** 2.0 - (4.0 * a * c)) ** 0.5) / 2.0 * a
y = (-b - (b ** 2.0 - (4.0 * a * c)) ** 0.5) / 2.0 * a
print("1st Root =", x)
print("2nd Root =", y)
