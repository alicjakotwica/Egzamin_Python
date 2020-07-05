import math

def pole_kola(r):
    return math.pi*math.pow(r,2)

def pole_trojkatu(a,h):
    return (1/2)*a*h

def pole_prostokatu(a,b=None):
    if b==None:
        return math.pow(a,2)
    else:
        return a*b

try:
    figura=int(input("Wybierz figurę, której pole chcesz policzyć (koło [1], trójkąt [2], prostokąt [3]) wpisując odpowiednią cyfrę: "))
except ValueError:
    print("Nie podałeś liczby!")
    exit(-1)

if figura==1:
    try:
        r=float(input("Podaj długość promienia koła: "))
        if r>0:
            print("Pole figury koła o podanych wartościach wynosi "+str(pole_kola(r)))
        else:
            print("Promień koła musi być liczbą dodatnią!")
    except ValueError:
        print("Długość promienia nie jest liczbą!")
elif figura==2:
    try:
        a=float(input("Podaj długość boku trójkąta: "))
        h=float(input("Podaj długość wysokości opartej na podanym boku: "))
        if a>0 and h>0:
            print("Pole figury trójkąta o podanych wartościach wynosi "+str(pole_trojkatu(a,h)))
        else:
            print("Długość boku i wysokości musi być liczbą dodatnią!")
    except ValueError:
        print("Długość boku/wysokości nie jest liczbą!")
elif figura==3:
    a=input("Podaj długość boku a prostokąta: ")
    b=input("Podaj długość boku b prostokąta: ")

    if a.isnumeric() and b.isnumeric():
        a=float(a)
        b=float(b)
        if a>0 and b>0:
            print("Pole figury prostokątu o podanych wartościach wynosi "+str(pole_prostokatu(a,b)))
        else:
            print("Długość boków musi być liczbą dodatnią!")
    elif a.isnumeric() and b.isnumeric()==False:
        a=float(a)
        if a>0:
            print("Pole figury prostokątu (kwadratu) o podanych wartościach wynosi "+str(pole_prostokatu(a)))
        else:
            print("Długość boku musi być liczbą dodatnią!")
    elif a.isnumeric()==False and b.isnumeric():
        b=float(b)
        if b>0:
            print("Pole figury prostokątu (kwadratu) o podanych wartościach wynosi "+str(pole_prostokatu(b)))
        else:
            print("Długość boku musi być liczbą dodatnią!")
    else:
        print("Długości obu boków nie są liczbami!")

else:
    print("Podałeś złą liczbę, nie wiem czego pole chcesz policzyć!")
    exit(-1)



