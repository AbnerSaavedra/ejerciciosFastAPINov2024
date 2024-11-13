import time 

from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()

#https://fastapi.tiangolo.com/advanced/middleware/#integrated-middlewares

'''
app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)
'''

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["localhost", "*.example.com"]
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get('/holaMundo')
def home():
    return {"message": "Hello world"}

'''
Los encabezados HTTP, o HTTP headers, permiten transferir información cuando el cliente o el servidor realizan 
una petición o envían una respuesta. En una petición a un servidor web se incluye una primera línea con datos 
básicos sobre la petición seguida de una serie de líneas que son los encabezados o headers. A esta primera línea 
se le conoce como request line y al resto de líneas que la suceden se les denomina encabezados HTTP.

La mayor parte de los encabezados son opcionales y depende del tipo de solicitud o respuesta será necesario 
incluirlas.

https://www.hostingplus.pe/blog/cual-es-la-funcion-de-los-encabezados-http/

¿Qué es Compresión GZIP?
La compresión con GZIP permite comprimir los recursos de una página web antes de que estos sean servidos a los 
navegadores de los usuarios para que la página web cargue más rápido y se mejore de esta manera su WPO.

https://borjaarandavaquero.com/que-es/compresion-gzip/
'''