from pydantic import BaseModel,Field
from datetime import datetime

class MessageCreation(BaseModel):
    question : str = Field(min_length =1)
    reponse : str = Field(min_length =1)
    Datecreation : datetime = Field(default_factory=datetime.utcnow)



class messageOllama(BaseModel):
    question : str = Field(min_length =1)


