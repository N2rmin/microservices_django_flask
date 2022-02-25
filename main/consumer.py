import pika
params=pika.URLParameters('amqps://aklhzvrg:8Hk6Ctf1UGjRgVLHkCjfHHtr1NOoaiU8@cow.rmq2.cloudamqp.com/aklhzvrg')

connection =pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue='main')

def callback(ch,method,properties,body):
    print("Received in main")
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback, auto_ack=True)

print("Starting Consuming")

channel.start_consuming()
channel.close()