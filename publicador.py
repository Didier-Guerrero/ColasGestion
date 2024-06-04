import pika

def send_message_to_queue(message):
    credentials = pika.PlainCredentials('admin', '12Didier')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    print(f" [x] Sent '{message}'")
    
    connection.close()

send_message_to_queue('Funciona el sistema de colas!')