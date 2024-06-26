#!/usr/bin/env python
import pika

# Establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Create a queue, if it doesn't exist already (note: this is channel-specific)
channel.queue_declare(queue='hello')

# Send a message to the queue. The content of the message will be a string "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()