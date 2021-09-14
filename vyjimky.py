# EXCEPTIONS - pouzivaji se pri praci s chybama

while True: 
    try:
        cislo1 = int(input("Zadej cislo: "))
        cislo2 = int(input("Zadej cislo: "))
        vysledek = cislo1 / cislo2
        print("Vypocitano. Koncime")
        break
    except ValueError as e:
        print("Value error")
        print(e)
    except ZeroDivisionError as e: # takto se uklada instance ValueError do promenne e
        print("Zero division")
        print(e)
    except:
        print("Nejaka necekana vyjimka")

print("program v pohode pokracuje")

#LBYL = look before you leap
#EAFP = easier to ask forgiveness then permission


#toto je vlastni definice vyjimky, ktera dedi od parent vyjimky "Exception"
class TooManyEmployersException(Exception):
    pass

employers = 500

def delej_neco_jineho():
    if employers > 400:
        raise TooManyEmployersException


def delej_neco():
    delej_neco_jineho()

try:
    delej_neco()
except TooManyEmployersException:
    print("to many")
