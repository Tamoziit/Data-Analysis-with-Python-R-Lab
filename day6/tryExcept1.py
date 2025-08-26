try:
    num1, num2 = eval(input("Enter 2 numbers in the format (n1, n2): "))
    
    if num2 == 0:
        raise ZeroDivisionError("Division by 0 not possible")
    
    res = num1 / num2
    print("Result =", res)
except ZeroDivisionError as e:
    print(e)
except SyntaxError as e:
    print("Syntax Error:", e)
except Exception as e:
    print("Input is not in valid format")