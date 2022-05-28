from pydantic import BaseModel


# Route: /acronym
class AcronymModel(BaseModel):
    word: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "I Don't Give A F***"
                }
            ]
        }


# Route: /define
class DefineModel(BaseModel):
    word: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": {
                        "type": "Adjective",
                        "definition": [
                            "consisting of or combining two races"
                        ]
                    }
                }
            ]
        }


# Route: /tr
class TranslateModel(BaseModel):
    text: str
    dest: str = "en"

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": {
                        "translation": "Hola",
                        "origin": "en",
                        "dest": "es"
                    }
                }
            ]
        }
