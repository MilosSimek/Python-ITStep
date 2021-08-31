x = int(input("Zadej Cislo 1: \n"))
y = int(input("Zadej cislo 2: \n"))
print("Zvol cilso operace\n", "1 - Scitani\n", "2 - Odcitani\n", "3 - modulo\n", "4 - Exponent")
operace = int(input())

if operace == 1:
    print("Soucet je: ", x+y)
elif operace == 2:
    print("Rozdil je: ", x-y)
elif operace == 3:
    print("Modulo je: ", x%y)
elif operace == 4:
    print("Rozdil je: ", x**y)
else:
    print("Zadana operace neexituje")