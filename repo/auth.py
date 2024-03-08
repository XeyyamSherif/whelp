from peewee import * IntegrityError
from fastapi import FastAPI, HTTPException
from models.user import User


class AuthRepository:
    @classmethod
    def create_user(cls, username: str, password: str) -> User:
        try:
            user = User.create(username=username, password=password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Username already exists.")
