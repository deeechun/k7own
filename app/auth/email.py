from flask_mail import Mail, Message
import os

mail = Mail()

def send_mail(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=os.environ['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)