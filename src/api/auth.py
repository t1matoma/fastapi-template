from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer

from settings.database import get_db
from apps.auth.schemas.user import UserSchema, UserCreateSchema
from apps.auth.schemas.token import TokenSchema
from apps.auth.services.user import UserService
from api.dependencies import get_current_user, get_current_user_access, get_current_user_refresh


http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix="/auth", 
    tags=["auth"],
    dependencies=[Depends(http_bearer)]
)


@router.post("/login", response_model=TokenSchema)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    service = UserService(db)
    access_token = service.login(form_data.username, form_data.password)
    refresh_token = service.create_refresh_token(form_data.username)
    if not access_token or not refresh_token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenSchema(access_token=access_token, refresh_token=refresh_token)


@router.post(
        "/refresh", 
        response_model=TokenSchema,
)
def refresh_token(
    db: Session = Depends(get_db),
    user = Depends(get_current_user_refresh)
):
    service = UserService(db)
    access_token = service.create_access_token(user.username)
    if not access_token:
        raise HTTPException(status_code=401, detail="Invalid credentials 3")
    return TokenSchema(access_token=access_token)


@router.get("/me", response_model=UserSchema)
def read_current_user(
    user: UserSchema = Depends(get_current_user_access)
):
    user = UserSchema(username=user.username)
    return user


# TODO: Implement user registration with proper validation
@router.post("/register", response_model=UserSchema)
def register(
    user_data: UserCreateSchema,
    db: Session = Depends(get_db)
):
    service = UserService(db)
    user = service.create_user(user_data.username, user_data.pasword)
    if not user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return UserSchema(username=user.username)

