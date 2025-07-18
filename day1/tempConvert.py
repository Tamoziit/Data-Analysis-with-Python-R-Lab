cel1 = float(input("Enter temp. in Celcius: "))
fahr1 = (9.0 * cel1) / 5.0 + 32.0
print(cel1, "deg. Celcius =", fahr1, "deg. Fahrenheit")

fahr2 = float(input("Enter temp. in Fahrenheit: "))
cel2 = (5.0 / 9.0) * (fahr2 - 32.0)
print(fahr2, "deg. Fahrenheit =", cel2, "deg. Celcius")