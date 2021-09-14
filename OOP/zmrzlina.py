class KopecekZmrzliny:


    def __init__(self, prichut):
        self.prichut = prichut
        

    def __str__(self):
        return f"hezky se vypisuje prichut {self.prichut}"



class ZmrzlinovyPohar:    
    """
    Umi prodavat kopecky metodou prodej_kopecek s jednim parameterem
    """
    pocet = 3

    def __init__(self):
        self.pohar = []
        #self.__class__.pocet +=1   
    

        
    def pridej_kopecek(self, kopecek):
        if len(self.pohar) <= self.__class__.pocet:
            self.pohar.append(kopecek)
        else:
            print("Moc kopecku")

    def __str__(self):
        result = "Ja jsem zmrzlinovy pohar\n"
        for kopecek in self.pohar:
            result += f"\t{kopecek}\n"
        result += "tohle je konec zmrzlinoveho poharu. Dobrou chut"

        return result

class VelkyPohar(ZmrzlinovyPohar):    
        pocet = 1

kopecek1 = KopecekZmrzliny("Pistaciova")
kopecek2 = KopecekZmrzliny("Hrachova")
kopecek3 = KopecekZmrzliny("Brokolicova")
kopecek4 = KopecekZmrzliny("Hnusna")
kopecek5 = KopecekZmrzliny("AAAA")

# print(kopecek1)
# print(kopecek2)
# print(kopecek3)
# print(kopecek4)

pohar = VelkyPohar()


pohar.pridej_kopecek(kopecek1) # instance se dostane do tridy Zmrzlinovy pohar, pak mohu pracovat s instanci v jine tride a mohu pristupovat k hodnotam
pohar.pridej_kopecek(kopecek2)
pohar.pridej_kopecek(kopecek3)
pohar.pridej_kopecek(kopecek4)
pohar.pridej_kopecek(kopecek5)

# pohar.pohar.apend(kopecek1) # tohle by fungovalo, ale tak to delat nechceme

#print(ZmrzlinovyPohar.__doc__) #takhle obvykle ne


print(pohar)