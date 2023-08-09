from fastapi import FastAPI
import uvicorn
from dataclasses import dataclass
from app.config.server import ServerConfig
from app.core.helpers.env import is_dev
from app.config.auth import AuthConfig

app = FastAPI()


@dataclass
class HomeResponse:
    message: str


@app.get("/")
async def home() -> HomeResponse:
    return HomeResponse(
        message=AuthConfig.secret,
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=ServerConfig.host,
        port=ServerConfig.port,
        reload=is_dev(),
    )
