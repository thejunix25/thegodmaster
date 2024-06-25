numeros_pacientes = input("digite la cantidad de paciente")
lista_pacientes = []

for i in range(numeros_pacientes):
    nombre = input("digite nombre paciente: ")
    edad = input("digite la edad: ")
    numero_social = input("digite el numero de seguridad social")
    lista_pacientes.append(dict(
        nombre=nombre,
        edad=edad,
        numaro_social=numero_social,
    ))

n_social=input("digite el numero social del paciente")

for paciente in lista_pacientes:
    if paciente["numero social"] == n_social:
        paciente["temperatura"] = input("digite la temperatura del paciente:")


