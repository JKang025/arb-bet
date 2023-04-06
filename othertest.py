import webscraper

info = webscraper.ggbet()
name = info[1]
score = info[2]
for i in range(len(name)):
    print(name[i] + " " + str(score[i]))