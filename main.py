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

    list_of_obj = []
    counter = 0
    scrapers = [pinnacle, luckbox, vulkan, ggbet]
    for scraper in scrapers:
        website, names, scores = scraper()
        names = nameStandardize(names)
        list_of_obj = list_of_obj + objectify(scores, names, website, counter)
        counter = counter + len(names)
        print("JEFFREY " + website)
        print(names)
        print(scores)
        print("JEFFREY END")
        print("\n\n\n\n-------------------\nNEW: ", website)

    the_map = mapify(list_of_obj)
    final_list = nameProcessing(the_map)
    g = Graph()
    g.update_graph(final_list)
    g.output_graph("output.txt")
    print(g.list_of_arb_opp)

def script():
    try:
        print('bruh')
    except:
         print("someting went wrong")
  
      
if __name__ == '__main__':
	main()