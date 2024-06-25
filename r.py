import random

alzar = random.randint(1,1000)
numero = int(input("dijite el numero ganador:"))
while alzar != numero:
    if numero > alzar:
        print("el numero que digite el"
              "es mayor")
    else:
        print("el numero que digitaste el"
              "es menor")

    numero = int(input("digite el numero ganador:"))
else:
    print("ganaste")









