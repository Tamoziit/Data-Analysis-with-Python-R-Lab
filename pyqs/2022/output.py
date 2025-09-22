def my_function(n):
    return_value = None
    if n == 0 or n == 1:
        return_value = False
    
    i=2
    while i < n**0.5:
        if n%i==0:
            return_value = False
            break
        i+=1
        return_value = True
        
    return return_value

print(my_function(37))