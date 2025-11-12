try:
    fh = open("test.txt", "r")
    fh2 = open("dest.txt", "w")
    
    lines = fh.readlines()
    for line in lines:
        fh2.write(line)
    
    fh.close()
    fh2.close()
except FileNotFoundError as e:
    print(e)