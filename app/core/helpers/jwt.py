import jwt
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from typing import Any
from app.config.auth import AuthConfig


@dataclass
class JWTPayload:
    sub: int
    role: str


def create_token(
    secret: str, payload: JWTPayload, exp_seconds: int | None = None
) -> str:
    """
    generate a JWT using app_secret, which will be read from the environment
    """
    exp = (
        datetime.now(tz=timezone.utc) + timedelta(seconds=exp_seconds)
        if exp_seconds
        else None
    )

    payload_updated = asdict(payload)
    if exp:
        payload_updated.update({"exp": exp})

    return jwt.encode(
        key=secret,
        payload=payload_updated,
        algorithm=AuthConfig.jwt_algo,
    )


def validate_token(secret: str, token: str) -> JWTPayload | None:
    """
    confirm if a provided JWT is valid. If valid, extract payload content from
    the token
    """
    try:
        payload = jwt.decode(
            token,
            key=secret,
            algorithms=[
                AuthConfig.jwt_algo,
            ],
        )
    except:
        return None

    if not "sub" in payload or not "role" in payload:
        return None

    return JWTPayload(
        sub=payload["sub"],
        role=payload["role"],
    )
