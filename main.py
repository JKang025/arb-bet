from webscraper import luckbox, pinnacle
from webscraper import luckbox
from webscraper import pinnacle
from webscraper import vulkan
from webscraper import ggbet
from calculations import Graph
from utils import nameStandardize, sendMail, nameProcessing, mapify, objectify
import schedule
import time


def main():
    # schedule.every().hour.do(script)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)

    
    
    ggbetInfo = ggbet()
    # luckboxTeamNames = luckboxInfo[0]
    # luckboxScores = luckboxInfo[1]
    # pinnacleInfo = pinnacle()
    # pinnacleTeamNames = pinnacleInfo[0]
    # pinnacleScores = pinnacleInfo[1]
    # vulkanInfo = vulkan()
    # vulkanTeamNames = vulkanInfo[0]
    # vulkanScores = vulkanInfo[1]

    # temp = temporary()

    # g = Graph()
    # g.initialize_graph("Pinnacle", pinnacleTeamNames, pinnacleScores)
    # g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
    # g.update_graph("Vulkan", vulkanTeamNames, vulkanScores)
    # g.output_graph()

def script():
    try:
        luckboxInfo = luckbox()
        luckboxTeamNames = luckboxInfo[0]
        luckboxTeamNames = nameStandardize(luckboxTeamNames)
        luckboxScores = luckboxInfo[1]
        luckbox_objs = objectify(luckboxScores, luckboxTeamNames, "Luckbox")


        pinnacleInfo = pinnacle()
        pinnacleTeamNames = pinnacleInfo[0]
        pinnacleTeamNames = nameStandardize(pinnacleTeamNames)
        pinnacleScores = pinnacleInfo[1]
        pinnacle_objs = objectify(pinnacleScores, pinnacleTeamNames, "Pinnacle")
        
        joined = luckbox_objs + pinnacle_objs

        the_map = mapify(joined)



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