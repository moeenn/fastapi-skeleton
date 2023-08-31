from fastapi import APIRouter, HTTPException
from app.config.auth_config import AuthConfig
from app.core.helpers import jwt
from .auth_dto import LoginRequest, LoginResponse

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login")
async def login(body: LoginRequest) -> LoginResponse:
    if body.email != "admin@site.com":
        raise HTTPException(
            status_code=401,
            detail={
                "error": "invalid email or password",
            },
        )

    payload = jwt.JWTPayload(
        sub=10,
        role="ADMIN",
    )

    token = jwt.create_token(AuthConfig.secret, payload, 300)
    return LoginResponse(token=token)
