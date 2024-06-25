#entrada
texto = input("ingrese el texto")
numero = int(input("ingrese el numero"))

#salida
print("hola mundo")
print(f"texto con variable {texto}")

numero = 1

if (numero == 1):
      print("primer camino")
      # action
elif (numero == 0):
    print("segundo camino")
    # action
else:
    print("tercer camino")
        # action




numero = int(input("digite un numero"))

if numero % 2 == 0:
    print(f"el numero {numero}"
          f"es divisible por 2 ")
elif numero % 3 == 0:
    print(f"el numero {numero}"
          f" es divisible por 3 ")
else:
    print("no es divisible por 2 ni por 3")

cantidad_libros = int(input("ingrese la cantidad de libros que desea comprar "))
precio_unitario = float(input("ingrese el precio unitario de cada libro: "))
nivel_academico = input("ingrese su nivel academico ('primaria', 'secundaria', 'universidad'): ").lower()

#calcular costo total antes de descuentos
costo_total = cantidad_libros * precio_unitario

# aplicar descuento del 5% si la cantidad de libros es 3 o mas
if cantidad_libros >= 3:
    costo_total *= 0.95

# aplicar descuento adicional del 10% si el nivel academico es "universidad"
if nivel_academico == " universidad":
    costo_total *= 0.9

#aplicar descuento adicional del 7% si el costo total es $50 o mas
if costo_total >= 50:
    costo_total *= 0.93

# imprimir recibo detallado
print("\nrecibo detallado")
print(f"cantidad de libros : {cantidad_libros}")
print(f"precio unitario: ${precio_unitario:.2f}")
print(f"costo total antes de descuentos: ${cantidad_libros * precio_unitario:.2f}")
print(f"costo total despues de descuentos: ${costo_total:.2f}")

#ejercicio
palabra = input ("ingrese una palabra: ")
if palabra == palabra[::-1]:
    print("¡la palabra es un palindromo!")
else:
    print("la palabra no es un palindromo.")



