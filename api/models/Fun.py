from pydantic import BaseModel


# Route: /fact
class FactsModel(BaseModel):
    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "The longest hiccuping spell lasted a whopping 68 years."
                }
            ]
        }
