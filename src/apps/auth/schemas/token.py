from pydantic import BaseModel, ConfigDict


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"

    model_config = ConfigDict(from_attributes=True)
