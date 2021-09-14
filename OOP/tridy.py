class Clovek():
    pocet = 0

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.__class__.pocet += 1

    def __repr__(self):
        return f"Jsem {self.jmeno} {self.prijmeni} a " \
            f"uz existuji {self.__class__.pocet}"

    def vstavej(self):
        print("Dobre rano")

    def jdi_do_prace(self):
        print("Vyrazim do prace, za chvili tam budu")

class Programator(Clovek):

    def __init__(self, jmeno, prijmeni, jazyk):
        super().__init__(jmeno, prijmeni)
        self.jazyk = jazyk

    def programuj(self):
        print("Programuji si bez oblibeneho programovaciho jazyka")



karel = Programator("Karel", "Novak", "Python")
aneta = Clovek("Aneta", "Lan")

print(karel)
karel.vstavej()
karel.jdi_do_prace()
karel.programuj()


aneta.vstavej()
aneta.jdi_do_prace()
# aneta.programus()

