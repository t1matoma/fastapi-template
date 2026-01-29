from fastapi import Depends, HTTPException
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from utils.jwt import decode_jwt
from apps.auth.services.user import UserService
from settings.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db=db)


def validate_token_type(payload: dict, token_type: str):
    if payload.get("type") != token_type:
        raise HTTPException(status_code=401, detail="Invalid token type")
    return True

def get_current_user(
    token_type: str,
):
    def dependency(
        token: str = Depends(oauth2_scheme),
        service: UserService = Depends(get_user_service),
    ):
        try:
            payload = decode_jwt(token)
            print("Decoded payload:", payload)  #
        except InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials 1")
        
        validate_token_type(payload, token_type)

        username = payload.get("sub")
        user = service.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials 2")
        return user
    return dependency


get_current_user_access = get_current_user(token_type="access")
get_current_user_refresh = get_current_user(token_type="refresh")

