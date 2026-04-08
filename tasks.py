import json
import redis
from celery_app import app

redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)


@app.task
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, value in data.items():
        redis.set(key, json.dumps(value))

    return f"Загружено {len(data)} ключей"

