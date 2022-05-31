from pydantic import BaseModel
from fastapi import File, UploadFile


# Route: /password
class PasswordModel(BaseModel):
    length: int = 12

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "MKrclk"
                }
            ]
        }


# Route: /gen_palette
class PaletteModel(BaseModel):
    limit: int = 1
    type_as: str = "rgb"
    file: UploadFile = File(...)

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": [
                        [
                            40,
                            47,
                            55
                        ]
                    ]
                }
            ]
        }
