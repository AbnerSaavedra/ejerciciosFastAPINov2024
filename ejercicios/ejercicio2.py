from pydantic import BaseModel, ValidationError
from pydantic import field_validator
from datetime import date
from pydantic_core.core_schema import FieldValidationInfo

class reservaHotel(BaseModel):
    fechaEntrada: date
    fechaSalida: date
    cantHuespedes: int
    tipoHabitacion: str

    # Creamos nuestras validaciones propias
    @field_validator("fechaEntrada")
    def validate_fechaEntrada(cls, v, info: FieldValidationInfo):
        if 'fechaSalida' in info.data and v >= info.data['fechaSalida']:
            raise ValueError("Fecha de salida no puede ser menor a la de entrada.")
        return v
    @field_validator("fechaSalida")
    def validate_fechaSalida(cls, s, info: FieldValidationInfo):
        print("Info data:", info.data)
        if 'fechaEntrada' in info.data and s <= info.data['fechaEntrada']:
            raise ValueError("Fecha de entrada no puede ser mayor a la de salida.")
        return s
    @field_validator("cantHuespedes")
    def validate_quantity(cls, cantHuespedes):
        if cantHuespedes < 1:
            raise ValueError("Quantity not allowed")
        return cantHuespedes
    @field_validator("tipoHabitacion")
    def validarTipoHabitacion(thab):
        if thab in tiposHabitaciones:
            print("Tipo de habitación válido")
        else:
            raise ValueError("Tipo de habitación no válido.")
        return thab

tiposHabitaciones = ["Individual", "Matrimonial", "Familiar"]

fecha1 = date(2024, 11, 22)
fecha2 = date(2024, 11, 20)

#reserva = reservaHotel(fechaEntrada=date(2024, 11, 22), fechaSalida=date(2024, 11, 20), cantHuespedes=-2, tipoHabitacion="duplex")

try:
    reserva = reservaHotel(fechaEntrada=fecha1, fechaSalida=fecha2, cantHuespedes=2, tipoHabitacion="Matrimonial")
    print("Reserva hotel: ", reserva)
except ValidationError as e:
    print(e.json())
  



