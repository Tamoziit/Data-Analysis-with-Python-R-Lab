fh = open("./file1.txt", "r")

lines = fh.readlines()
print("No. of lines =", len(lines))

fh.seek(0)
count = 0
for line in lines:
    count += len(line)
    
print("No. of characters =", count)