#1 imprime los numeros del 1 al 5 utilizando un bucle for
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento == 0:
        continue
    print(elemento)

# 2 imprime los cuadrados de los numeros del 1 al 4.
mi_lista = [1, 2, 3, 4]
mi_lista = [elemento * 2 for elemento in mi_lista]
print(mi_lista)

#3
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_par = 0
for elemento in mi_lista:
    if elemento % 2 == 0:
        suma_par += elemento
    print(suma_par)

