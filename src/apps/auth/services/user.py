from sqlalchemy.orm import Session

from ..repositories.user import UserRepository
from ..models.user import User
from utils.password import verify_password
from utils.jwt import encode_jwt


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def get_user_by_username(self, username: str) -> User | None:
        return self.user_repository.get_user_by_username(username)

    def create_user(self, username: str, password: str) -> User | None:
        existing_user = self.get_user_by_username(username)
        if existing_user:
            return None
    
        return self.user_repository.create(username, password)
    
    def verify_user_credentials(self, username: str, password: str) -> bool:
        user = self.get_user_by_username(username)
        if not user:
            return False
        
        return verify_password(password, user.hashed_password)
    
    def create_access_token(self, username: str) -> str | None:
        user = self.get_user_by_username(username)
        if not user:
            return None
        token = encode_jwt({"sub": user.username}, type="access")  # 15 minutes
        return token
    

    def login(self, username: str, password: str) -> str | None:
        is_valid = self.verify_user_credentials(username, password)
        if not is_valid:
            return None
        
        return self.create_access_token(username)
      
    def create_refresh_token(self, username: str) -> str | None:
        user = self.get_user_by_username(username)
        if not user:
            return None
        refresh_token = encode_jwt({"sub": user.username}, type="refresh", expire_minutes=60*24*7)  # 7 days
        return refresh_token
