from webscraper import luckbox, pinnacle
from calculations import Graph
from utils import nameProcessing, sendMail
import schedule
import time


def main():
    schedule.every().hour.do(script)
    while True:
        schedule.run_pending()
        time.sleep(60)
    

def script():
    try:
        luckboxInfo = luckbox()
        luckboxTeamNames = luckboxInfo[0]
        luckboxTeamNames = nameProcessing(luckboxTeamNames)
        luckboxScores = luckboxInfo[1]

        pinnacleInfo = pinnacle()
        pinnacleTeamNames = pinnacleInfo[0]
        pinnacleTeamNames = nameProcessing(pinnacleTeamNames)
        pinnacleScores = pinnacleInfo[1]


        g = Graph()
        g.initialize_graph("Pinnacle", pinnacleTeamNames, pinnacleScores)
        results = g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
        if(results != ""):
            sendMail(results)
        else:
            sendMail("there are no arbitrage oppertunities as of now")  
    except:
         print("someting went wrong")

    
      
if __name__ == '__main__':
	main()