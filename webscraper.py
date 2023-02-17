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

# Verify team names, scores, and matchups
def verify_matchups(file, team_names, scores):
    with open(file, "w") as f:
        for i in range(0,len(team_names),2):
            f.write(team_names[i] + ", " + str(scores[i]) + " : " + team_names[i+1] + ", " + str(scores[i+1]) + "\n")

# Verify HTML that was parsed
def verify_HTML(file, HTML):
    with open(file, "w") as f:
        f.write(HTML)


################################################
# From Pinnacle
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
            scores.append(float(scores_temp[i].text))

    # Verify output
    verify_matchups("pinnacle_matchups", team_names, scores)

    # Write output (just for confirmation)
    verify_HTML("pinnacle_HTML", driver.page_source)

    return [team_names, scores]




################################################
# From Luckbox
def luckbox():
    driver = setUp()
    driver.get("https://luckbox.com/?games=league-of-legends")

    # Configure cookies
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-cookiefirst-action="adjust"]'))
    )

    cookie_button = driver.find_element(By.XPATH, '//button[@data-cookiefirst-action="adjust"]')
    cookie_button.click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-cookiefirst-action="save"]'))
    )

    save_button = driver.find_element(By.XPATH, '//button[@data-cookiefirst-action="save"]')
    save_button.click()

    # Get matchups
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="team-name"]'))
    )

    luckbox_names_temp = driver.find_elements(By.XPATH, '//*[@class="team-name"]' or '//*[@class="draw"]') #draw odds are included here so we can identify/remove them in list of scores
    luckbox_scores_temp = driver.find_elements(By.XPATH, '//*[@class="odds"]') #includes draw odds
    luckbox_names = []
    luckbox_scores = []

    import time
    time.sleep(5)

    # Get rid of draw odds. Also save text from elements
    for i in (range(len(luckbox_names_temp))):
        if luckbox_names_temp[i].text != "Draw":
            luckbox_names.append(luckbox_names_temp[i].text)
            luckbox_scores.append(float(luckbox_scores_temp[i].text))

    verify_matchups("luckbox_matchups", luckbox_names, luckbox_scores)

    # verify HTML output
    verify_HTML("luckbox_HTML", driver.page_source)

    
    return [luckbox_names, luckbox_scores]

################################################
# From Vulkan
def vulkan():
    driver = setUp()
    driver.get('https://vulkan.bet/en/esports/league-of-legends')

    # Wait until appropriate elements are loaded
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="__app-Odd-button odd__button___2eiZg"]'))
    )

    vulkan_temp = driver.find_elements(By.XPATH, '//*[@class="__app-Odd-button odd__button___2eiZg"]')
    vulkan_names = []
    vulkan_scores = []

    # Get rid of draw odds. Also save text from elements
    for i in (range(len(vulkan_temp))):
        vulkan_title = vulkan_temp[i].get_attribute("title")

        # not including over/under odds
        if not vulkan_title.startswith("over") and not vulkan_title.startswith("under") and not "(" in vulkan_title:
            semicolon_index = vulkan_title.find(":")
            vulkan_names.append(vulkan_title[:semicolon_index])
            vulkan_scores.append(float(vulkan_temp[i].text))

    verify_matchups("vulkan_matchups", vulkan_names, vulkan_scores)

    # verify HTML output
    verify_HTML("vulkan_HTML", driver.page_source)

    return [vulkan_names, vulkan_scores]
