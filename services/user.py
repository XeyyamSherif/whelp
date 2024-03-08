from fastapi import HTTPException, status
from jose import JWTError
from models.user import User
from utils.get_token import get_token
from utils.jwt import decode_jwt_token


class UserService:
    @classmethod
    def get_user(cls, username: str, authorization):
        try:
            payload = decode_jwt_token(get_token(authorization))
            username: str = payload.get("sub")
        except JWTError as e:
            raise e
        user = User.get_or_none(username=username)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return User.get(username=username)