from pydantic import BaseModel, ValidationError
from pydantic import field_validator
from email_validator import validate_email, EmailNotValidError
from pydantic import EmailStr


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    password: str

    # Creamos nuestras validaciones propias
    @field_validator("name")
    def validate_name(n):
        if len(n) == 0:
            raise ValueError("Name should'nt be empty.")
        return n
    @field_validator("age")
    def validate_age(a):
        if a < 18 or a > 100:
            raise ValueError("Age not allowed")
        return a
    '''@field_validator("email")
    def email_validation(cls, email):
        try:
            v = validate_email(email)
            email = v['email']
        except EmailNotValidError as e:
            raise ValueError('Email no permitido'. str(e))'''
    @field_validator("password")
    def validate_password(password):
        if len(password) < 5:
            raise ValueError("Password not allowed")
        return password

  
try:
    user = User(name="", age=120, email="abnersaavedra@gmail.com", password="1234")
    print("User: ", user)
except ValidationError as e:
    print(e.json())


