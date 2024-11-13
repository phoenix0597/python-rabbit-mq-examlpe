# consumer.py
import pika

# Параметры подключения
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost", 5672, "/", credentials)
)
channel = connection.channel()

# Убеждаемся, что очередь существует
channel.queue_declare(queue="hello")


# Определяем функцию обратного вызова, которая будет обрабатывать сообщения
def callback(ch, method, properties, body: bytes):
    print(f" [x] Received {body.decode('utf-8')}")


# Подписываемся на очередь
channel.basic_consume(
    queue="hello",
    on_message_callback=callback,
    auto_ack=True,
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
