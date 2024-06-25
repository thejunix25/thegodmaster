#crear lista
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_string = ["a", "b", "c"]
lista_mixta = [1, "dos", 3.0, True]

#acceso a elementos
lista = ["a", "b", "c", "d"]
primer_elemento = lista[0]
segundo_elemento = lista[1]

#modificando elementos
lista = ["a", "b", "c", "d"]
lista[2] = "nuevo_valor"
print(lista[2])

#cortar listas
listas = [1, 2, 3, 4, 5]
sublistas = listas[1:4]

#unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2

#verificacion de elemento en lista
lista = ["a", "b", "c"]
existe_a = "a" in lista
existe_x = "x" in lista

#ordenar lista
lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
lista_numeros.sort()

#agregar elementos
lista = ["a", "b", "c"]


#pepito en la tienda

lista_valores = [40000, 8000, 4000, 25000, 6000]
total = 0
for i in lista_valores:
    total += i

print(total)

lista_valores.remove(4000)

toal = 0
for i in lista_valores:
    total += i
print(total)

lista_valores.sort()
indice_verduras = lista_valores.index(6000)
lista_valores[indice_verduras] = 5000

