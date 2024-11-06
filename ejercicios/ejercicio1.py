from pydantic import BaseModel
from pydantic import field_validator
from email_validator import validate_email, EmailNotValidError


class User(BaseModel):
    name: str
    age: int
    email: str
    password: str

    # Creamos nuestras validaciones propias
    @field_validator("name")
    def validate_name(name):
        if len(name) == 0:
            raise ValueError("Name should'nt be empty.")
        return name
    @field_validator("age")
    def validate_age(age):
        if age < 18 or age > 100:
            raise ValueError("Age not allowed")
        return age
    @field_validator("email")
    def email_validation(cls, email):
        try:
            v = validate_email(email)
            email = v['email']
        except EmailNotValidError as e:
            raise ValueError('Email no permitido'. str(e))
    @field_validator("password")
    def validate_password(password):
        if len(password) < 5:
            raise ValueError("Password not allowed")
        return password

  
user = User(name="Abner", age=33, email="abnersaavedra@gmail.com", password="123456")

print("User: ", user)


