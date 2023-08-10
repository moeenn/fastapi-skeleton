import bcrypt

ENCODING: str = "utf-8"


def hash(cleartext: str) -> str:
    salt = bcrypt.gensalt()
    pwd: bytes = cleartext.encode(ENCODING)
    return bcrypt.hashpw(pwd, salt).decode(ENCODING)


def verify(cleartext: str, hashed: str) -> bool:
    return bcrypt.checkpw(
        cleartext.encode(ENCODING),
        hashed.encode(ENCODING),
    )
