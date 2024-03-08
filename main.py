from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import auth
from api.endpoints import user
from api.endpoints import task
from models.task import IpData
from models.user import User




def create_app() -> FastAPI:
    current_app = FastAPI()
    
    current_app.include_router(user.user_router)
    current_app.include_router(auth.auth_router)
    current_app.include_router(task.task_router)

    return current_app


app = create_app()



app.add_middleware(
    CORSMiddleware,
    # allow_origins=settings.ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    User.create_table()
    IpData.create_table()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
