from pydantic import BaseModel,Field
from datetime import date

class MessageCreation(BaseModel):
    question : str = Field(min_length =1)
    reponse : str = Field(min_length =1)
    messageDate : date = Field(default_factory=date.today)