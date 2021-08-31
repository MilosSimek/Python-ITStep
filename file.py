import os
print(os.getcwd())
#os.chdir("Python_code")


with open("slova.txt", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
    print("posledni prikaz uvnitr with")


# with = contect management, zav5e soubor za nás

seznam = [55, 22, 44, 66]

with open("cisla.txt", "w") as f2:
    for cislo in seznam:
        f2.write(str(cislo))

with open("slova.txt", "a") as f2:
    for cislo in seznam:
        f2.write("\n" + str(cislo))


with open("slova.txt") as f1, open("pokus.txt", "w") as f2:
    for line in f1:
        f2.write(line)