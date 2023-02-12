from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import requests
import os
import random

# Setup
driver_path = '/path/to/chromedriver'
options = Options()
options.headless = False #headless mode so popup doesn't pop up
driver = webdriver.Chrome(options=options, executable_path=driver_path)
os.chdir(os.path.dirname(__file__))
print("Directory: ", os.getcwd)

# Get random proxy
with open('http_proxies.txt', 'r') as file:
        proxies = file.readlines()
        rand_proxy = random.choice(proxies)
        print("Random proxy: ", rand_proxy)
options.add_argument(f'--proxy-server=(proxy)')

driver.get('https://www.pinnacle.com/en/esports-hub/league-of-legends/')

# Wait until website loads properly
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@class="style_price__3ZXqH style_drawPrice__1lAp7"]'))
)

# Get elements, output into txt file for validation
team_names_temp = driver.find_elements(By.XPATH, '//*[@class="style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy"]')
scores_temp = driver.find_elements(By.XPATH, '//*[@class="style_price__3ZXqH style_drawPrice__1lAp7"]')
team_names = []
scores = []

# Get rid of draw bets, which have same XPATH. Also save text from elements
for i in (range(len(team_names_temp))):
    if team_names_temp[i].text != "Draw":
        team_names.append(team_names_temp[i].text)
        scores.append(scores_temp[i].text)

# Verify output
with open("names.txt", "w") as f:
    for i in range(0,len(team_names),2):
        f.write(team_names[i] + ", " + scores[i] + " : " + team_names[i+1] + ", " + scores[i+1] + "\n")


# Write output (just for confirmation)
with open("output.txt", "w") as f:
    f.write(driver.page_source)


# -----------------------------------
# GRAPH STUFF
graph = {}

# Team name and website information
class Node:
    def __init__(self, website, scores):
        self.website = website
        self.scores = scores

# Inserts nodes into graph
def initialize_graph(website, team_names, scores):
# website = "Pinnacle"
    for i in range(0, len(team_names), 2):

        team_1 = team_names[i]
        team_2 = team_names[i+1]

        initialize_node(website, team_1)
        initialize_node(website, team_2)

        graph[team_1].scores[team_2] = scores[i] #input odds of team 1 winning against team 2
        graph[team_2].scores[team_1] = scores[i+1]

def initialize_node(website, team):
    if team not in graph:
        new_node = Node(website, {})
        graph[team] = new_node
        return True
    return False


# Prints graph
def output_graph():
    for element in graph:
        print(element, " : ", graph[element].website, " : [", end="")

        for neighbor in graph[element].scores:
            print(neighbor, " - ", graph[element].scores[neighbor], end="")

        print("]")

initialize_graph("Pinnacle", team_names, scores)
output_graph()







# From Luckbox
driver.get("https://luckbox.com/?games=league-of-legends")

# Wait until website loads properly
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@class="team-name"]'))
)

luckbox_names_temp = driver.find_elements(By.XPATH, '//*[@class="team-name"]' or '//*[@class="draw"]') #draw odds are included here so we can identify/remove them in list of scores
luckbox_scores_temp = driver.find_elements(By.XPATH, '//*[@class="odds"]') #includes draw odds
luckbox_names = []
luckbox_scores = []


# Get rid of draw odds. Also save text from elements
for i in (range(len(luckbox_names_temp))):
    if luckbox_names_temp[i].text != "Draw":
        luckbox_names.append(team_names_temp[i].text)
        luckbox_scores.append(scores_temp[i].text)

for i in luckbox_names:
    print(i)


# Parse teamnames and change graph accordingly
for i in range(0,len(luckbox_names),2):
    team_1 = luckbox_names[i]
    team_2 = luckbox_names[i+1]

    # if either team is not in graph yet, initialize
    if initialize_node(team_1) or initialize_node(team_2):
        initialize_node(team_2)

        graph[team_1].scores[team_2] = scores[i] #input odds of team 1 winning against team 2
        graph[team_2].scores[team_1] = scores[i+1]

    # else if both teams are already in the graph. 
    else:
        score_1 = graph[team_1].scores[team_2]
        score_2 = graph[team_2].scores[team_1]

        if luckbox_scores[i] > score_1: #if prev odds > current odds, replace it
            score_1 = luckbox_scores[i]

        if luckbox_scores[i+1] > score_2: #if prev odds > current odds, replace it
            score_2 = luckbox_scores[i+1]

        # Arb opportunity!
        if 1/score_1 + 1/score_2 < 1:
            print("WORKS")


driver.close()
driver.quit()
































def send_request(session, proxy):
   try:
       response = session.get('http://httpbin.org/ip', proxies={'http': f"http://{proxy}"})
       print(response.json())
   except:
       pass



# # if __name__ == "__main__":
# #     with open('list_proxy.txt', 'r') as file:
# #         proxies = file.readlines()

# #         with requests.Session() as session:
# #             for proxy in proxies:
# #                 send_request(session, proxy)







# # Finding team names for Pinnacle
# results = [[]]

# def read_txt():
#     STR = 'style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy'
#     STR_2 = '</span><span class="style_odds__2pux1"><span class="style_price__3ZXqH style_drawPrice__1lAp7">'

#     w = open("names.txt", "w")
#     with open("output.txt", "r") as f:

#         lines = f.readlines()
#         for line in lines:

#             # loop to ensure that all instances of STR get read
#             index = 0
#             names = [] # 2 names, one for each team
#             scores = [] # 2 scores

#             while index < len(line):

#                 for i in range(2):
#                     index = line.find(STR, index)
#                     if index == -1:
#                         break

#                     # if found, then search next chars to find name 
#                     # I think a more elegant method can be done w Selenium but it was giving me issues
#                     index += len(STR)
#                     index_start = line.find('title="', index) + len('title="')
#                     index_end = line.find('">', index)
#                     name = line[index_start:index_end]
#                     names.append(name)

#                     w.write(name + " : " + str(index_start) + " : " + str(index_end) + "\n")

#                     # find score
#                     # index = line.find(STR_2, index)
#                     # if index == -1:
#                     #     break

#                     # index += len(STR_2)
#                     # index_end = line.find('<', index)
#                     # score = int(line[index:index_end])
#                     # scores[i] = score

#                     # w.write(score + " : " + str(index) + " : " + str(index_end) + "\n")
#                     # print("hello\n")

#                     index = index_end # search for next name

#     w.close()

# read_txt()


#         # if STR in f:
#         #     team_1 = "hello"
#         #     team_2 = "goodbye"
#         #     team_odds = 4 # team 1's odds against team 2

#         #     results[team_1].append[team_2]


# # Check if arb is profitable
# def check_arb(prob_1, prob_2):
#     if (1/prob_1 + 1/prob_2 < 1):
#         return True

#     return False



# # def add_team():
# #     h_test = driver.find_element("class name", 'style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy')

    

# # f.close()

# print("working")