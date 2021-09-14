class Cislo():
    def __init__(self, cislo):
        self.cislo = cislo

    def __add__ (self, other):   #scitani - mam vlastni scitani c1 je self.cislo a c2 je other.cislo. Vychazi z print(c1 + c2)
        print("scitam")
        return self.cislo + other.cislo

    def __mul__(nalevo, napravo): #nasobeni. Vlastni nasobeni, ktere nenasobi
        print("Mel bych nasobit, ale nechci")
        return f"{nalevo.cislo} * {napravo.cislo} a nevim kolik to je"


c1 = Cislo(5)
c2 = Cislo(6)

print(c1 + c2)
print(c1 * c2)