from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Для запуска сервера, в терминале используйте команду :  uvicorn module_16_3:app --reload

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_users(
        username: Annotated[str, Path(description="Имя пользователя")],
        age: Annotated[int, Path(description="Возраст пользователя")]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(description="ID пользователя")],
        username: Annotated[str, Path(description="Имя пользователя")],
        age: Annotated[int, Path(description="Возраст пользователя")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(description="ID пользователя")]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
