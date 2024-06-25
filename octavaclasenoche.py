#forma de crear
def imprimir_hola():
    print("hola")

imprimir_hola()

#funciones con parametros
def imprimir_mensaje(mensaje):
    print(mensaje)

imprimir_mensaje("hola")

#funciones con parametros por defecto
def imprimir_mensaje_defecto(mensaje="hola"):
    print(mensaje)

imprimir_mensaje_defecto()
imprimir_mensaje_defecto("hola 2")

class Carro:
    def __inti__(self, placa, modelo, marca, color):
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10


    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10

class Carro:
    def _init_(self, placa, modelo, marca, color, tipo_motor="Manual"):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.velocidad = 0
        self.tipo_motor = tipo_motor
        self.esta_prendido = False
        self.cambio = 0
        self.cloche = False

    def prender(self):
        if not self.esta_prendido:
            self.esta_prendido = True
            print("He prendido el carro")
        else:
            print("El carro se encuentra encendido")

    def meter_cambio(self, cambio, cloche  = False):
        self.cloche = cloche
        if self.cloche:
            if (cambio - self.cambio) > 2:
                self.apagar()
            self.cambio = cambio
            return self.cambio
        else:
            print("Se apaga el carro")
            return cambio

    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print("Acelerando a :", self.velocidad)


    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10

    def apagar(self):
        if self.esta_prendido:
            self.esta_prendido = False

carro1 = Carro("123", "2024", "Mazada", "Cx30", "Rojo")
carro1.prender()
carro1.prender()
print(carro1.meter_cambio(1,True))
acelar = 1
while True:
    carro1.acelerar(acelar)
    if carro1.velocidad >= 10 and carro1.cambio == 1:
        cambio = int(input("Meta un cambio por favor: "))
        carro1.meter_cambio(cambio, True)
        if carro1.velocidad == 15:
            carro1.apagar()
        if not carro1.esta_prendido:
            break

    if carro1.velocidad >= 30 and carro1.cambio == 2:
        cambio = int(input("Meta un cambio por favor: "))
        carro1.meter_cambio(cambio, True)

        if carro1.velocidad == 35:
            carro1.apagar()

        if not carro1.esta_prendido:
            break

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}

libros = []
usuarios = []
libros_usuarios = []

class Usuario(BaseModel):
    nombre: str
    id: int

class Libro(BaseModel):
    titulo: str
    autor: str
    estado: int = 0
    id: int = None

    def guardar(self):
        if self.id is None:
            self.id = len(libros) + 1
            libros.append(self)
        else:
            for libro in libros:
                if libro.id == self.id:
                    libro.autor = self.autor
                    libro.titulo= self.titulo
                    libro.estado = self.estado
        return self


    @classmethod
    def consultar(cls, libro_id):
        for libro in libros:
            if libro.id == libro_id:
                return libro
        return None

    @classmethod
    def consultar_todos(cls):
        return libros



class LibroUsuario():
    usuario_id : int
    libro_id : int
    tiempo_prestamo : int

    def _init_(self):
        pass

@app.post("/libro")
async def crear_libro(libro: Libro):
    return libro.guardar()


@app.get("/libros")
async def consultar_libro():
    return Libro.consultar_todos()

@app.get("/libro/{libro_id}")
async def consultar(libro_id : int):
    return Libro.consultar(libro_id)
