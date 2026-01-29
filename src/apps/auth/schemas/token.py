from pydantic_settings import BaseSettings


class TokenSchema(BaseSettings):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"

    class Config:
        from_attributes = True
