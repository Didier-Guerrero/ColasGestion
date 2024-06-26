import pika
import smtplib
from email.mime.text import MIMEText

def send_email(body):
    sender_email = "didierguerrero70@gmail.com"
    receiver_email = "didierguerrero9078@gmail.com"
    password = "arfg qgqp flsy sfqp"
    msg = MIMEText(body)
    msg['Subject'] = 'Prueba exitosa'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Mail enviado a {receiver_email}")

def callback(ch, method, properties, body):
    print(f"Received {body}")
    send_email(body.decode())

def start_consuming():
    credentials = pika.PlainCredentials('admin', '12Didier')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('Esperando mensaje, para salir CTRL+C')
    channel.start_consuming()

start_consuming()


#anadir objetos clases, un caso de uso real