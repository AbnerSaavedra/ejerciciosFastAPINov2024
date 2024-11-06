from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import *
 
app = FastAPI()

class Producto(BaseModel):

    id: int
    nombre: str
    descripcion: str
    precio: int
    categoria: str
    fechaCreacion: datetime
    fechaActualizacion: datetime

listaProductos = []

@app.get("/productos", response_model=List[Producto])
def get_products() -> List[Producto]:
    return listaProductos

@app.post("/productos/", response_model=Producto)
def crear_producto(producto: Producto):
    listaProductos.append(producto)
    return producto

@app.get("/productos/{id}")
def get_producto(id: int):
    if len(listaProductos) > 0:
        producto = list(filter(lambda p: p.id == id, listaProductos))
        return producto
        
@app.put("/productos/{id}")
def update_producto(id: int, producto: Producto):
    for prod in listaProductos:
        if prod.id == id:
            index = listaProductos.index(prod)
            listaProductos[index] = producto
    return producto


@app.delete("/productos/{id}")
def delete_producto(id: int):
    for prod in listaProductos:
        if prod.id == id:
            index = listaProductos.index(prod)
            del listaProductos[index]
    return {"mensaje": "Producto eliminado exitosamente.", "productos": listaProductos}
