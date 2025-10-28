import random

def unique(numlist):
    uniqueEle = []
    for ele in numlist:
        c = numlist.count(ele)
        if(c == 1):
            uniqueEle.append(ele)
            
    print("Unique Elements:", uniqueEle)
    return

def duplicate(numlist):
    duplicates = {}
    for ele in numlist:
        c = numlist.count(ele)
        if (c >= 2):
            duplicates[ele] = c
            
    print("Duplicate Elements:", duplicates)
    return

def create_unique(numlist):
    unique_lst = []
    for x in numlist:
        if x not in unique_lst:
            unique_lst.append(x)
            
    print("Unique List:", unique_lst)
    return


lst = []
for x in range(20):
    lst.append(random.randint(0, 9))
    
print("Original List:", lst)

unique(lst)
duplicate(lst)
create_unique(lst)