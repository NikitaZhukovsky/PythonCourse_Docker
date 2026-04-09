import os
import json
import redis
from celery_app import app

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True
)


@app.task
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    try:
        for key, value in data.items():
            redis_client.set(key, json.dumps(value, ensure_ascii=False))
    except Exception as e:
        return f"Ошибка при сохранении: {str(e)}"

    return f"Загружено {len(data)} ключей"

