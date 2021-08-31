cislo = int(input("Zadej cislo: \n"))

prvni_cislo = cislo // 1000
druhe_mezi = cislo % 1000
druhe_cislo = druhe_mezi //100
treti_mezi = druhe_mezi % 100
treti_cislo = treti_mezi // 10
ctvrte_mezi = treti_mezi % 10


print(prvni_cislo)
print(druhe_mezi)
print(druhe_cislo)
print(treti_mezi)
print(treti_cislo)
print(ctvrte_mezi)

print(ctvrte_mezi,treti_cislo,druhe_cislo,prvni_cislo)

nove_cislo = str(ctvrte_mezi)+str(treti_cislo)+str(druhe_cislo)+str(prvni_cislo)

print(nove_cislo)