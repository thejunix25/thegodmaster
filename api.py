@app.post("/libros/", response_model=schemas.Libro)
async def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    query = text("INSERT INTO libros (autor, titulo, estado) VALUES (:autor, :titulo, :estado)")
    db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado})
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**libro.dict(), "id": last_id}

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/libros/", response_model=List[schemas.Libro])
async def read_libros(db: Session = Depends(get_db)):
    query = text("SELECT * FROM libros")
    result = db.execute(query).fetchall()
    return [schemas.Libro(id=row.id, autor=row.autor, titulo=row.titulo, estado=row.estado) for row in result]

@app.post("/usuarios/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    query = text("INSERT INTO usuarios (nombre, documento) VALUES (:nombre, :documento)")
    db.execute(query, {"nombre": usuario.nombre, "documento": usuario.documento})
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**usuario.dict(), "id": last_id}

@app.get("/usuarios/", response_model=List[schemas.Usuario])
async def create_libro_usuarios(libro_usuario: schemas.LibroUsuarioCreare,(get_db)):
    query = text("SELECT * FROM usuarios")
    result = db.execute(query).fetchall()
    return [schemas.Usuario(id=row.id, nombre=row.nombre, documento=row.documento) for row in result]

@app.post("/libros_usuarios/", response_model=schemas.LibroUsuario)
async def create_libro_usuario(libro_usuario: schemas.LibroUsuarioCreate, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO libros_usuarios (usuario_id, libro_id, tiempo_prestamo) 
        VALUES (:usuario_id, :libro_id, :tiempo_prestamo)
    """)
    db.execute(query, {
        "usuario_id": libro_usuario.usuario_id,
        "libro_id": libro_usuario.libro_id,
        "tiempo_prestamo": libro_usuario.tiempo_prestamo,
    })
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**libro_usuario.dict(), "id": last_id}

@app.get("/libro/{libro_id}", response_model=schemas.Libro)
async def read_libro(libro_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM libros WHERE id = :libro_id")
    libro = db.execute(query, {"libro_id": libro_id}).fetchone()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro not found")
    return schemas.Libro(id=libro.id, autor=libro.autor, titulo=libro.titulo, estado=libro.estado)


@app.get("/libros/search/", response_model=List[schemas.Libro])
async def search_libros(query: str, db: Session = Depends(get_db)):
    search_query = text("SELECT * FROM libros WHERE titulo LIKE :query")
    result = db.execute(search_query, {"query": f"%{query}%"}).fetchall()
    return [schemas.Libro(id=row.id, autor=row.autor,
                          titulo=row.titulo, estado=row.estado) for row in result]


@app.put("/libro/{libro_id}", response_model=schemas.Libro)
async def update_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    query = text("""
        UPDATE libros SET autor = :autor, titulo = :titulo, estado = :estado 
        WHERE id = :libro_id
    """)
    db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado, "libro_id": libro_id})
    db.commit()
    return {**libro.dict(), "id": libro_id}

@app.delete("/libro/{libro_id}", response_model=dict)
async def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    query = text("DELETE FROM libros WHERE id = :libro_id")
    db.execute(query, {"libro_id": libro_id})
    db.commit()
    return {"message": "Libro eliminado"}