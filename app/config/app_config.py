from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    debug: bool = os.getenv("APP_MODE") == "dev"