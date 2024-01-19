# Event-Driven Communication

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue='order_events')

channel.basic_publish(exchange='', routing_key='order_events', body='Order Created')
