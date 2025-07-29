a = int(input("Enter value of a:\n"))
b = int(input("Enter value of b:\n"))
c = int(input("Enter value of c:\n"))

D = b ** 2.0 - (4.0 * a * c)

if(abs(D) <= 1.00e-5):
    print("Roots are real & identical")
    x = y = -b / (2.0 * a)
    print("1st Root =", x)
    print("2nd Root =", y)
elif(D > 0):
    print("Roots are real & distinct")
    x = (-b + (b ** 2.0 - (4.0 * a * c)) ** 0.5) / (2.0 * a)
    y = (-b - (b ** 2.0 - (4.0 * a * c)) ** 0.5) / (2.0 * a)
    print("1st Root =", x)
    print("2nd Root =", y)
else:
    print("Roots are imaginary")
    real = -b / (2.0 * a)
    img = (abs(D) ** 0.5) / (2.0 * a)
    print("1st Root =", real, "+", img, "i")
    print("2nd Root =", real, "-", img, "i")