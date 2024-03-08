from fastapi import APIRouter, Header
from services.auth import AuthService
from services.task import TaskService
from utils.get_token import get_token




task_router = APIRouter()


@task_router.get("/add_task/{ip}")
async def add_task(ip: str, authorization: str = Header(None)):
    AuthService.authorize(get_token(authorization))
    task = TaskService.add_task(ip)
    return task



@task_router.get("/status/{id}")
async def status(id: str, authorization: str = Header(None)):
    AuthService.authorize(get_token(authorization))
    ip_data = TaskService.result_task(id)
    return ip_data