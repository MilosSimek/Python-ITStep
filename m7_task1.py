with open("slova.txt") as f1, open("pokus1.txt", "w") as f2:
    for line in f1:
        if len(line) > 7:
            f2.write(line)