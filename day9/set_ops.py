import random

s1 = set()
s2 = set()

n1 = int(input("Enter size of set 1: "))
for i in range(n1):
    ele = random.randint(1, 10)
    s1.add(ele)
    
n2 = int(input("Enter size of set 2: "))
for i in range(n2):
    ele = random.randint(1, 10)
    s2.add(ele)
    
print("Set 1:", s1, "\nSet 2:", s2)

while(1):
    choice = int(input("Enter choice:\n 1. Union\n 2. Intersection\n 3. Set Difference\n 4. Symmetric Difference\n 5. Exit\n"))
    if (choice == 1):
        print("Union:", s1 | s2)
    elif (choice == 2):
        print("Intersection:", s1 & s2)
    elif (choice == 3):
        print("Difference:\n A - B =", s1 - s2, "\n B - A =", s2 - s1)
    elif (choice == 4):
        print("Symmetric Difference:", s1 ^ s2)
    elif (choice == 5):
        print("EOP")
        break
    else:
        print("Wrong Choice!")