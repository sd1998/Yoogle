import pika
from preprocess import preprocess

credentials = pika.PlainCredentials('<cred_user>', '<cred_pass>')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='vulture.rmq.cloudamqp.com', port=5672, virtual_host='<host>', credentials=credentials, heartbeat=2000, blocked_connection_timeout=2000))
channel = connection.channel()
channel.queue_declare(queue='preprocessing1')

def callback(channel, method, properties, body):
    preprocess(body.decode('utf-8'))
    print('Record processed')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='preprocessing1', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
