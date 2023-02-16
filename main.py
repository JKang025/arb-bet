from webscraper import luckbox, pinnacle
from calculations import Graph
from utils import nameProcessing, sendMail
import schedule
import time




def main():
    schedule.every().day.at("12:00").do(script)

    while True:
        schedule.run_pending()
        time.sleep(60)
    

def script():
    luckboxInfo = luckbox()
    luckboxTeamNames = luckboxInfo[0]
    luckboxTeamNames = nameProcessing(luckboxTeamNames)
    luckboxScores = luckboxInfo[1]

    pinnacleInfo = pinnacle()
    pinnacleTeamNames = pinnacleInfo[0]
    pinnacleTeamNames = nameProcessing(pinnacleTeamNames)
    pinnacleScores = pinnacleInfo[1]

    #testarray = ['Kwangdong Freecs', 'Gen.G', 'UOL Sexy Edition', 'NNO Prime', 'Rebels Gaming', 'Team Heretics Academy', 'BK ROG Esports', 'Team BDS Academy', '3BL Esports', "Team RA'AD", 'MOUZ', 'Eintracht Spandau', 'Cyber Wolves', 'Partizan Esports', 'ZennIT', 'BLX UTD', 'Team GO', 'Izi Dream', 'Fox Gaming', 'Anubis Gaming', 'Guasones Team', 'UCAM Tokiers', 'KRC Genk Esports', 'The Agency', 'GamerLegion', 'BIG', 'Giants Gaming', 'Fnatic TQ', 'Odivelas Sports Club', 'Varona Esports', 'Ankora Gaming', 'Valiance', 'GameWard', 'LDLC OL', 'Nigma Galaxy', 'GnG Esports', 'HEET', 'Northern Lions', 'FC Schalke 04', 'Eintracht Frankfurt']
    #print(testarray)
    #print("---------------------------------")
    #testarray = nameProcessing(testarray)
    #print(testarray)


    g = Graph()
    g.initialize_graph("Pinnacle", pinnacleTeamNames, pinnacleScores)
    g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
    g.output_graph()
      
if __name__ == '__main__':
	main()