import smtplib
from email.message import EmailMessage
import string

def sendMail(email_message):
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
    msg.set_content(email_message)

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        
def nameProcessing(teamname_list):
    AUTO_REMOVE_WORDS = ["esports", "team", "club", "gaming", "sports"]
    list = []
    for name in teamname_list:
        name = name.lower()
        name = name.translate(str.maketrans('', '', string.punctuation))
        for word in AUTO_REMOVE_WORDS:
            name = name.replace(word, '')
        name = name.replace("chall", "challengers")
        name = name.strip()
        list.append(name)
    return list   
