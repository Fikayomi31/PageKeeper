import os
import secrets

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "JWT_SECRET_KEY environment variable is not set. Please set it to a secure random value."
        "Set it before starting the application. You can generate a secure random value using Python's secrets module, for example: secrets.token_hex(32)"
    )

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes
