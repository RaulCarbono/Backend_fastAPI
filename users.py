from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#inicia el serevidor: univcorn users:app --reload

#entidad user

class User(BaseModel) : 
    id : int
    name: str
    surname : str
    url : str
    age : int

users_fake_db = [User(id=1, name="Raul",surname="Carbono", url="https://prueba.com", age=24),
                 User(id=2, name="Carbono", surname="Alejandro", url="https://tegano.com", age=25)]





@app.get("/users")
async def users() : 
    return users_fake_db


#path
@app.get("/user/{id}/")
async def user(id:int) : 
   return search_user(id)

#query 
@app.get("/user/")
async def user(id:int, name:str) : 
   return search_user(id)

@app.get("/userquery/")
async def user(id:int) : 
   return search_user(id)
   
    
def search_user(id:int) :
    users = filter(lambda user :user.id == id, users_fake_db)
    try: 
        return list(users)[0]
    except:
        return {"error":"no existe ese usuaio compae"}