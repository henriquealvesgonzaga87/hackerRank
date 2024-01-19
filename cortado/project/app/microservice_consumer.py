# Event-Driven Communication

import pika


def callback(ch, method, properties, body):
    print(f"Received order event: {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue='order_events')

channel.basic_consume(queue='order_events', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
