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


def setUp():
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
    return driver

def pinnacle():
    driver = setUp()

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
    return [team_names, scores]




################################################
# From Luckbox
def luckbox():
    driver = setUp()
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
            luckbox_names.append(luckbox_names_temp[i].text)
            luckbox_scores.append( luckbox_scores_temp[i].text)

    for i in luckbox_names:
        print(i)
    
    return [luckbox_names, luckbox_scores]