class Zmrzlina:
    def __init__(self, prichut):
        self.prichut = prichut


    def __str__(self):
        return f"Prichut je {self.prichut}"


cokoladova = Zmrzlina("Cokoladova")
vanilkova = Zmrzlina("Vanilkova")

prichute = [cokoladova, vanilkova]

for i in prichute:
    print(i)



class Napoj:
    def __init__(self, jmeno, teplota = 20):
        self.jmeno = jmeno
        self.teplota = teplota

    def __str__(self):
        return f"Napoj je {self.jmeno}"\
            f" teplota je {self.teplota}"



cola = Napoj("Cola", 21)
fanta = Napoj("Fanta")

print(cola)
print(fanta)


class Kniha:
    def __init__(self, autor, jmeno, rok_vydani, cena):
        self.autor = autor
        self.jmeno = jmeno
        self.rok_vydani = rok_vydani
        self.cena = cena


    def __str__(self):
        return f"Knuhu napsal {self.autor} v roce {self.rok_vydani}"\
            f" Kniha se jmenuje {self.jmeno} a stoji {self.cena}"


psohlavci = Kniha("Jirasek", "Psohlavci", 1820, 3.54 )
honzikova_cesta = Kniha("Nevim kdo", "Honzikova cesta", 1980, 20 )

print(psohlavci)
print(honzikova_cesta)