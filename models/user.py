from peewee import Model, AutoField, CharField
from core.database import database

class User(Model):
    id = AutoField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = database
    
    