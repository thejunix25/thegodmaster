from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {"jello": "world"}

class User(BaseModel):
    username: str
    email: str
    password: str

@app.post("/users/")
async def create_user(user: User):
    return{
        "username": user.username,
        "email": user.email,
        "password": hash(user.create)
    }

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    return {
        "user_id": user_id,
        "username": user.username,
        "email": user.email,
        "password": hash(user.password)
    }

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {
        "message": f"usuario con el"
        f"id: {user_id} eliminado "
        f"correctamente"
    }

class UserUpdate(BaseModel):
    email: optional[str] = None

n = input

n / =0