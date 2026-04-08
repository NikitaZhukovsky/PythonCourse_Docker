# 1. Запустить контейнеры
```bash
docker-compose up -d
```

# 2. Загрузить данные в Redis
```bash
docker exec redis-loader-worker python run_task.py
```
# 3. Посмотреть записи в Redis
```bash
docker exec redis-loader-redis redis-cli --scan | % { $k=$_; $v=docker exec redis-loader-redis redis-cli GET $_; "$k : $v" }
```

