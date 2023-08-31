from fastapi import FastAPI
import uvicorn
from app.config.server_config import ServerConfig
from app.config.app_config import AppConfig
from app.modules.auth.auth_router import auth_router

app = FastAPI()
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=ServerConfig.host,
        port=ServerConfig.port,
        reload=AppConfig.debug,
    )
