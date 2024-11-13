from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

'''
En Python, la sentencia pass se usa como marcador de posición para indicar que no se necesita código real en una 
situación donde una sentencia es sintácticamente necesaria. Cuando se ejecuta, no se devuelve nada y no sucede nada. 
 
En el caso de las clases, la palabra clave pass se usa para indicar que no hay nada que hacer en la clase. 
Se utiliza cuando se quiere crear una clase, método, función, bucle o condicional, pero aún no se quiere definir 
ningún comportamiento. 
 
El código vacío no está permitido en bucles, definiciones de funciones, definiciones de clases o instrucciones if. 

https://www.datacamp.com/es/tutorial/python-pass#:~:text=La%20sentencia%20Python%20pass%20sirve,en%20un%20bloque%20de%20c%C3%B3digo.

'''