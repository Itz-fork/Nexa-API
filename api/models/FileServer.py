from pydantic import BaseModel
from fastapi import File, UploadFile


# Route: /upload
class UploadModel(BaseModel):
    file: UploadFile = File(...)

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": {
                        "name": "arch.zip",
                        "id": "z.ip8hC5y7VcG58uLYV5uCMznA.zip"
                    }
                }
            ]
        }


# Route: /download
class DownloadModel(BaseModel):
    id: str

    class Config:
        schema_extra = {
            'examples': [
                {}
            ]
        }


# Route: /delete
class DeleteModel(BaseModel):
    id: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "File - z.ip8hC5y7VcG58uLYV5uCMznA.zip removed!"
                }
            ]
        }
