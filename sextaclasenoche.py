#for con if
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento % 2 == 0:
        print(f"numero par: {elemento}")
    else:
        print(f"numero impar: {elemento}")

#for con sprint
mensaje ="hola mundo"

for caracter in mensaje:
    print(caracter)

#for con break
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento == 3:
        break
    print(elemento)

#for con continue
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento == 3:
        continue
    print(elemento)

#for con comprehesion
mi_lista = [elemento * 2 for elemento in mi_lista]
print(mi_lista)

#for con zip (iterar dos listas a la vez)
nombres = ["alice", "bob", "charlie"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

#while con break
contador = 0

while True :
    print(contador)
    contador += 1
    if contador >= 5:
        break

#while con continue
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)


#1 imprime los numeros del 1 al 5 utilizando un bucle for
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento == 0:
        continue
    print(elemento)

#2 imprime los cuadrados de los numeros del 1 al 4.
mi_lista =[1, 2, 3, 4]
mi_lista = [elemento * 2 for elemento in mi_lista]
print(mi_lista)

#5 imprime los caracteres de la cadena de texto "DevZeros
mensaje = "DevZeros"

for caracter in mensaje:
    print(caracter)

#3
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_par = 0
for elemento in mi_lista:
    if elemento % 2 == 0:
        suma_par += elemento
        print(f"numero par: {elemento}")

#4
mi_lista = [10, 20, 30, 40, 50]
for elemento in mi_lista:
    print(elemento)

numero = input("ingresa un numero positivo")
contador = 1

while contador < 11:
    print(contador * 5)


import random

# Genera un número aleatorio entre 1 y 5
numero_aleatorio = random.randint(1, 100)
numero_teclado = int(input("digite un numero: del 1 al 100"))

while (numero_aleatorio != numero_teclado):
    if numero_teclado > numero_aleatorio:
        print("el numero digitado es mayor que el esperado")
    elif numero_aleatorio < numero_teclado:
        print("el numero digitado es menor que el esperado")
        numero_teclado = int(input("digite un numero: del 1 al 100: "))
print("has ganado")
