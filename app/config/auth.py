from dataclasses import dataclass
from app.core.helpers.env import env


@dataclass
class AuthConfig:
    secret: str = env("APP_SECRET")
