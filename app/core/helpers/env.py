import os


def env(key: str) -> str:
    """read a value from system env"""
    value: str | None = os.getenv(key)
    if not value:
        raise Exception(f"failed to read environment variable: {key}")

    return value
