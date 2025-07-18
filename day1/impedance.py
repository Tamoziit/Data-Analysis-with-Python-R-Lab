R = int(input("Enter value of Resistor:\n"))
L = int(input("Enter value of Inductor:\n"))
C = int(input("Enter value of Capacitor:\n"))
f = float(input("Enter frequency:\n"))

# Impedance for freq 'f' Hz
omega = 2.0 * 3.141519 * f
Z = (R ** 2.0 + ((omega * L) - (1.0 / (omega * C))) ** 2.0) ** 0.5
print("Impedance =", Z)

# Resonant Frequency
res = 1.0 / (2.0 * 3.141519 * (L * C) ** 0.5)
print("Resonant Frequency =", res)

# Impedance for Resonant Frequency
omegaRes = 2.0 * 3.141519 * res
ZRes = (R ** 2.0 + ((omegaRes * L) - (1.0 / (omegaRes * C))) ** 2.0) ** 0.5
print("Resonant Impedance =", ZRes)