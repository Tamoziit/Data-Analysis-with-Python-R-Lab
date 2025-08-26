class TooHot(Exception):
    pass

class TooCold(Exception):
    pass

try:
    temp = float(input("Enter a temp.: "))
    
    if temp >= 20 and temp <= 40:
        print("Temperature =", temp)
    elif temp > 40:
        raise TooHot("Temp. too high")
    elif temp < 20:
        raise TooCold("Temp. too less")
except TooHot as e:
    print(e)
except TooCold as e:
    print(e)