from peewee import *
from config import settings


timeout = 10

database = MySQLDatabase(
    'whelp',
    user='avnadmin',
    password=settings.db_password,
    host=settings.db_host,
    port=21293,
    charset='utf8mb4',
    connect_timeout=timeout,
    read_timeout=timeout,
    write_timeout=timeout
)