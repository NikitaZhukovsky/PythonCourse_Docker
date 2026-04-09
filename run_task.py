from tasks import load_data
import sys

def run_task():
    try:
        result = load_data.delay()
        print(result.get(timeout=30))
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_task()