from tasks import load_data

try:
    result = load_data.delay()
    print(result.get(timeout=30))
except Exception as e:
    print(f"Ошибка: {e}")