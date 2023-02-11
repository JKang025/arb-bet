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

# Get random proxy
with open('dali/http_proxies.txt', 'r') as file:
        proxies = file.readlines()
        rand_proxy = random.choice(proxies)
        print("Random proxy: ", rand_proxy)

options.add_argument(f'--proxy-server=(proxy)')
driver.get('https://www.pinnacle.com/en/esports-hub/league-of-legends/')
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@class="style_price__3ZXqH style_drawPrice__1lAp7"]'))
)


team_names = driver.find_elements(By.XPATH, '//*[@class="style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy"]')
scores = driver.find_elements(By.XPATH, '//*[@class="style_price__3ZXqH style_drawPrice__1lAp7"]')
# print(elements.text)

print(len(team_names))
print(len(scores))


# for e in scores:
#     print(e.text)

# Write output (just for confirmation)
with open("output.txt", "w") as f:
    f.write(driver.page_source)



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