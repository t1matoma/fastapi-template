from pydantic_settings import BaseSettings


class UserSchema(BaseSettings):
    username: str

    class Config:
        from_attributes = True


class UserCreateSchema(UserSchema):
    password: str