from fastapi import APIRouter, HTTPException, Header
from api.schemas.auth import LoginSchema, SignUpSchema
from services.auth import AuthService
from utils.get_token import get_token

auth_router = APIRouter()


@auth_router.post("/signup")
async def signup(data: SignUpSchema):
    AuthService.create_user(data.username, data.password)
    return {"message": "User created successfully"}

@auth_router.post("/login", )
async def login(data: LoginSchema):
    token = AuthService.login(data.username, data.password)
    return {"tokens": token}

@auth_router.get("/refresh_token")
async def refresh_token(authorization: str = Header(None)):
    return {"tokens": AuthService.refresh_token(get_token(authorization))}