from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

#setup
# driver_path = '/path/to/chromedriver'
# options = Options()
# options.headless = True #headless mode so popup doesn't pop up
# driver = webdriver.Chrome(options=options, executable_path=driver_path)
# driver.get('https://www.pinnacle.com/en/esports-hub/league-of-legends/')
# with open("output.txt", "w") as f:
#     f.write(driver.page_source)




# Finding team names for Pinnacle
# results = [[]]

def read_txt():
    STR = "style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy"

    w = open("names.txt", "w")
    with open("output.txt", "r") as f:

        lines = f.readlines()
        for line in lines:

            # loop to ensure that all instances of STR get read
            index = 0
            while index < len(line):
                index = line.find(STR, index)
                if index == -1:
                    break
                # if found, then search next 200 chars to find name and score.
                # I think a more elegant method can be done w Selenium but it was giving me issues
                index += len(STR)

                index_start = line.find('title="', index) + len('title="')
                index_end = line.find('">', index)

                name = line[index_start:index_end]
                w.write(name + " : " + str(index_start) + " : " + str(index_end) + "\n")
                print(name)

                index = index_end # search for next name

    w.close()

read_txt()


        # if STR in f:
        #     team_1 = "hello"
        #     team_2 = "goodbye"
        #     team_odds = 4 # team 1's odds against team 2

        #     results[team_1].append[team_2]


# Check if arb is profitable
def check_arb(prob_1, prob_2):
    if (1/prob_1 + 1/prob_2 < 1):
        return True

    return False



# def add_team():
#     h_test = driver.find_element("class name", 'style_teamName__24KNG style_teamName__3jTXF ellipsis style_drawTeamName__3xViy')

    

# f.close()

print("working")