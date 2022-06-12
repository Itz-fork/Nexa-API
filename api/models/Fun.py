from pydantic import BaseModel


# Route: /fact
class FactModel(BaseModel):
    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "The longest hiccuping spell lasted a whopping 68 years."
                }
            ]
        }


# Route: /insult
class InsultModel(BaseModel):
    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": "Why are you rolling your eyes? Are you looking for your brain?"
                }
            ]
        }
