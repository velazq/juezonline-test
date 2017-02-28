import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print("Recibido: %r" % body)

channel.basic_consume(callback,
                      queue='test',
                      no_ack=True)

print('Esperando a recibir mensajes...')
channel.start_consuming()
