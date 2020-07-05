import time
import datetime

try:
    ile_sekund = int(input("Ile sekund ma działać program? "))
except ValueError:
    print("Nie podałeś liczby całkowitej!")

today=datetime.datetime.today()
DD=today.day
Mon=time.strftime("%b")
YYYY=today.year
godzina=time.strftime("%H:%M:%S")
unix=time.time()

with open("logs.txt","w") as f:
    for i in range(ile_sekund):
        f.write(str(i)+"|"+str(DD)+" "+str(Mon)+ " " +
        str(YYYY) + "|"+str(godzina)+ "|"+str(unix)+"\n")
        time.sleep(1)