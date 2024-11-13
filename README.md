# Простой пример использования RabbitMQ в Python

1. Установка необходимых библиотек (не все они необходимы - black - по привычке :)):

```bash
pip install -r requirements.txt
```

2. Запуск RabbitMQ-сервера:

```bash
docker-compose up -d
```

3. Запуск консюмера сообщений:

```bash
python consumer.py
```

4. Запуск продюсера сообщений:

```bash
python producer.py
```

5. Остановка RabbitMQ-сервера:

```bash
docker-compose down
```
