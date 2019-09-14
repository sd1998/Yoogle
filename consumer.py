import pika 
from preprocess import preprocess

credentials = pika.PlainCredentials('drranqba', '7IgeUUVTTkPQWD2BO3xN4So1O7DEH7iY')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='vulture.rmq.cloudamqp.com', port=5672, virtual_host='drranqba', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='preprocessing')

def callback(channel, method, properties, body):
    preprocess(body.decode('utf-8'))
    print('Record processed')
    channel.basic_ack(delivery_tag=method.delivery_tag)
    
channel.basic_consume(queue='preprocessing', on_message_callback=callback, auto_ack=False)
channel.start_consuming()