from webscraper import luckbox, pinnacle, vulkan
from webscraper import luckbox
from webscraper import pinnacle
from webscraper import vulkan
from webscraper import ggbet
from calculations import Graph
from utils import nameStandardize, sendMail, nameProcessing, mapify, objectify
import argparse
import schedule
import time
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", action="store_true", help="include flag to activate the GUI")
    parser.add_argument("--email", action="store_true", help="include flag to send a email")
    parser.add_argument("--refreshtime", default="day", help="choose between 10 minutes, hour, day, and week")

    args = parser.parse_args()
    script(args.gui, args.email)
    
    if(args.refreshtime == "hour"):
        schedule.every(1).hour.do(script, args.gui, args.email)    
    elif(args.refreshtime == "day"):
        schedule.every(1).day.do(script, args.gui, args.email)   
    elif(args.refreshtime == "week"):
        schedule.every(1).week.do(script, args.gui, args.email) 
    elif(args.refreshtime == "minute"):
        schedule.every(10).minute.do(script, args.gui, args.email) 
    else:
        print("please enter hour, day or month for refreshtime. To use the default (day), enter nothing")
        sys.exit(0)
    while True:
        schedule.run_pending()
        time.sleep(1)


def script(gui, email):
    try:
        # gets all relevant infomration
        list_of_obj = []
        counter = 0
        scrapers = [pinnacle, luckbox, vulkan, ggbet]
        for scraper in scrapers: 
            website, names, scores = scraper()
            names = nameStandardize(names)
            list_of_obj = list_of_obj + objectify(scores, names, website, counter)
            counter = counter + len(names)
            print("\n\n\n\n-------------------\nNEW: ", website)

        # parses through the information of matches, standarizes the names
        the_map = mapify(list_of_obj)
        final_list = nameProcessing(the_map)
        
        # does arbitrage calculations and outputs it in both output.txt and console
        g = Graph()
        g.update_graph(final_list)
        g.output_graph("output.txt")
        print(g.list_of_arb_opp)

        if(gui):
             print("does GUI stuff")
        
        if(email):
            if(len(g.list_of_arb_opp) == 0):
                  sendMail("There are no current arbitrage opperunities")
            else:
                result = ""
                for string in g.list_of_arb_opp:
                     result = result + string
                sendMail(result)         
    except:
         print("someting went wrong")
  
      
if __name__ == '__main__':
	main()