import smtplib
from email.message import EmailMessage
import string
from difflib import get_close_matches, SequenceMatcher
import sys
import json


# an object representing a certain match, containing information about team names,
# scores, website, and other releveant information
class scoreObj:
    def __init__(self, score, name, website, matchid):
        self.opp_score = {}
        self.score = score
        self.website = website 
        self.og_name = name
        self.modifer = '' # if a team plays in a special divison
        self.matchid = matchid # self made id, used to determine order in the future
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


# turns array of names and scores for a certain website into scoreObj objects
def objectify(scores, names, website, counter):
    s = set()
    for i in range(len(scores)):
        obj = scoreObj(scores[i], names[i], website, i + counter + 1)
        s.add(obj)
    return s


# creates a map of unique names to set of objects that has the unique names
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


# standarizes given array of teamnames, including lowercasing, removing puncation, etc
def nameStandardize(teamname_list):
    AUTO_REMOVE_WORDS = ["esports", "team", "club", "gaming", "sports"] # common strings in team names that don't give information
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

# given map created by mapify(), returns a list of all score objects inside the
# map, changing similar names to be the same, and in format/order for other functions
# in calculations.py to parse
def nameProcessing(the_map):
    counter = 0
    num_of_keys = len(the_map.keys())
    new_map = dict()
    final_list = [] # list to return
    while(counter < num_of_keys): # condition is met when all scoreObj in the_map are processed
        keys = list(the_map.keys())
        name = keys[0] # gets first name, which has not yet been processed
        new_map[name] = the_map[name]
        del the_map[name]
        del keys[0]
        close_matchs = get_close_matches(name, keys, sys.maxsize, 0.7)
        #print("SIMILAR WORDS TO " + name + ": " + str(close_matchs))
        for close_name in close_matchs: # gets all scoreobj with names close to name, and groups them together in the new_map
            new_map[name] = new_map[name].union(the_map[close_name])
            del the_map[close_name]
        counter = counter + len(close_matchs) + 1
    
    for n in new_map.keys():
        for obj in new_map[n]:
            if(obj.modifer != ''):
                obj.name = n
            else:
                obj.name = (n + " " + obj.modifer).strip()
            final_list.append(obj)
    final_list.sort(key=lambda x: x.matchid, reverse=False)
    return final_list


# sends email given by email_message 
def sendMail(email_message):
    # constants, replace if not using gmail
    PORT = 465  
    SMTP_SERVER = "smtp.gmail.com"

    # credentials located in json file, format as given in example_credentials.json
    with open('credentials.json', 'r') as fp:
        data = json.load(fp)

    # google account app password
    # refer to https://support.google.com/accounts/answer/185833
    APP_PASSWORD = data['app_password']

    SENDER_EMAIL = data['sender_email']
    RECIEVER_EMAIL = "knightdips@gmail.com"
    
    # creating message object
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIEVER_EMAIL
    msg['Subject'] = "ARBITRAGE OPPERUNITY"
    msg.set_content(email_message)

    with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        

