from peewee import Model, AutoField, CharField, BooleanField, FloatField
from core.database import database

class IpData(Model):
    ip = CharField()
    is_eu = BooleanField(default=False)
    city = CharField(default='')
    region = CharField(default='')
    region_code = CharField(default='')
    country_name = CharField(default='')
    country_code = CharField(default='')
    continent_name = CharField(default='')
    continent_code = CharField(default='')
    latitude = FloatField(default=0.0)
    longitude = FloatField(default=0.0)
    postal = CharField(default=None, null=True)
    calling_code = CharField(default='')
    flag = CharField(default='')
    emoji_flag = CharField(default='')
    emoji_unicode = CharField(default='')

    class Meta:
        database = database