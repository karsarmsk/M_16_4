from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
def create_users(user: User, username: str, age: int):
    i_user = len(users)
    if i_user == 0:
        user.id = 1
    else:
        user.id = users[i_user - 1].id +1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int, user: str = Body()):
    raise1 = True
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    if raise1:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    raise2 = True
    i_delete = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(i_delete)
            return delete_user
        i_delete += 1
    if raise2:
        raise HTTPException(status_code=404, detail='User was not found')


