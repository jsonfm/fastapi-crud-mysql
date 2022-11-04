from fastapi import FastAPI
from config import config
from routes.user import user


app = FastAPI()

app.include_router(user)
