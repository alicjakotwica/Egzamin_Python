import random
import math

number=list()

for i in range(10):
    element=random.random()
    number.append(element)

numbers=sorted(number)

with open("percent.txt","w") as f:
    for a in numbers:
        b=math.trunc(100*a)
        f.write(str(a)+";"+str(b)+"%"+"\n")

