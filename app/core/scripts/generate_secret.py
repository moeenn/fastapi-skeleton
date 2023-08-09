import secrets


def generate_secret(length: int = 64) -> str:
    return secrets.token_hex(length)


if __name__ == "__main__":
    secret = generate_secret()
    print(secret)
