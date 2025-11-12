with open("test.txt", "r") as fh:
    lines = fh.readlines()
    print("No. of lines:", lines)
    
    fh.seek(0)
    count = 0
    for line in lines:
        count += len(line)
    
    print("No. of characters:", count)