class KopecekZmrzliny:
    def __init__(self, prichut):
        self.prichut = prichut

    def __str__(self):
        return f"hezky se vypisuje prichut {self.prichut}"



class ZmrzlinovyPohar:
    """
    Umi prodavat kopecky metodou prodej_kopecek s jednim parameterem
    """
    def __init__(self):
        self.pohar = []

        
    def pridej_kopecek(self, kopecek):
        self.pohar.append(kopecek)
       

    def __str__(self):
        result = "Ja jsem zmrzlinovy pohar\n"
        for kopecek in self.pohar:
            result += f"\t{kopecek}\n"
        result += "tohle je konec zmrzlinoveho poharu. Dobrou chut"

        return result

        


kopecek1 = KopecekZmrzliny("Pistaciova")
kopecek2 = KopecekZmrzliny("Hrachova")
kopecek3 = KopecekZmrzliny("Brokolicova")
kopecek4 = KopecekZmrzliny("Hnusna")

# print(kopecek1)
# print(kopecek2)
# print(kopecek3)
# print(kopecek4)

pohar = ZmrzlinovyPohar()


pohar.pridej_kopecek(kopecek1) # instance se dostane do tridy Zmrzlinovy pohar, pak mohu pracovat s instanci v jine tride a mohu pristupovat k hodnotam
pohar.pridej_kopecek(kopecek2)
pohar.pridej_kopecek(kopecek3)
pohar.pridej_kopecek(kopecek4)

# pohar.pohar.apend(kopecek1) # tohle by fungovalo, ale tak to delat nechceme

#print(ZmrzlinovyPohar.__doc__) #takhle obvykle ne


print(pohar)