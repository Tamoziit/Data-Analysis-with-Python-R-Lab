source = input("Enter source file: ")
dest = input("Enter destination file: ")

try:
    f1 = open(source, "r")
    f2 = open(dest, "w")
    
    for line in f1:
        f2.write(line)
        
    print("File copied successfully!")
    f1.close()
    f2.close()
except Exception as e:
    print(e)