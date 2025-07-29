pizza = int(input("Enter no. of pizzas: "))
puff = int(input("Enter no. of puffs: "))
coldDrinks = int(input("Enter no. of coldDrinks: "))

tp = 100.0 * pizza
tpuff = 20.0 * puff
tcd = 10.0 * coldDrinks

sum = tp + tpuff + tcd

print("____BILL MEMO____\n       ****")
print("Pizzas: ", pizza, "* Rs. 100 = Rs.", tp)
print("Puffs: ", puff, "* Rs. 20 = Rs.", tpuff)
print("Cold Drinks: ", coldDrinks, "* Rs. 10 = Rs.", tcd)
print("______________________________________")
print("Sum = Rs.", sum)
