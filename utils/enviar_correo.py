from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from smtplib import SMTP # Simple Message Transfer Protocol
from os import environ, getcwd, path

def enviar_correo(destinatarios, titulo, cuerpo):
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    # Agregamos el titulo a nuestro mensaje
    mensaje['Subject'] = titulo

    # Agregando el cuerpo a nuestro mensaje
    mensaje.attach(MIMEText(cuerpo))

    #           SERVIDOR              | PUERTO
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail   > smtp.gmail.com        | 587
    # icloud  > smtp.mail.me.com      | 587
    # yahoo   > smtp.mail.yahoo.com   | 587

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(user=email_emisor, password=password_email_emisor)

    emisor.sendmail(from_addr=email_emisor, to_addrs=destinatarios, msg=mensaje.as_string())

    # Cerrar la conexion con mi servidor de correos
    emisor.quit()

def enviar_correo_adjuntos(destinatarios, titulo):
    cuerpo = 'Por favor, revisa los archivos adjuntos'
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_SENDER')
    password_email_emisor = environ.get('PASSWORD_SENDER')

    # Agregamos el titulo a nuestro mensaje
    mensaje['Subject'] = titulo

    mensaje.attach(MIMEText(cuerpo))

    # getcwd > nos devuelve la ruta en la cual esta nuestro archivo  principal del proyecto en el servidor (app.py)
    ruta = getcwd()
    # path.join > en base a los parametros que nosotros le pasemos creara la cadena de direccion ya sea con '/' o '\'
    ruta_definitiva = path.join(ruta, 'utils', 'lapicero.jpg')

    with open(ruta_definitiva, 'rb') as archivo:
        print(archivo)
        archivo = MIMEApplication(archivo.read(), Name='lapicero.jpg')
    
    # luego de que se termino la lectura del archivo
    archivo['Content-Disposition'] = 'atachement; filename="lapicero.jpg"'
    mensaje.attach(archivo)

    emisor = SMTP('smtp.gmail.com', 587)

    emisor.starttls()

    emisor.login(user=email_emisor, password=password_email_emisor)

    emisor.sendmail(from_addr=email_emisor, to_addrs=destinatarios, msg=mensaje.as_string())

    emisor.quit()