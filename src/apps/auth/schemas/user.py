from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    username: str

    model_config = ConfigDict(from_attributes=True)


class UserCreateSchema(UserSchema):
    password: str
