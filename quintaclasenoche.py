#operaciones de conjutos (union, intersection, diferencia)
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
print(conjunto1)
print(conjunto2)

union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
diferencia = conjunto1.difference(conjunto2)
print(union)
print(interseccion)
print(diferencia)

#longitud
conjunto = {1, 2, 3, 4, 5,}
longitud = len(conjunto)
print(conjunto)
print(longitud)

#inmutabilidad como las tuplas
conjunto_inmutable =frozenset([1, 2, 3, 4])
print(conjunto_inmutable)

#modificar elemento
mi_diccionario = {"nombre": "juan", "edad": 25, "ciudad": "ejemplo"}
mi_diccionario = [edad] = 26
mi_diccionario = [ocupacion] = "estudiantes"
print(mi_diccionario)
print(mi_diccionario)
print(mi_diccionario)

#eliminar elementos
del mi_diccionario ["edad"]
print(mi_diccionario)

#longitud
longitud = len(mi_diccionario)
print(longitud)

#sintaxis de diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}


alumno1 = {"nombre": "juan", "edad": 18, "ciudad": "valledupar", "grado": 10, "colegio": "eloy quintero araujo", "telefono": 3016096773}
alumno2 = {"nombre": "jose", "edad": 20, "ciudad": "medellin", "grado": 11, "colegio": "loperena", "telefono": 3225763064}
alumno3 = {"nombre": "junix", "edad": 19, "ciudad": "japon", "grado": 10, "colegio": "gakkou", "telefono": 819012345678}
alumno4 = {"nombre": "lina", "edad": 23, "ciudad": "costa rica", "grado": 11, "colegio": "humboldt", "telefono": 50688888888}
alumno5 = {"nombre": "esteban", "edad": 17, "ciudad": "bogota", "grado": 10, "colegio": "loperena", "telefono": 3225763064}
alumno6 = {"nombre": "samuel", "edad": 16, "ciudad": "cali", "grado": 9, "colegio": "loperena", "telefono": 3225763064}
alumno7 = {"nombre": "manuel", "edad": 16, "ciudad": "choco", "grado": 10, "colegio": "loperena", "telefono": 3225763064}
alumno8 = {"nombre": "kevin", "edad": 24, "ciudad": "cauca", "grado": 11, "colegio": "loperena", "telefono": 3225763064}
alumno9 = {"nombre": "carlos", "edad": 22, "ciudad": "medellin", "grado": 11, "colegio": "loperena", "telefono": 3225763064}
alumno10 = {"nombre": "andres", "edad": 21, "ciudad": "caldas", "grado": 11, "colegio": "loperena", "telefono": 3225763064}

lista_estudintes = [alumno1, alumno2, alumno3, alumno4, alumno5, alumno6, alumno7, alumno8, alumno9, alumno10]

print(lista_estudintes)

lista_estudintes.pop(5)
lista_estudintes.pop(7)
lista_estudintes[3]["nombre"] = "profesor"

#range(stop)
rango1 = range(5)
print(rango1)

#range(start, stop)
rango2 = range(2, 7)
print(rango2)

#range(start, stop, step)
rango3 = range(1, 10, 2)
print(rango3)

#convertir a lista de numeros
lista_numeros = list(range(5))
print(lista_numeros)

mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    print(elemento)

#for con if
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    if elemento % 2 == 0:
        print(f"numero par: {elemento}")
    else:
        print(f"numero impar: {elemento}")

#for con sprint
mensaje = "hola, mundo!"

for caracter in mensaje:
    print(caracter)