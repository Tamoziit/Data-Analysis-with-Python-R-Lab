try:
    num1, num2 = eval(input("Enter: "))
    
    if num2 == 0:
        raise ZeroDivisionError("Division by 0 not possible")
    else:
        res = num1 / num2
        print("Result:", res)
except ZeroDivisionError as e:
    print(e)
except SyntaxError as e:
    print(e)
except Exception as e:
    print("Input is not in proper format")