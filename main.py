from webscraper import luckbox, pinnacle
from webscraper import luckbox
from webscraper import pinnacle
from webscraper import vulkan
from calculations import Graph
from utils import nameProcessing, sendMail
import schedule
import time


def main():
    schedule.every().hour.do(script)
    while True:
        schedule.run_pending()
        time.sleep(60)
    
    luckboxInfo = luckbox()
    luckboxTeamNames = luckboxInfo[0]
    luckboxScores = luckboxInfo[1]
    pinnacleInfo = pinnacle()
    pinnacleTeamNames = pinnacleInfo[0]
    pinnacleScores = pinnacleInfo[1]
    vulkanInfo = vulkan()
    vulkanTeamNames = vulkanInfo[0]
    vulkanScores = vulkanInfo[1]


    g = Graph()
    g.initialize_graph("Pinnacle", pinnacleTeamNames, pinnacleScores)
    # g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
    g.update_graph("Vulkan", vulkanTeamNames, vulkanScores)
    g.output_graph()

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