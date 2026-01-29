from sqlalchemy.orm import Session

from src.apps.auth.models.user import User
from src.utils.password import hash_password


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username==username).first()

    def create(self, username: str, password: str) -> User:
        hashed_password = hash_password(password)
        user = User(
            username=username, 
            hashed_password=hashed_password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    