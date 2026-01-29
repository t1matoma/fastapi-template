from fastapi import FastAPI

from settings.config import get_settings
from api.auth import router as auth_router
from settings.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


settings = get_settings()

app.include_router(auth_router)