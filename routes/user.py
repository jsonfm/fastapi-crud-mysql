from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User


user = APIRouter(prefix="/users")

@user.get("/")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/")
def create_user(user: User):
    result = conn.execute(users.insert().values(user.dict()))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/{id}")
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/{id}")
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id)).first()
    return Response(status=HTTP_204_NO_CONTENT)


@user.put("/{id}")
def update_user(id: str):
    conn.execute(users.update().values().where(users.c.id == id))
    return "updated"
