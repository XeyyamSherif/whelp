from fastapi import HTTPException, status
from jose import JWTError
from peewee import  IntegrityError
from models.user import User
from utils.jwt import create_tokens_pair, decode_jwt_token



class AuthService:
    @classmethod
    def create_user(cls, username: str, password: str) -> User:
        try:
            user = User.create(username=username, password=password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Username already exists.")
    
    @classmethod
    def login(cls, username: str, password: str) -> User:
        user = User.get_or_none(username=username, password=password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_tokens_pair({"sub": user.username})
    
    
    @classmethod
    def refresh_token(cls, token: str):
        try:
            payload = decode_jwt_token(token)
            username: str = payload.get("sub")
        except JWTError as e:
            raise e
        user = User.get_or_none(username=username)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_tokens_pair({"sub": user.username})
    
    
    
    @classmethod
    def authorize(cls, token: str):
        try:
            payload = decode_jwt_token(token)
            username: str = payload.get("sub")
        except JWTError as e:
            raise e
        user = User.get_or_none(username=username)
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


    