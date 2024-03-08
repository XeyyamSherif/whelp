from models.task import IpData
from celery_tasks import my_task
import requests
from config import settings

class TaskService:
    @classmethod
    def add_task(cls, ip :str):
        ip_data = requests.get(f"https://api.ipdata.co/{ip}?api-key={settings.ip_key}&fields=ip,is_eu,city,region,region_code,country_name,country_code,continent_name,continent_code,latitude,longitude,postal,calling_code,flag,emoji_flag,emoji_unicode").json()
        task = my_task.delay(ip_data)
        return {"task_id": task.id}
    
    def result_task(task_id: str):
        result = my_task.AsyncResult(task_id)
        IpData.create(**result.get())
        return result.get()