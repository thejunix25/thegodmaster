"""
#ejercicio 1
#obtener un numero por teclado y verificar si es divisible por 2 y por 3
#obtener 3 numeros por teclado y verificar cual es el mayor de los 3
#obtener un numero por teclado y verificar si es par o impar
#pepito perez fue ala tienda a comprar 1 kg de carne donde su valor es de 25.000 pesos el tendero le comento que si compraba 2 kg iba a obtener el 35% de descuento obtener el valor a pagar si pepito compro 2.5 kg de carne
#si andres fue a comprar 5 huevos a la tienda y en la tienda solo habian 3 huevos
entonces andres le toca a)ir a otra tienda b)llevar los 3 huevos ala casa c)comprar otra cosa
determinar la respuesta de la mama
"""
numero = int(input("digite un numero"))

#ejercicio 1
if numero % 2 == 0:
    print(f"el numero {numero}"
          f"es divisible entre 2 y 3")
elif numero % 3 == 0:
    print(f"el numero {numero}"
          f"el numero es divisible entre 2 y 3")
else:
    print("no es divisible por 2 y por 3")

#ejercicio 3

numero = int(input("ingrese un numero"))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

#ejercicio 2

num1 = int(input("ingrese primer numero por teclado"))
num2 = int(input("ingrese segundo numero por teclado"))
num3 = int(input("ingrese tercer numero por teclado"))
if num1 >= num2 and num1 >= num3:
    print("el numero ", num1, "es el mayor de los tres")
if num2 >= num1 and num2 >= num3:
    print("el numero ", num2, "es el mayor de los tres")
if num3 >= num1 and num3 >= num2:
    print("el numero ", num3, "es el mayor de los tres")

#ejercicio 4

valor_carne = 25000 # xkg
cantidad_carne = 2.5 # xkg
total_antes = valor_carne * cantidad_carne
total_despues = 0
if (cantidad_carne >= 2):
    total_despues = total_antes - (total_antes * 0.35)
print("el precio total a pagar de pepito"
      f" por los 2.5 kg de carne es : {total_despues}")

cantidad_huevos = 5
if cantidad_huevos <= 3:
    print("a) ir a otra tienda")
    print("b) llevar los 3 huevos ala casa")
    print("c) comprar otra cosa")
    opcion = input("que opcion escojio andres?:").lower()
    if opcion == "a":
        print("aja y el resto")
    elif opcion == "b":
        print("por que te demoraste?")
    else:
        print("esto no fue lo que pedi")

peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

IMC = round(peso / math.pow(estatura, 2), 1)

print("Su IMC es de " + str(IMC))

lista = [["Composición corporal", "Índice de masa corporal (IMC)"], ["Peso inferior al normal", "Menos de 18.5"],
         ["Normal", "18.5 – 24.9"], ["Peso superior al normal", "25.0 – 29.9"], ["Obesidad", "Más de 30.0"]]

print(tabulate(lista))

"""
(1) suma
(2) resta
(3) multiplicacion
(4) division
"""
def calculadora(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 + num2
    elif op == 3:
        return num1 + num2
    
