seconds = int(input("Enter time in seconds: "))

hrs = seconds // 3600
mins = (seconds % 3600) // 60
rem = seconds % 60  

print("Hours:", hrs)
print("Minutes:", mins)
print("Seconds:", rem)