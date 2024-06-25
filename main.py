#ejercicio 1
a = 5
b = a + 3
c = b * 2
a = c - 1

resultado = a + b + c
print(resultado)
#ejercicio 2
x = 10
y = 2 * x
z = x // 2
x = z + y

resultado = x - y * z
print(resultado)

#ejercicio 3
m = 7
n = m + 3
m = m * 2
n = n - 1

resultado = m % n
print(resultado)

numero = int(input("ingrese un numero"))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

#definicion de nuevas variables
primer_nombre = "juan"
segundo_nombre = "pablo"
primer_apellido = "alvear"
segundo_apellido = "moscote"

print("tu primer nombre es:",
      primer_nombre,
      "tu segundo nombre es:",
      segundo_nombre,
      "tu primer apellido es:",
      primer_apellido,
      "tu segundo apellido es:",
      segundo_apellido)
print("hola mundo\n"*10)

primer_numero = 1
segundo_numero = 10

if primer_numero == 1 and segundo_numero == 10:
    print("this block one")
elif primer_numero == 1 or segundo_numero == 15:
    print("this block two")
elif not(primer_numero == 2):
    print("this block three")
else:
    print("this block four")


