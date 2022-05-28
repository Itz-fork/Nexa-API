from pydantic import BaseModel


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
