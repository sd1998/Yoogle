import pika

credentials = pika.PlainCredentials('drranqba', '7IgeUUVTTkPQWD2BO3xN4So1O7DEH7iY')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='vulture.rmq.cloudamqp.com', port=5672, virtual_host='drranqba', credentials=credentials, heartbeat=2000, blocked_connection_timeout=2000))
channel = connection.channel()
channel.queue_declare(queue='preprocessing1')
with open('links.txt') as file:
    lines = file.readlines()
    for line in lines:
        channel.basic_publish(exchange='', routing_key='preprocessing1', body=line[0:len(line) - 1])
connection.close()
