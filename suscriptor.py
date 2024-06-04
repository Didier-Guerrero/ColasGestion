import pika
import smtplib
from email.mime.text import MIMEText

def send_email(body):
    # Configuración del correo
    sender_email = "didierguerrero70@gmail.com"
    receiver_email = "didierguerrero9078@gmail.com"
    #la password es del sender esta es contraseña de aplicacion
    password = "arfg qgqp flsy sfqp"

    msg = MIMEText(body)
    msg['Subject'] = 'Prueba exitosa'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Enviar correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    send_email(body.decode())

def start_consuming():
    # Conexión a RabbitMQ con credenciales
    credentials = pika.PlainCredentials('admin', '12Didier')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()

    # Declarar una cola
    channel.queue_declare(queue='email_queue')

    # Configurar el consumidor
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Esperando mensaje, para salir CTRL+C')
    channel.start_consuming()


start_consuming()