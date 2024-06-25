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
