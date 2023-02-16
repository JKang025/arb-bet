import smtplib
import ssl
from email.message import EmailMessage


def sendMail():
    #constants. Replace if not using gmail
    PORT = 465  
    SMTP_SERVER = "smtp.gmail.com"

    #google account app password
    #refer to https://support.google.com/accounts/answer/185833
    APP_PASSWORD = "hmfocxnsgljbezsf"

    SENDER_EMAIL = "arbbetproject@gmail.com"
    RECIEVER_EMAIL = "arbbetproject@gmail.com"
    
    #creating message object
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIEVER_EMAIL


    msg['Subject'] = "ARBITRAGE OPPERUNITY"
    msg.set_content("This is eamil message")

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        
