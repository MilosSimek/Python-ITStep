class Clovek:
    def __init__(self, jmeno_z_parametru, prijmeni_z_parametru, vek_z_parametru=20):  
        self.jmeno = jmeno_z_parametru
        self.prijmeni = prijmeni_z_parametru
        self.vek = vek_z_parametru
        self.kde_pracuje = "IBM"
        if self.vek >= 18:
            self.plolety = True
        else:
            self.plolety = False

        
        # magicka metoda. (dunder). Maji specialni funkce uvnitr jazyka
        # __init__ se musi psat u kazde tridy
        # self je hodnota atributu pro vytvorenou instanci
    
    def __str__(self):
        return f"Jmenuji se {self.jmeno} {self.prijmeni}"\
            f" a je mi {self.vek} let"


karel = Clovek("Karel", "Novak", 29)


aneta = Clovek("Aneta", "Fialova", 15)
aneta2 = Clovek("Aneta", "Modra")
aneta3 = Clovek(prijmeni_z_parametru="Cervena", vek_z_parametru=2, jmeno_z_parametru="Pavla")

print(karel)
print(aneta)
print(aneta2)
print(aneta3)


