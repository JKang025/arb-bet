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
import time


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
        for i in range(0,len(scores),2):
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
            if(scores_temp[i].text != ''):
                team_names.append(team_names_temp[i].text)
                scores.append(float(scores_temp[i].text))

    # Verify output
    verify_matchups("pinnacle_matchups", team_names, scores)

    # Write output (just for confirmation)
    verify_HTML("pinnacle_HTML", driver.page_source)

    return "Pinnacle", team_names, scores

# Helper – scroll to end of page with (in)finite loading
def auto_scroll(driver):
    import time
    
    pause_time = 3
    height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(pause_time)

        # If curr height is same as prev, don't scroll anymore
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        else: # else: keep scrolling
            height = new_height

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

    # Wait until website loads properly
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="link-to-matches lb-btn btn-color-dark btn-size-medium btn-full-width btn-uppercased"]'))
    )

    match_button = driver.find_element(By.XPATH, '//button[@class="link-to-matches lb-btn btn-color-dark btn-size-medium btn-full-width btn-uppercased"]')

    # Scroll to button to reveal all matches
    driver.execute_script("arguments[0].scrollIntoView(true);", match_button) # for some reason this line overshoots, so scroll back up in next two lines
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,-400)", "")
    time.sleep(3)

    match_button.click()

    # See all matches – first click button that asks to see all matches, then scroll to load
    auto_scroll(driver)

    luckbox_names_temp = driver.find_elements(By.XPATH, '//*[@class="team-name"]' or '//*[@class="draw"]') #draw odds are included here so we can identify/remove them in list of scores
    luckbox_scores_temp = driver.find_elements(By.XPATH, '//*[@class="odds"]') #includes draw odds
    luckbox_names = []
    luckbox_scores = []

    time.sleep(5)

    # Get rid of draw odds. Also save text from elements
    for i in (range(len(luckbox_names_temp))):
        if luckbox_names_temp[i].text != "Draw":
            if(luckbox_scores_temp[i].text != ''):
                luckbox_names.append(luckbox_names_temp[i].text)
                luckbox_scores.append(float(luckbox_scores_temp[i].text))

    verify_matchups("luckbox_matchups", luckbox_names, luckbox_scores)

    # verify HTML output
    verify_HTML("luckbox_HTML", driver.page_source)

    
    return "Luckbox", luckbox_names, luckbox_scores

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

        # not including over/under odds, draw odds, or total odds
        if not (vulkan_title.startswith("over") or vulkan_title.startswith("under") or (any([x in vulkan_title for x in ["Draw", "("]]))):
            semicolon_index = vulkan_title.find(":")
            vulkan_names.append(vulkan_title[:semicolon_index])
            vulkan_scores.append(float(vulkan_temp[i].text))

    verify_matchups("vulkan_matchups", vulkan_names, vulkan_scores)

    # verify HTML output
    verify_HTML("vulkan_HTML", driver.page_source)

    return "Vulkan", vulkan_names, vulkan_scores

################################################
# GGBet
def get_more_links(number):
    link = "https://ggbet.com/en/?page=" + str(number) + "&sportIds[]=esports_league_of_legends"


def ggbet():
    driver = setUp()
    driver.get('https://ggbet.com/en/live?sportIds%5B%5D=esports_league_of_legends')

    # Element contains two nested elements. Check the first to see if it's "winner", i.e. the bet we're looking for
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="market__container___3VAIG"]'))
    )

    ggbet_names = []
    ggbet_scores = []

    ggbet_temp = driver.find_elements(By.XPATH, '//*[@class="market__container___3VAIG"]')
    for element in ggbet_temp:
        header = element.find_element(By.XPATH, './/*[@class="__app-Market-name market__name___2HszL"]') # find element within parent

        if header.text == "Winner": # if header is the correct one for odds (there are three headers)
            try: # some scores are hidden; if that's the case, don't append
                names = element.find_elements(By.XPATH, './/*[@class="oddButton__title___eYYGG"]')
                scores = element.find_elements(By.XPATH, './/*[@class="oddButton__coef___2tokv"]')

                counter = 0
                for score in scores:
                    if not score.text == "-": # if score is not null, append
                        ggbet_scores.append(float(score.text))
                        counter += 1

                if counter == 2:
                    for name in names:
                        ggbet_names.append(name.text)

            except:
                continue
    

    print(len(ggbet_names))
    print(ggbet_names)
    print(len(ggbet_scores))
    print(ggbet_scores)
    
    verify_matchups("ggbet_matchups", ggbet_names, ggbet_scores)

    verify_HTML("ggbet_HTML", driver.page_source)


    return "GGBet", ggbet_names, ggbet_scores


