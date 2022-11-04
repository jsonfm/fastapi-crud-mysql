from fastapi import FastAPI
from config import config
from routes.user import user


app = FastAPI(title="FASTAPI + MYSQL 💚")

app.include_router(user)
