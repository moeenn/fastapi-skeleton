from fastapi import FastAPI
from app.modules.auth.auth_router import auth_router


app = FastAPI()
app.include_router(auth_router)
