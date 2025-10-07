with open("out-data.txt", "w") as f1:
    with open("in-data.txt", "r") as f2:
        for i, line in enumerate(f2, start = 1):
            if i % 2 != 0:
                f1.write(line)