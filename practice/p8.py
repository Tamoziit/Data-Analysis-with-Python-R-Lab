def gcd(n1, n2):
    if(n1 % n2 == 0):
        return n2
    else:
        return gcd(n2, n1 % n2)

def gcdN(arr):
    if len(arr) == 0:
        print("Empty List")
        return
    
    if len(arr) < 2:
        print("Atleast 2 elements required")
        return
    
    gcdRes = arr[0]
    for i in range(1, len(arr)):
        gcdRes = gcd(gcdRes, arr[i])
    
    return gcdRes

arr = eval(input("Enter nos: "))
print(arr)
print("GCD =", gcdN(arr))