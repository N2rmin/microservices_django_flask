import pika

params=pika.URLParameters('amqps://aklhzvrg:8Hk6Ctf1UGjRgVLHkCjfHHtr1NOoaiU8@cow.rmq2.cloudamqp.com/aklhzvrg')

connection =pika.BlockingConnection(params)

channel=connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='main',body='hello main')
