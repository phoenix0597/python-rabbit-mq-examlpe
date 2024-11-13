# producer.py
from time import sleep

import pika

# Параметры подключения
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", 5672, "/", credentials)
)
channel = connection.channel()

# Убеждаемся, что очередь существует
channel.queue_declare(queue="hello")


for i in range(100):
    # Отправляем сообщение
    channel.basic_publish(
        exchange="",
        routing_key="hello",
        body="Hello World!".encode("utf-8"),  # Преобразуем строку в байты
    )
    print(f" [v] Sent 'Hello World {i+1} time!'")
    sleep(1)

# Закрываем соединение
connection.close()
