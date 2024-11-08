from typing import Annotated
from fastapi import FastAPI, Form


app = FastAPI()

@app.post("/login")
# Definimos los parámetros Form a traves de anotaciones
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

'''
Las anotaciones en Python son una característica que permite a los desarrolladores indicar el tipo de datos 
de los parámetros de una función o de las variables. También se pueden utilizar para mejorar la legibilidad 
del programa. 

Existen dos tipos principales de anotaciones en Python:
Anotaciones de funciones: Permiten agregar el tipo de los argumentos de entrada y salida de una función. 
Anotaciones de variables: Se utilizan para indicar el tipo de datos de las variables. 
'''