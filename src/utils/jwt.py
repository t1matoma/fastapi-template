from datetime import timedelta, datetime

import jwt

from src.settings.config import get_settings


settings = get_settings()


def encode_jwt(
        payload: dict, 
        type: str,
        private_key: str = settings.AUTH_JWT.private_key.read_text(), 
        algorithm: str = settings.AUTH_JWT.algorithm,
        expire_minutes: int = settings.AUTH_JWT.access_token_expire_minutes,
        expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.utcnow()

    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({"type": type,"exp": expire, "iat": now})

    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
        token: str | bytes, 
        public_key: str = settings.AUTH_JWT.public_key.read_text(), 
        algorithms: list[str] = [settings.AUTH_JWT.algorithm]
) -> dict:
    return jwt.decode(token, public_key, algorithms=algorithms)