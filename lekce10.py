menu = {'kure': 200, 'smazak': 180, 'bazant': 350, 'svickova': 350}
objednavka = ''
suma = 0


while objednavka != 0:
    for key, value in menu.items():
        if objednavka == key:
            suma +=value
            print(suma)
        else:
            objednavka = (input())
    print(suma)
    

    