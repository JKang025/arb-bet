import webscraper
from calculations import Graph
from utils import nameStandardize, sendMail, nameProcessing, mapify, objectify

luckboxname = ['LGD Gaming', 'Ninjas in Pyjamas', 'Frank Esports', 'Deep Cross Gaming', 'Hanwha Life Esports', 'DRX', 'ThunderTalk Gaming', 'Oh My God', 'Beyond Gaming', 'SEM9 WPE', 'Impunity', 'J Team', 'CTBC Flying Oyster', 'PSG Talon', 'Cryptova', 'Sinners Esports', 'Team Brute', 'Dynamo Eclot', 'Team ESCA Gaming', 'Alior Bank Team', 'BIG', 'NNO Prime', 'Entropiq', 'eSuba', 'Grypciocraft Esports', 'Exeed Poland', 'Eintracht Spandau', 'Eintracht Frankfurt', 'Valiance', 'Crvena zvezda', 'Iron Wolves', 'Komil&Friends', 'UOL Sexy Edition', 'SK Gaming Prime', 'White Dragons', 'EGN Esports', 'MAGAZA', 'Cyber Wolves', 'Kwandong F Chall', 'Kwangdong Freecs Challengers']
luckboxscore = [3.1, 1.32, 1.42, 2.7, 1.32, 3.1, 1.62, 2.15, 1.06, 7.0, 1.62, 2.15, 1.62, 2.15, 2.4, 1.5, 2.9, 1.35, 2.9, 1.35, 2.1, 1.65, 1.8, 1.9, 1.13, 5.0, 1.3, 3.2, 2.8, 1.38, 1.32, 3.1, 1.72, 2.0, 1.5, 2.4, 2.9, 1.35, 1.0, 1.0]
luckboxname = nameStandardize(luckboxname)
luckboxobj = objectify(luckboxscore, luckboxname, "Luckbox")

pinname = ['SANDBOX', 'T1', 'Hanwha Life', 'DRX', 'Kwangdong Freecs', 'BRION', 'Nongshim RedForce', 'KT Rolster', 'T1', 'Gen.G', 'Liiv SANDBOX', 'Dplus KIA', 'LGD', 'Ninjas in Pyjamas', 'ThunderTalk', 'Oh My God', 'Invictus', 'JD Gaming', 'Rare Atom', 'Bilibili', 'SANDBOX', 'T1', 'LGD', 'Ninjas in Pyjamas', 'Ultra Prime Academy', 'Pinnacle', 'Frank', 'Deep Cross', 'Hanwha Life', 'DRX', 'SEM9 WPE', 'Beyond', 'V3', 'Sengoku', 'ThunderTalk', 'Oh My God', 'J Team', 'Impunity', 'PSG Talon', 'CTBC Flying Oyster', 'Cryptova', 'SINNERS Esports', 'BRUTE', 'Dynamo Eclot', 'ESCA', 'Alior Bank', 'Falcons', 'Villarreal QLASH', 'Lille', 'Project Conquerors', 'Entropiq', 'eSuba', 'Schalke 04', 'GamerLegion', 'Grypciocraft', 'exeed', 'LEX', 'Levante UD', 'beGenius ESC', 'ViV', 'Valiance', 'Crvena zvezda', 'Sampi', 'Inside Games', 'Eintracht Spandau', 'Eintracht Frankfurt', 'Iron Wolves', 'Komil and Friends', 'AYM', 'ZETA', 'Akroma', 'Du Sud', 'MAGAZA', 'Cyber Wolves', 'Unicorns of Love SE', 'SK Gaming Prime', 'Illuminar', 'Maturalni Forsaken', 'White Dragons', 'EGN', 'Wizards', 'Case', 'Joblife', 'Atletec', 'BIG', 'NNO Prime', 'Szaty Bobra', 'Zero Tenacity', 'GTZ', 'Byteway', 'Ramboot', 'ZEST', 'MS Company', 'Klanik', 'Maycam Evolve', 'Boca Juniors', 'Ankora', 'Partizan', 'MOUZ', 'E WIE EINFACH', 'Boavista FC', 'Odivelas', 'Counter Logic Gaming', 'FlyQuest', 'For The Win', 'Varona', 'Immortals', 'Evil Geniuses', 'Liquid', 'Cloud9', 'TSM', 'Dignitas', 'Golden Guardians', '100 Thieves', 'Kwangdong Freecs', 'BRION', 'Invictus', 'JD Gaming', 'Fukuoka Softbank Hawks', 'AXIZ', 'Nongshim RedForce', 'KT Rolster', 'Impunity', 'Beyond', 'Rare Atom', 'Bilibili', 'Deep Cross', 'PSG Talon', 'Detonation FocusMe', 'Burning Core', 'Ultra Prime', 'Weibo', 'J Team', 'CTBC Flying Oyster', 'HELL PIGS', 'SEM9 WPE', 'FURIA', 'Los Grandes', 'RED Canids', 'Fluxo', 'Heretics', 'SK Gaming', 'KaBuM', 'paiN', 'INTZ', 'Vivo Keyd Stars', 'Liberty', 'LOUD', 'Astralis', 'BDS', 'TSM Chall', 'Liquid First', 'FlyQuest Chall', 'Cincinnati Fear', 'Immortals Chall', 'CLG Chall', 'Dignitas Chall', 'Wildcard', 'Cloud9 Chall', 'Area of Effect', 'Evil Geniuses Chall', '100 Thieves Chall', 'T1', 'Gen.G', 'LNG', 'FunPlus Phoenix', 'Sengoku', 'Crest Act', 'Liiv SANDBOX', 'Dplus KIA', 'PSG Talon', 'J Team', "Anyone's Legend", 'Team WE', 'Beyond', 'HELL PIGS', 'EDward Gaming', 'Top Esports', 'CTBC Flying Oyster', 'Frank', 'SEM9 WPE', 'Impunity', 'INTZ', 'RED Canids', 'Fluxo', 'Los Grandes', 'paiN', 'LOUD', 'FURIA', 'Vivo Keyd Stars', 'KaBuM', 'Liberty', 'Cincinnati Fear', 'Liquid First', 'Golden Guardians Chall', 'CLG Faith', 'Liquid Chall', 'FLY FAM', 'TSM Chall', 'Cloud9 Chall', 'FlyQuest Chall', 'Wildcard', 'Dignitas Chall', '100 Thieves Chall', 'KOI', 'G2', 'FURIA Academy', 'Los Grandes Academy', 'RED Academy', 'Fluxo Academy', 'KaBuM Academy', 'paiN Academy', 'INTZ Academy', 'Vivo Keyd Stars Academy', 'Liberty Academy', 'LOUD Academy', 'Forsaken', 'Alior Bank', 'Grypciocraft', 'ESCA', 'Verdant', 'Nativz', 'Szaty Bobra', 'Iron Wolves', 'Ruddy', 'Riddle', 'Komil and Friends', 'Exeed', 'UniQ', 'NORD', 'Illuminar', 'Zero Tenacity', 'Domino', 'Vanir', 'INTZ Academy', 'RED Academy', 'Fluxo Academy', 'Los Grandes Academy', 'Six Karma', 'Isurus', 'FURIA Academy', 'Vivo Keyd Stars Academy', 'paiN Academy', 'LOUD Academy', 'Estral', 'Aze', 'KaBuM Academy', 'Liberty Academy', 'Forsaken', 'ESCA', 'Szaty Bobra', 'Komil and Friends', 'UniQ', 'Riddle', 'Iron Wolves', 'Grypciocraft', 'Domino', 'NORD', 'Zero Tenacity', 'Alior Bank', 'Verdant', 'Vanir', 'Illuminar', 'Exeed', 'Ruddy', 'Nativz', 'The Kings', 'All Knights', 'Rainbow7', 'Infinity', 'Dire Wolves', 'PEACE', 'Bliss', 'Kanga', 'Pentanet.GG', 'MAMMOTH', 'Chiefs', 'Ground Zero']
pinscore = [3.2, 1.359, 1.306, 3.54, 1.884, 1.934, 5.04, 1.178, 1.335, 3.34, 3.17, 1.366, 4.39, 1.219, 1.636, 2.29, 4.03, 1.25, 2.88, 1.427, 3.2, 1.359, 4.39, 1.219, 1.057, 7.4, 1.384, 2.87, 1.306, 3.54, 7.5, 1.075, 27.3, 1.006, 1.636, 2.29, 2.46, 1.51, 2.03, 1.735, 2.3, 1.578, 2.94, 1.37, 3.18, 1.322, 1.781, 1.892, 1.333, 2.92, 1.694, 2.09, 2.02, 1.74, 1.139, 5.24, 2.01, 1.689, 1.552, 2.24, 2.69, 1.431, 1.558, 2.34, 1.271, 3.52, 1.386, 2.87, 2.92, 1.333, 3.85, 1.2, 2.5, 1.492, 1.833, 1.909, 2.01, 1.751, 1.512, 2.45, 2.23, 1.558, 1.344, 2.87, 2.18, 1.636, 2.46, 1.507, 1.223, 3.95, 1.25, 3.41, 4.26, 1.166, 2.51, 1.442, 7.39, 1.077, 1.248, 3.7, 3.32, 1.299, 3.74, 1.28, 1.131, 5.41, 3.91, 1.261, 2.63, 1.5, 1.505, 2.61, 2.56, 1.52, 1.884, 1.934, 4.03, 1.25, 1.05, 9.43, 5.04, 1.178, 2.02, 1.746, 2.88, 1.427, 2.35, 1.552, 1.118, 5.75, 6.71, 1.116, 2.99, 1.358, 1.33, 3.14, 3.49, 1.274, 1.5, 2.48, 2.0, 1.833, 1.456, 2.61, 1.869, 1.869, 3.0, 1.357, 3.01, 1.398, 2.12, 5.72, 3.44, 3.13, 2.8, 3.61, 2.36, 4.78, 1.476, 12.65, 4.91, 2.34, 1.335, 3.34, 1.207, 4.56, 1.06, 8.5, 3.17, 1.366, 1.392, 2.84, 4.0, 1.253, 1.297, 3.33, 2.36, 1.606, 1.763, 1.99, 5.94, 1.112, 3.25, 1.309, 2.74, 1.418, 2.09, 1.689, 1.421, 2.73, 1.338, 3.09, 1.833, 7.45, 1.279, 20.02, 1.229, 23.87, 7.96, 1.775, 5.19, 2.26, 2.33, 4.97, 2.22, 1.675, 2.02, 1.74, 1.2, 4.22, 1.188, 4.37, 3.12, 1.333, 1.8, 1.943, 1.609, 2.23, 1.201, 4.2, 1.25, 3.69, 1.361, 2.98, 2.81, 1.4, 1.662, 2.14, 7.07, 1.083, 3.3, 1.302, 2.65, 1.444, 3.96, 1.222, 2.48, 1.5, 1.574, 2.3, 2.81, 1.4, 1.869, 1.869, 1.113, 5.91, 1.285, 3.41, 1.268, 3.28, 1.143, 4.62, 7.89, 1.037, 2.93, 1.332, 6.93, 1.056, 1.251, 3.4, 1.416, 2.6, 1.337, 2.9, 1.099, 5.52, 2.02, 1.68, 1.478, 2.41, 1.438, 2.52, 1.078, 6.31, 1.023, 11.13, 1.048, 8.0]
pinname = nameStandardize(pinname)
pinobj = objectify(pinscore, pinname, "Pinnacle")

joined = luckboxobj.union(pinobj) 

the_map = mapify(joined)
for key in the_map.keys():
    for obj in the_map[key]:
        print(obj)
print("----------------------------------")
the_set = nameProcessing(the_map)
for obj in the_set:
    print(obj)

luckbox_final_name = []
luckbox_final_score = []

pin_final_name = [] 
pin_final_score = []

for obj in the_set:
    if(obj.website == 'Luckbox'):
        luckbox_final_name.append(obj.name)
        luckbox_final_score.append(obj.score)
    elif(obj.website == 'Pinnacle'):
        pin_final_name.append(obj.name)
        pin_final_score.append(obj.score)

g = Graph()
g.initialize_graph("Pinnacle", pin_final_name, pin_final_score)
# result = g.update_graph("Luckbox", luckbox_final_name, luckbox_final_score)
print("\n\n\n----------\n")
# g.output_graph


for node in g:
    print("There is a node here")


# print(result)
#webscraper.pinnacle()

