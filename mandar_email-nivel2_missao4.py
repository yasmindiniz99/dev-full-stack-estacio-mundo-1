#import dos pacotes necessários
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

#Função para segurar todo o processo de mandar o email
def send_email(email_recipient, email_subject, email_message, attachment_location = ''):

    #definir o conteudo do email
    email_sender = 'yasmindiniz99@hotmail.com'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_sender, '@P0l01313')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True


def sendEmail(emails):
    for n in range(0, len(emails)):
        send_email(emails[n], 'Mensagem enviada com Python', 'Oi, mãe essa mensagem foi enviada com Python!')

emails = ['mi.diniz@hotmail.com', 'feminicesevaidades@gmail.com', 'micheledinizmarykay@gmail.com']
sendEmail(emails)
