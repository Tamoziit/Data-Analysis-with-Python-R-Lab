def check_triangle(x = 3, y = 3, z = 3):
    x = int(x)
    y = int(y)
    z = int(z)
    
    if x == 0 or y ==0 or z == 0:
        print("Not a triangle")
        return
    elif (x + y <= z) or (y + z <= x) or (z + x <= y):
        print("Not a triangle")
        return
    elif x == y and y == z:
        print("Equilaterial triangle")
    elif x == y or y == z or x == z:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
    
    s = (x + y + z) / 2.0
    ar = (s * (s - x) * (s - y) * (s - z)) ** 0.5
    print("Area =", ar)

x = input("Enter side x (default 3): ") or 3
y = input("Enter side y (default 3): ") or 3
z = input("Enter side z (default 3): ") or 3

check_triangle(x, y, z)