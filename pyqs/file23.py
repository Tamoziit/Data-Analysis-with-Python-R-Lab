def write_even_numbers(arr):
    f = open("abc.txt", "w")
    
    for num in arr:
        if num % 2 == 0:
            f.write(str(num) + "\n")
            
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
write_even_numbers(arr)
print("Written to file")