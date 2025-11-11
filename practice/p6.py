a = int(input("Enter coeff. of a: "))
b = int(input("Enter coeff. of b: "))
c = int(input("Enter coeff. of c: "))

if a == 0:
    print("Equation is linear")
    x = -c / b
    print("Root =", x)
else:
    D = b ** 2 - (4.0 * a *c)
    if (abs(D) <= 1.00e-5):
        print("Roots are real & equal")
        x = -b / (2.0 * a)
        print("x = y =", x)
    elif D > 0:
        print("Roots are real & distinct")
        x = (-b + D ** 0.5) / (2.0 * a)
        y = (-b - D ** 0.5) / (2.0 * a)
        print("x =", x)
        print("y =", y)
    else:
        print("Roots are imaginary")
        real = -b / (2.0 * a)
        img = ((-D) ** 0.5) / (2.0 * a)
        print(f"x = {real} + {img}i")
        print(f"y = {real} - {img}i")