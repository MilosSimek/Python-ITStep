with open("slova.txt") as f1, open("pokus2.txt", "w") as f2:
    data = f1.readlines()
    data_reverse = data[::-1]
    for item in data_reverse:
        f2.write(item.rstrip("\n")+ "\n")
