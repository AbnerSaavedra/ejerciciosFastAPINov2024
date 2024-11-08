from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/files')
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post('/uploadfile')
async def create_upload_file(file: UploadFile):
    await file.seek(0)
    content = await file.read()
    await file.close()
    print("Content: ", content)
    return {"filename": file.filename, "content_type": file.content_type, "file": file.file}