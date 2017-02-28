import pika
properties = pika.BasicProperties(delivery_mode=2)
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='test')
channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Mensaje de prueba')
connection.close()
