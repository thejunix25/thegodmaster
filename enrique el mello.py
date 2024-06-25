#for con break
mi_lista = [1,2,3,4,5]

for elemento in mi_lista:
    if elemento == 3:
        break
    print(elemento)


#for con c
mi_lista = [1,2,3,4,5]
nueva_lista = [elemento * 2 for elemento in mi_lista]
print(nueva_lista)

# for
nombres = ["alice","bob", "charlie"]
edades = [ 25 , 30, 22]


#while con break
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break

#while
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)

#while con else
contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    print("fin del bucle")

#while con pass
contador = 0

while contador < 5:
    pass
contador += 1

#1
#1 imprime los numeros del 1 al 5 utilizando un bucle for
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento == 0:
        continue
    print(elemento)