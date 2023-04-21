from utils import *
from webscraper import *
from calculations import *
#luckbox_info = luckbox()
luckbox_team_name = ['kabum', 'liberty', 'cincinnati fear', 'liquid first', 'golden guardians academy', 'clg faith', 'tsm academy', 'cloud9 academy', 'flyquest academy', 'wildcard', 'dignitas academy', '100 thieves academy', 'liquid academy', 'flyquest fam', 'brion challengers', 'kt rolster challengers', 'ninjas in pyjamas', 'thundertalk', 'dplus kia challengers', 'liiv sandbox youth', 'lgd', 'royal never give up', 'koi', 'g2', 't1 challengers', 'drx challengers', 'oh my god', 'ultra prime', 'hanwha life  challengers', 'nongshim redforce academy', 'weibo', 'invictus', 'inside games', 'dynamo eclot', 'cryptova', 'esuba', 'grypciocraft', 'esca', 'verdant', 'nativz', 'sampi', 'sinners', 'rebels', 'fnatic tq', 'ruddy', 'riddle', 'brute', 'entropiq', 'szaty bobra', 'iron wolves', 'mcon lg ultragear', 'northern lions', 'uniq', 'nord', 'blx utd', 'krc genk', 'guasones', 'fc barcelona', '7am', 'the agency', 'illuminar', 'zero tenacity', 'domino', 'vanir', 'movistar riders', 'giants', 'zennit', 'heet', 'bisons e', 'koi academy', 'six karma', 'isurus', 'estral', 'aze', 'nongshim redforce', 'geng', 'jd', 'funplus phoenix', 'kt rolster', 'dplus kia', 'lng', 'bilibili', 'forsaken', 'esca', 'galakticos', 'beşiktaş', 'uniq', 'riddle', 'szaty bobra', 'komilfriends', '5 ronin', 'istanbul wildcats', '3bl', 'anubis', 'aegis', 'ldlc ol', 'uol sexy edition', 'e wie einfach', 'gamerlegion', 'eintracht spandau', 'iron wolves', 'grypciocraft', 'domino', 'nord', 'valiance', 'diamant', 'fox', 'gng', 'dark passage', 'supermassive', 'bk rog', 'karmine corp', 'sk  prime', 'big', 'zero tenacity', 'alior bank', 'verdant', 'vanir', 'nigma galaxy', 'triple', 'fut', 'nasr', 'magaza', 'crvena zvezda', 'gameward', 'solary', 'ruddy', 'nativz', 'ankora', 'cyber wolves', 'geekay', 'raad', 'fc schalke 04', 'nno prime', 'xtremedominators', 'partizan', 'mouz', 'eintracht frankfurt', 'bds academy', 'izi dream', 'the kings', 'all knights', 'rainbow7', 'infinity', 'liiv sandbox youth', 'brion challengers', 'hanwha life', 'brion', 'geng challengers', 'dplus kia challengers', 't1', 'liiv sandbox', 'nongshim redforce academy', 'kt rolster challengers', 'geekay', 'anubis', 'istanbul wildcats', 'beşiktaş', 'izi dream', 'ldlc ol', 'sk  prime', 'fc schalke 04', 'mcon lg ultragear', 'the agency', 'eintracht spandau', 'nno prime', 'magaza', 'diamant', 'galakticos', 'fut', '3bl', 'gng', 'fc barcelona', 'heretics academy', 'go', 'aegis', 'rebels', 'movistar riders', 'for the win', 'boavista fc', '5 ronin', 'supermassive', 'fox', 'nigma galaxy', 'northern lions', 'zennit', 'karmine corp', 'gameward', 'uol sexy edition', 'big', 'krc genk', 'heet', 'mouz', 'gamerlegion', 'guasones', 'koi academy', 'valiance', 'partizan', 'triple', 'raad', 'bds academy', 'solary', 'varona', 'egn', 'e wie einfach', 'eintracht frankfurt', 'blx utd', '7am', 'bisons e', 'giants', 'cyber wolves', 'crvena zvezda', 'vitalitybee', 'bk rog', 'odivelas', 'byteway', 'flyquest', '100 thieves', 'gtz', 'white dragons', 'immortals', 'liquid', 'golden guardians', 'cloud9', 'tsm', 'counter logic', 'dignitas', 'evil geniuses', 'hanwha life  challengers', 'drx challengers', 'geng', 'drx', 'kwangdong freecs challengers', 't1 challengers', 'ninjas in pyjamas', 'anyones legend', 'kwangdong freecs', 'dplus kia', 'we', 'rare atom', 'tsm', 'cloud9', 'dignitas', 'flyquest', 'golden guardians', 'evil geniuses', 'immortals', 'counter logic', 't1', 'kt rolster', 'royal never give up', 'thundertalk', 'nongshim redforce', 'liiv sandbox', 'jd', 'top', 'brion', 'drx', 'funplus phoenix', 'lgd', 'kwangdong freecs', 'hanwha life', 'dire wolves', 'peace', 'bliss', 'kanga', 'pentanetgg', 'mammoth', 'chiefs esc', 'ground zero', 'inside games', 'brute', 'cryptova', 'entropiq', 'sinners', 'dynamo eclot', 'sampi', 'esuba']
luckbox_team_name = nameStandardize(luckbox_team_name)
luckbox_score = [9.0, 1.03, 1.5, 12.0, 1.38, 12.0, 9.0, 1.62, 4.0, 1.98, 2.15, 3.6, 1.26, 10.0, 10.0, 1.02, 2.35, 1.52, 1.17, 4.4, 5.3, 1.12, 2.15, 1.62, 1.65, 2.1, 1.32, 3.1, 1.52, 2.35, 1.52, 2.35, 6.3, 1.08, 3.8, 1.22, 1.13, 5.0, 1.22, 3.8, 2.8, 1.38, 2.0, 1.72, 2.8, 1.38, 5.3, 1.12, 1.26, 3.4, 1.42, 2.7, 7.0, 1.06, 4.8, 1.15, 6.3, 1.08, 1.52, 2.35, 3.2, 1.3, 2.7, 1.42, 1.42, 2.7, 2.4, 1.5, 1.42, 2.7, 1.52, 2.35, 1.06, 7.0, 7.0, 1.06, 1.06, 7.0, 1.55, 2.3, 1.52, 2.35, 1.26, 3.4, 1.72, 2.0, 7.5, 1.05, 1.15, 4.8, 6.3, 1.08, 2.1, 1.65, 2.4, 1.5, 1.2, 4.0, 3.4, 1.26, 3.2, 1.3, 7.0, 1.06, 3.8, 1.22, 1.55, 2.3, 3.2, 1.3, 1.72, 2.0, 1.3, 3.2, 1.26, 3.4, 1.42, 2.7, 1.42, 2.7, 1.2, 4.0, 2.7, 1.42, 1.72, 2.0, 1.13, 5.0, 6.3, 1.08, 1.22, 3.8, 1.85, 1.85, 10.0, 1.02, 1.52, 2.35, 1.22, 3.8, 2.1, 1.65, 1.42, 2.7, 1.32, 3.1, 1.25, 3.5, 5.0, 1.13, 1.38, 2.8, 3.5, 1.25, 1.15, 4.8, 1.35, 2.9, 4.0, 1.2, 1.52, 2.35, 2.4, 1.5, 1.26, 3.4, 4.0, 1.2, 3.2, 1.3, 1.85, 1.85, 2.8, 1.38, 1.5, 2.4, 2.1, 1.65, 1.12, 5.3, 8.0, 1.04, 2.4, 1.5, 1.55, 2.3, 2.1, 1.65, 1.22, 3.8, 1.13, 5.0, 1.38, 2.8, 3.4, 1.26, 3.8, 1.22, 1.9, 1.8, 1.85, 1.85, 3.8, 1.22, 2.4, 1.5, 3.1, 1.32, 1.5, 2.4, 2.1, 1.65, 1.42, 2.7, 3.8, 1.22, 1.38, 2.8, 1.38, 2.8, 2.8, 1.38, 2.8, 1.38, 1.8, 1.9, 4.8, 1.15, 1.55, 2.3, 1.13, 5.0, 4.4, 1.17, 1.2, 4.0, 7.0, 1.06, 1.55, 2.3, 3.8, 1.22, 6.3, 1.08, 2.8, 1.38, 2.7, 1.42, 1.38, 2.8, 1.52, 2.35, 7.0, 1.06, 1.72, 2.0, 1.65, 2.1, 1.72, 2.0, 5.8, 1.1, 1.52, 2.35, 1.1, 5.8, 1.02, 10.0, 1.08, 6.3, 4.0, 1.2, 4.8, 1.15, 2.15, 1.62, 3.4, 1.26]
#print(luckbox_team_name)
#print(luckbox_score)
#print("--------------------------")
luckbox_objs = objectify(luckbox_score, luckbox_team_name, "Luckbox", 0)

#pinnacle_info = pinnacle()
pinnacle_team_name = ['ninjas in pyjamas', 'thundertalk', 'lgd', 'royal never give up', 'oh my god', 'ultra prime', 'weibo', 'invictus', 'jd', 'funplus phoenix', 'lng', 'bilibili', 'ninjas in pyjamas', 'anyones legend', 'we', 'rare atom', 'kabum', 'liberty', 'cincinnati fear', 'liquid first', 'golden guardians chall', 'clg faith', 'liquid chall', 'fly fam', 'tsm chall', 'cloud9 chall', 'flyquest chall', 'wildcard', 'dignitas chall', '100 thieves chall', 'brion chall', 'kt rolster chall', 'rare atom period', 'we academy', 'geng global academy', 'kwangdong f chall', 'ninjas in pyjamas', 'thundertalk', 'ultra prime academy', 'bilibili junior', 'liiv sandbox youth', 'dplus kia chall', 'lgd', 'royal never give up', 'koi', 'g2', 'furia academy', 'los grandes academy', 'red academy', 'fluxo academy', 'kabum academy', 'pain academy', 'intz academy', 'vivo keyd stars academy', 'liberty academy', 'loud academy', 't1 chall', 'drx chall', 'oh my god', 'ultra prime', 'hanwha life chall', 'nongshim rf chall', 'weibo', 'invictus', 'inside games', 'dynamo eclot', 'cryptova', 'esuba', 'forsaken', 'alior bank', 'sampi', 'sinners', 'grypciocraft', 'esca', 'verdant', 'nativz', 'brute', 'entropiq', 'rebels', 'fnatic tq', 'szaty bobra', 'iron wolves', 'mcon', 'northern lions', 'ruddy', 'riddle', 'guasones', 'barca', 'komil and friends', 'exeed', 'benelux united', 'genk', 'uniq', 'nord', 'movistar riders', 'giants', 'illuminar', 'zero tenacity', '7am', 'the agency', 'domino', 'vanir', 'intz academy', 'red academy', 'bisons', 'koi academy', 'zennit', 'heet', 'fluxo academy', 'los grandes academy', 'six karma', 'isurus', 'furia academy', 'vivo keyd stars academy', 'pain academy', 'loud academy', 'estral', 'aze', 'kabum academy', 'liberty academy', 'jd', 'funplus phoenix', 'lng', 'bilibili', 'forsaken', 'esca', 'galakticos', 'besiktas', 'aegis', 'ldlc ol', 'unicorns of love se', 'e wie einfach', 'szaty bobra', 'komil and friends', '5 ronin', 'istanbul wildcats', 'uniq', 'riddle', '3bl', 'anubis', 'valiance', 'diamant', 'bk rog', 'karmine corp', 'gamerlegion', 'eintracht spandau', 'iron wolves', 'grypciocraft', 'dark passage', 'supermassive', 'mcon', 'the agency', 'domino', 'nord', 'fox', 'gng', 'magaza', 'crvena zvezda', 'gameward', 'solary', 'sk prime', 'big', 'zero tenacity', 'alior bank', 'fut', 'nasr', 'northern lions', 'zennit', 'verdant', 'vanir', 'nigma galaxy', 'triple', 'ankora', 'cyber wolves', 'vitalitybee', 'go', 'schalke 04', 'nno prime', 'illuminar', 'exeed', 'genk', 'heet', 'ruddy', 'nativz', 'geekay', 'raad', 'xtremedominators', 'partizan', 'bds academy', 'izi dream', 'mouz', 'eintracht frankfurt', 'benelux united', '7am', 'the kings', 'all knights', 'rainbow7', 'infinity', 'nongshim rf chall', 'kt rolster chall', 'geng global academy', 'dplus kia chall', 'liiv sandbox youth', 'brion chall', 'dark passage', 'nasr', 'ldlc ol', 'izi dream', 'sk prime', 'schalke 04', 'istanbul wildcats', 'besiktas', 'geekay', 'anubis', 'magaza', 'diamant', 'aegis', 'go', 'eintracht frankfurt', 'nno prime', 'barca', 'heretics academy', 'galakticos', 'fut', '3bl', 'gng', 'gameward', 'karmine corp', 'unicorns of love se', 'big', 'rebels', 'movistar riders', '5 ronin', 'supermassive', 'for the win', 'boavista fc', 'fox', 'nigma galaxy', 'valiance', 'partizan', 'bds academy', 'solary', 'mouz', 'gamerlegion', 'guasones', 'koi academy', 'triple', 'raad', 'varona', 'egn', 'cyber wolves', 'crvena zvezda', 'bk rog', 'vitalitybee', 'e wie einfach', 'eintracht frankfurt', 'bisons', 'giants', 'odivelas', 'byteway', 'flyquest', '100 thieves', 'gtz', 'white dragons', 'immortals', 'liquid', 'golden guardians', 'cloud9', 'tsm', 'counter logic', 'dignitas', 'evil geniuses', 'kwangdong f chall', 't1 chall', 'hanwha life chall', 'drx chall', 'ninjas in pyjamas', 'anyones legend', 'we', 'rare atom', 'tsm', 'cloud9', 'dignitas', 'flyquest', 'liquid', '100 thieves', 'golden guardians', 'evil geniuses', 'immortals', 'counter logic', 'dire wolves', 'peace', 'bliss', 'kanga', 'pentanetgg', 'mammoth', 'chiefs', 'ground zero']
pinnacle_team_name = nameStandardize(pinnacle_team_name)
pinnacle_score = [2.39, 1.591, 4.9, 1.185, 1.336, 3.34, 1.467, 2.73, 1.077, 8.83, 1.543, 2.5, 1.293, 3.64, 1.793, 2.05, 12.67, 1.029, 1.465, 12.85, 1.243, 23.14, 1.212, 26.11, 7.8, 1.793, 5.85, 2.07, 2.1, 5.72, 11.4, 1.036, 2.52, 1.485, 1.595, 2.26, 2.39, 1.591, 2.62, 1.452, 4.5, 1.179, 4.9, 1.185, 2.48, 1.552, 2.28, 1.588, 1.248, 3.71, 1.202, 4.18, 3.36, 1.293, 1.925, 1.819, 1.666, 2.13, 1.336, 3.34, 1.526, 2.41, 1.467, 2.73, 6.36, 1.1, 4.7, 1.166, 1.877, 1.862, 2.81, 1.4, 1.134, 5.36, 1.25, 3.69, 5.57, 1.125, 2.04, 1.724, 1.255, 3.64, 1.444, 2.65, 2.81, 1.4, 4.95, 1.152, 1.917, 1.826, 5.7, 1.12, 7.07, 1.083, 1.552, 2.35, 3.3, 1.302, 1.531, 2.4, 2.65, 1.444, 3.96, 1.222, 1.552, 2.35, 2.92, 1.374, 2.19, 1.632, 1.574, 2.3, 2.95, 1.367, 1.869, 1.869, 1.062, 8.41, 1.192, 4.32, 1.077, 8.83, 1.543, 2.5, 1.294, 3.37, 1.724, 2.04, 2.48, 1.5, 1.2, 4.22, 1.165, 4.72, 4.95, 1.152, 8.05, 1.057, 2.13, 1.666, 3.69, 1.25, 1.724, 2.04, 3.41, 1.285, 3.71, 1.247, 3.32, 1.299, 2.48, 1.5, 7.07, 1.077, 1.571, 2.31, 2.74, 1.418, 1.724, 2.04, 1.299, 3.32, 1.277, 3.49, 1.2, 4.22, 1.571, 2.31, 1.444, 2.65, 1.444, 2.65, 8.18, 1.065, 1.869, 1.869, 2.03, 1.729, 1.331, 3.14, 1.142, 5.16, 1.142, 5.17, 1.222, 3.96, 13.77, 1.025, 1.25, 3.69, 1.531, 2.4, 3.12, 1.333, 2.06, 1.709, 1.507, 2.46, 2.79, 1.403, 3.72, 1.246, 1.294, 3.35, 1.751, 2.01, 1.2, 4.22, 1.416, 2.74, 1.42, 2.73, 1.166, 4.7, 3.32, 1.299, 2.48, 1.5, 1.285, 3.41, 2.8, 1.401, 3.32, 1.299, 1.869, 1.869, 1.666, 2.13, 1.25, 3.69, 2.13, 1.666, 9.47, 1.05, 1.125, 5.58, 2.62, 1.454, 3.69, 1.25, 1.869, 1.869, 1.4, 2.81, 3.41, 1.285, 1.943, 1.8, 3.69, 1.25, 2.13, 1.666, 2.65, 1.444, 2.48, 1.5, 1.5, 2.48, 3.12, 1.333, 1.363, 3.18, 1.389, 2.86, 3.01, 1.396, 2.87, 1.431, 1.952, 1.862, 5.18, 1.17, 4.21, 1.2, 1.571, 2.31, 1.293, 3.64, 1.793, 2.05, 3.04, 1.348, 6.64, 1.093, 1.854, 1.884, 2.59, 1.462, 2.75, 1.414, 1.438, 2.52, 1.078, 6.31, 1.023, 11.13, 1.048, 8.0]
#print(pinnacle_team_name)
#print(pinnacle_score)
#print("--------------------------")
pinnacle_objs = objectify(pinnacle_score, pinnacle_team_name, "Pinnacle", len(luckbox_objs) + 1)

#vulkan_info = vulkan()
vulkan_team_names = ['cincinnati fear', 'liquid first', 'golden guardians challengers', 'clg faith', 'flyquest challengers', 'wildcard', 'tsm challengers', 'cloud9 challengers', 'liquid challengers', 'fly fam', 'dignitas challengers', '100 thieves challengers', 'kt rolster challengers', 'fredit brion challengers', 'rare atom period', 'we academy', 'ji jie hao', 'max', 'kwangdong freecs challengers', 'geng global academy', 'ninjas in pyjamas', 'thundertalk']
vulkan_team_names = nameStandardize(vulkan_team_names)
vulkan_scores = [1.58, 7.26, 1.34, 7.68, 5.55, 2.0, 6.72, 1.74, 1.34, 8.34, 2.28, 4.6, 1.06, 7.69, 2.96, 1.37, 2.28, 1.59, 2.1, 1.68, 2.27, 1.59]
#print(vulkan_team_names)
#print(vulkan_scores)
#print("--------------------------")
vulkan_obj = objectify(vulkan_scores, vulkan_team_names, "Vulkan", len(luckbox_objs) + 1 + len(pinnacle_objs))

#ggbet_info = ggbet()
ggbet_team_names = ['lgd', 'royal never give up', 'kt rolster challengers', 'fredit brion challengers', 'sampi', 'esuba', 'six karma', 'isurus', 'grypciocraft', 'esca', 'gamerlegion', 'eintracht frankfurt', 'geekay', 'raad', 'ruddy', 'nativz', 'ankora', 'cyber wolves', 'gameward', 'solary', 'rebels', 'fnatic tq', 'ninjas in pyjamas', 'thundertalk', 'zero tenacity', 'alior bank']
ggbet_team_names = nameStandardize(ggbet_team_names)
ggbet_scores = [1.92, 1.82, 1.01, 17.15, 1.65, 2.15, 1.12, 5.53, 1.05, 8.63, 1.65, 2.15, 1.05, 8.31, 1.03, 9.77, 2.29, 1.58, 1.18, 4.43, 1.26, 3.58, 1.34, 3.12, 1.07, 7.47]
#print(ggbet_team_names)
#print(ggbet_scores)
#print("--------------------------")
ggbet_obj = objectify(ggbet_scores, ggbet_team_names, "ggbet", len(luckbox_objs) + 1 + len(pinnacle_objs) + len(vulkan_scores))

joined = luckbox_objs.union(pinnacle_objs).union(vulkan_obj).union(ggbet_obj)
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

a = processing()
results = a.findArbitrage(list)
print(results)
#a.printOdds()