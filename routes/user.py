from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User


user = APIRouter(prefix="/users", tags=["users"])


@user.get("/", response_model=list[User], description="Returns a list with all availables users.")
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/", response_model=User, description="Creates a new user.")
def create_user(user: User):
    result = conn.execute(users.insert().values(user.dict()))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/{id}", response_model=User, description="Return an user given an id.")
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, description="Delete an user given an id.")
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id)).first()
    return Response(status=HTTP_204_NO_CONTENT)


@user.put("/{id}", response_model=User, description="Update user info.")
def update_user(id: str, user: User):
    print("user: ", user)
    conn.execute(users.update().values(user.dict()).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
