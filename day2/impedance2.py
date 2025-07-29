R = int(input("Enter value of Resistor:\n"))
L = int(input("Enter value of Inductor:\n"))
C = int(input("Enter value of Capacitor:\n"))

f = fres = 0.1
omega = 2 * 3.141519 * f
Zmin = (R ** 2.0 + ((omega * L) - (1.0 / (omega * C))) ** 2.0) ** 0.5

while(f < 0.5):
    omega = 2 * 3.141519 * f
    Z = (R ** 2.0 + ((omega * L) - (1.0 / (omega * C))) ** 2.0) ** 0.5
    if(Z < Zmin):
        Zmin = Z
        fres = f
    
    f += 0.05
    
print("Impedance =", Zmin)
print("Resonance frequency =", fres)