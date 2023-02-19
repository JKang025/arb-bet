import smtplib
from email.message import EmailMessage
import string
from difflib import get_close_matches, SequenceMatcher
import sys

class scoreObj:
    def __init__(self, score, name, website, matchid):
        self.score = score
        self.website = website 
        self.og_name = name
        self.modifer = ''
        self.matchid = matchid
        li = list(name.split(" "))
        if(SequenceMatcher(None, 'challengers', li[-1]).ratio() > 0.6):
            self.modifer = 'challengers'
            del li[-1]
        elif(SequenceMatcher(None, 'academy', li[-1]).ratio() > 0.6):
            self.modifer = 'academy'
            del li[-1]
        self.name = ' '.join(li)
    def __str__(self):
        return self.og_name + " | " + self.name + " | " + self.modifer + " | " + str(self.score) + " | " + self.website


def objectify(scores, names, website, counter):
    s = set()
    for i in range(len(scores)):
        obj = scoreObj(scores[i], names[i], website, i + counter + 1)
        s.add(obj)
    return s

def mapify(objs):
    the_map = dict()
    for obj in objs:
        if(obj.name in the_map):
            the_map[obj.name].add(obj)
        else:
            s = set()
            s.add(obj)
            the_map[obj.name] = s
    return the_map

def nameStandardize(teamname_list):
    AUTO_REMOVE_WORDS = ["esports", "team", "club", "gaming", "sports"]
    list = []
    for name in teamname_list:
        name = name.lower()
        name = name.translate(str.maketrans('', '', string.punctuation))
        for word in AUTO_REMOVE_WORDS:
            name = name.replace(word, '')
        #name = name.replace("chall", "challengers")
        name = name.strip()
        list.append(name)
    return list   

def nameProcessing(the_map):
    counter = 0
    num_of_keys = len(the_map.keys())
    
    new_map = dict()
    
    while(counter < num_of_keys):
        keys = list(the_map.keys())
        name = keys[0]
        #print("hehehe " + name)
        new_map[name] = the_map[name]
        del the_map[name]
        del keys[0]
        close_matchs = get_close_matches(name, keys, sys.maxsize, 0.7)
        print("SIMILAR WORDS TO " + name + ": " + str(close_matchs))
        for close_name in close_matchs:
            new_map[name] = new_map[name].union(the_map[close_name])
            del the_map[close_name]
        counter = counter + len(close_matchs) + 1
    
    final_list = []
    for n in new_map.keys():
        for obj in new_map[n]:
            if(obj.modifer != ''):
                obj.name = n
            else:
                obj.name = (n + " " + obj.modifer).strip()
            final_list.append(obj)
    
    final_list.sort(key=lambda x: x.matchid, reverse=False)
    return final_list





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
        

