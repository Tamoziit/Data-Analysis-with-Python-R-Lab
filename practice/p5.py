pizza = int(input("Enter no. of pizzas: "))
puffs = int(input("Enter no. of puffs: "))
drinks = int(input("Enter no. of cold drinks: "))

x = pizza * 100
y = puffs * 20
z = drinks * 10

print("___ Bill Details ___")
print("No. of Pizzas:", pizza)
print("Price =", x)
print("No. of Puffs:", puffs)
print("Price =", y)
print("No. of Cold Drinks:", drinks)
print("Price =", z)
print("Total =", x + y + z)