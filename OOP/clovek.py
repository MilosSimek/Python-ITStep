class Clovek:
    def __init__ (self, jmeno, prijmeni, pracoviste, povolani):
        self.jmenu = jmeno
        self.prijmeni = prijmeni
        self.pracoviste = pracoviste
        self.povolani = povolani

    def vstavej(self):
        print("Dobre Rano")
        print("Dnes jsem se dobre vyspal")

    def jdi_do_mesta(self, mesto):
        """mesto je obycejny paramter, neboli nezavisla promenna"""
        print(f"jdi do {mesto}")

    def jdi_do_prace(self, pracoviste):
        """pracoviste je obycejny paramter, neboli nezavisla promenna"""
        print(f"Jdu do {pracoviste}")

    def jdi_do_prace2(self):
        """pracoviste je vlastnost patrici instanci tridy, proto
        jdu pomoci teckove notace
        tj. napr. pracovist je vlastnost patrici Karlovi
        pristup pres tecku = pristup do objektu, resp. do instance"""
        print(f"Jdu do {self.pracoviste}")


karel = Clovek("Karel", "Novak", "IBM", "programator")

karel.vstavej()
karel.jdi_do_prace("Avast")
karel.jdi_do_prace2()
karel.jdi_do_mesta("Dilli")

aneta = Clovek("Aneta", "Cerna", "Seznam.cz", "manazerka")

aneta.jdi_do_prace2()