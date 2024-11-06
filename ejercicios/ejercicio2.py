from pydantic import BaseModel
from pydantic import field_validator
from datetime import *

tiposHabitaciones = ["Individual", "Matrimonial", "Familiar"]

fecha1 = datetime(year=2024, month=11, day=22).date()
fecha2 = datetime(year=2024, month=11, day=20).date()

class reservaHotel(BaseModel):
    fechaEntrada: datetime
    fechaSalida: datetime
    cantHuespedes: int
    tipoHabitacion: str

    # Creamos nuestras validaciones propias
    '''@field_validator("fechaEntrada", "fechaSalida")
    def validarFechasReservacion(cls, fechaEntrada,fechaSalida):
        if fechaSalida <= fechaEntrada:
            raise ValueError("Fecha de salida no puede ser menor a la de entrada.")'''
    @field_validator("cantHuespedes")
    def validate_quantity(cantHuespedes):
        if cantHuespedes < 1:
            raise ValueError("Quantity not allowed")
        return cantHuespedes
    @field_validator("tipoHabitacion")
    def validarTipoHabitacion(tipoHabitacion):
        if tipoHabitacion in tiposHabitaciones:
            print("Tipo de habitación válido")
        else:
            raise ValueError("Tipo de habitación no válido.")

  
reserva = reservaHotel(fechaEntrada="2024-11-06", fechaSalida="2024-11-07", cantHuespedes=2, tipoHabitacion="Matrimonial")

print("Reserva hotel: ", reserva)


