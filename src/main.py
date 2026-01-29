from fastapi import FastAPI

from src.settings.config import get_settings
from src.api.auth import router as auth_router
from src.settings.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


settings = get_settings()

app.include_router(auth_router)