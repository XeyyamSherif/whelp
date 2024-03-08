from fastapi import APIRouter, Header

from services.user import UserService


user_router = APIRouter()


@user_router.get("/getuser/{username}")
async def get_user(username: str, authorization: str = Header(None)):
    user = UserService.get_user(username, authorization)
    return user