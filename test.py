from webscraper import luckbox, pinnacle, vulkan
from webscraper import luckbox
from webscraper import pinnacle
from webscraper import vulkan
from webscraper import ggbet
from calculations import Graph
from utils import nameStandardize, sendMail, nameProcessing, mapify, objectify
import schedule
import time

list_of_obj = []
counter = 0




# Output graph for verification
fakename1 = ['jeffrey', 'brian']
fakescore1 = [5.0, 0.2]
fakename2 = ['jeffrey', 'brian']
fakescore2 = [3.0, 0.1]

list_of_obj += objectify(fakescore1, fakename1, "Pinnacle", counter) + objectify(fakescore2, fakename2, "Luckbox", counter + 2)
the_map = mapify(list_of_obj)
final_list = nameProcessing(the_map)
g = Graph()
g.update_graph(final_list)
g.output_graph("output.txt")
print(g.list_of_arb_opp)