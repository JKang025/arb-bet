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
    schedule.every().hour.do(script)
    while True:
        schedule.run_pending()
        time.sleep(60)
        

def script():
    try:
        luckbox_info = luckbox()
        luckbox_team_name = luckbox_info[0]
        luckbox_team_name = nameStandardize(luckbox_team_name)
        luckbox_score = luckbox_info[1]
        luckbox_objs = objectify(luckbox_score, luckbox_team_name, "Luckbox")

        pinnacle_info = pinnacle()
        pinnacle_team_name = pinnacle_info[0]
        pinnacle_team_name = nameStandardize(pinnacle_team_name)
        pinnacle_score = pinnacle_info[1]
        pinnacle_objs = objectify(pinnacle_score, pinnacle_team_name, "Pinnacle")
        
        vulkan_info = vulkan()
        vulkan_team_names = vulkan_info[0]
        vulkan_team_names = nameStandardize(vulkan_team_names)
        vulkan_scores = vulkan_info[1]
        vulkan_obj = objectify(vulkan_scores, vulkan_team_names, "Vulkan")

        joined = luckbox_objs + pinnacle_objs + vulkan_obj
        the_map = mapify(joined)
        list = nameProcessing(the_map)

        luckbox_final_name = []
        luckbox_final_score = []
        pin_final_name = []
        pin_final_score = []
        vulkan_final_name = []
        vulkan_final_score = []
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


        g = Graph()
        g.initialize_graph("Pinnacle", pin_final_name, pin_final_score)
        results = g.update_graph("Luckbox", luckbox_final_name, luckbox_final_score)
        results = results + g.update_graph("Vulkan", vulkan_final_name, vulkan_final_score)
        if(results != ""):
            sendMail(results)
        else:
            sendMail("there are no arbitrage oppertunities as of now")  
    except:
         print("someting went wrong")

    
      
if __name__ == '__main__':
	main()