from tasks import load_data

result = load_data.delay()

print(result.get(timeout=30))

