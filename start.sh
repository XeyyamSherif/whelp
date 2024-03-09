#!/bin/bash


celery -A celery_tasks worker --loglevel=info &

uvicorn main:app --host 0.0.0.0 --port 8000