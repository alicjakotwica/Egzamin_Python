products=input("Podaj produkty do kupienia i oddziel je jedynie przecinkami: ").split(",")
produkty=set(products)
lista_zak=dict()


for a in produkty:
    i=a.upper()
    cost=input("Podaj cenę "+i+": ")
    try:
        float(cost)
        lista_zak.update({i:float(cost)})
    except ValueError:
        lista_zak.update({i:0})

suma=sum(lista_zak.values())
if suma<=100:
    print("Masz wystarczająco pieniędzy, by wszystko kupić.")
else:
    print("Nie stać cię na wszystkie artykuły z listy.")