def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

numbers=list()
liczba=0

while liczba!="exit":
    liczba=input("Podaj liczbę: ")
    if is_numeric(liczba):
        numbers.append(liczba)
    elif is_numeric(liczba)==False and liczba!="exit":
        break
if liczba=="exit":
    for i in numbers:
        print(i)
else:
    print("Podałeś "+str(len(numbers))+" liczb. Dalej się nie bawię")