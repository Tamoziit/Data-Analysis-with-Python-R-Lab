def reverse_list(in_lst):
    out_lst = []
    for i in range(len(in_lst) - 1, -1, -1):
        out_lst.append(in_lst[i])
        
    return out_lst

in_lst = [1, 2, 3, 4, 5]
print("Original:", in_lst)
print("Reverse:", reverse_list(in_lst))