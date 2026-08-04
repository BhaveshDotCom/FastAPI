from fastapi import FastAPI
from pydantic import BaseModel
'''
response_model defines what the client sees in the response, regardless of what your function actually returns. Hides sensitive fields (password, tokens, etc.)
'''

app = FastAPI()

class Response(BaseModel):
    name:str
    age:int
    passwd:str

class ClientResponse(BaseModel):
    name:str
    age:int

@app.get("/response", response_model=ClientResponse)
def response():
    return {
        "name" : "Bhavesh",
        "age" : 19,
        "passwd" : "123"
    }