import os
from dotenv import load_dotenv

load_dotenv()


class Settings():
    ip_key: str = os.getenv("API_KEY")
    db_password: str = os.getenv("DB_PWD")
    db_host: str = os.getenv("DB_HOST")



settings = Settings()