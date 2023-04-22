from webscraper import luckbox, pinnacle, vulkan
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

    # Initialize graph with Pinnacle
    website, names, scores = pinnacle()
    g = Graph()
    g.initialize_graph(website, names, scores)

    # Update graph with other scrapers
    scrapers = [luckbox, vulkan, ggbet]
    for scraper in scrapers:
        website, names, scores = scraper()
        print("\n\n\n\n-------------------\nNEW: ", website)
        g.update_graph(website, names, scores)

    # Output graph for verification
    g.output_graph("output.txt")
 
    # luckbox_1 = vulkan()
    
    # ggbetInfo = ggbet()
    # ggbetTeamNames = ggbetInfo[0]
    # ggbetScores = ggbetInfo[1]
    # luckboxTeamNames = luckboxInfo[0]
    # luckboxScores = luckboxInfo[1]
    # pinnacleInfo = pinnacle()
    # pinnacleTeamNames = pinnacleInfo[0]
    # pinnacleScores = pinnacleInfo[1]
    # vulkanInfo = vulkan()
    # vulkanTeamNames = vulkanInfo[0]
    # vulkanScores = vulkanInfo[1]


    # temp = temporary()
    # g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
    # g.update_graph("Vulkan", vulkanTeamNames, vulkanScores)
    # g.update_graph("GGBet", ggbetTeamNames, ggbetScores)


def script():
    try:
        luckbox_info = luckbox()
        luckbox_team_name = luckbox_info[1]
        luckbox_team_name = nameStandardize(luckbox_team_name)
        luckbox_score = luckbox_info[2]
        luckbox_objs = objectify(luckbox_score, luckbox_team_name, "Luckbox", 0)

        pinnacle_info = pinnacle()
        pinnacle_team_name = pinnacle_info[1]
        pinnacle_team_name = nameStandardize(pinnacle_team_name)
        pinnacle_score = pinnacle_info[2]
        pinnacle_objs = objectify(pinnacle_score, pinnacle_team_name, "Pinnacle", len(luckbox_objs) + 1)

        vulkan_info = vulkan()
        vulkan_team_names = vulkan_info[1]
        vulkan_team_names = nameStandardize(vulkan_team_names)
        vulkan_scores = vulkan_info[2]
        vulkan_obj = objectify(vulkan_scores, vulkan_team_names, "Vulkan", len(luckbox_objs) + 1 + len(pinnacle_objs))

        ggbet_info = ggbet()
        ggbet_team_names = ggbet_info[1]
        ggbet_team_names = nameStandardize(ggbet_team_names)
        ggbet_scores = ggbet_info[2]
        ggbet_obj = objectify(ggbet_scores, ggbet_team_names, "ggbet", len(luckbox_objs) + 1 + len(pinnacle_objs) + len(vulkan_scores))

        joined = luckbox_objs.union(pinnacle_objs).union(vulkan_obj).union(ggbet_obj)
        the_map = mapify(joined)
        list = nameProcessing(the_map)

        luckbox_final_name = []
        luckbox_final_score = []
        pin_final_name = []
        pin_final_score = []
        vulkan_final_name = []
        vulkan_final_score = []
        ggbet_final_name = []
        ggbet_final_score = []
        for obj in list:
            if(obj.website == 'Luckbox'):
                luckbox_final_name.append(obj.name)
                luckbox_final_score.append(obj.score)
            elif(obj.website == 'Pinnacle'):
                pin_final_name.append(obj.name)
                pin_final_score.append(obj.score)
            elif(obj.website == 'Vulkan'):
                vulkan_final_name.append(obj.name)
                vulkan_final_score.append(obj.score)
            elif(obj.website == 'ggbet'):
                ggbet_final_name.append(obj.name)
                ggbet_final_score.append(obj.score)

        g = Graph()
        g.initialize_graph("Pinnacle", pin_final_name, pin_final_score)
        results = g.update_graph("Luckbox", luckbox_final_name, luckbox_final_score)
        results = results + g.update_graph("Vulkan", vulkan_final_name, vulkan_final_score)
        results = results + g.update_graph("ggbet", ggbet_final_name, ggbet_final_score)
        if(results != ""):
            sendMail(results)
        else:
            sendMail("there are no arbitrage oppertunities as of now")  
    except:
         print("someting went wrong")

    
      
if __name__ == '__main__':
	main()