import threading
import time
# Función que se ejecutará de forma asíncrona
def saluda(nombre):
    # Espera 2 segundos
    time.sleep(2)
    print(f"Hola {nombre}")

# Declaro un hilo de ejecución
threading_greet = threading.Thread(target=saluda, args=("Abner",))
# Lo lanzo
threading_greet.start()
# Resto de mi código que se ejecutará de forma paralela
print("Soy el resto del código")