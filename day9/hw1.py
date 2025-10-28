lst = list(map(int, (x for x in range(0, 20))))
print("List:", lst)

# Separating odd and even position elements
odd_pos = [lst[i] for i in range(0, len(lst), 2)]
even_pos = [lst[i] for i in range(1, len(lst), 2)]
print(odd_pos, even_pos)

if len(even_pos) < 2 or len(odd_pos) < 2:
    print("Not enough elements to find 2nd largest/smallest.")
else:
    even_pos.sort()
    odd_pos.sort()
    
    second_largest_even = even_pos[-2]
    second_smallest_odd = odd_pos[1]
    
    print(second_largest_even, second_smallest_odd)
    total = second_largest_even + second_smallest_odd
    print("Sum =", total)