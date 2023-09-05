from webscraper import luckbox, pinnacle, vulkan, ggbet
from calculations import Graph
from utils import nameStandardize, sendMail, nameProcessing, mapify, objectify
import argparse
import schedule
import time
import sys
import json


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
        #scrapers = [luckbox]
        with open('setup.json', 'r') as fp:
            data = json.load(fp)
        if data["print_odds"] == "1":
             to_print = True
        else:
             to_print = False
        for scraper in scrapers: 
            website, names, scores = scraper(to_print)
            
            names = nameStandardize(names)
            list_of_obj = list_of_obj + objectify(scores, names, website, counter)
            counter = counter + len(names)
            print("\n\n\n\n-------------------\n: ", website)
            

        # parses through the information of matches, standarizes the names
        the_map = mapify(list_of_obj)
        final_list = nameProcessing(the_map)
        
        # does arbitrage calculations and outputs it in both output.txt and console
        g = Graph()
        g.update_graph(final_list)
        g.output_graph("output.txt")

        print("Arbitrage opportunities listed below:")
        for op in g.list_of_arb_opp:
             print(op)

        if(gui):
             print("does GUI stuff")
        
        if(email):
            if(len(g.list_of_arb_opp) == 0):
                  sendMail("There are no current arbitrage opportunities")
            else:
                result = ""
                for string in g.list_of_arb_opp:
                     result = result + string
                sendMail(result)         
    except Exception as e:
         print("someting went wrong")
         print(e)
  
      
if __name__ == '__main__':
	main()