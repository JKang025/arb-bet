# Arb-Bet
This project finds arbitrage opportunities for League of Legends professional e-Sports matches. It takes and compares scores from four different betting websites: Pinnacle Sports, Luckbox, Vulkan Bet, and GGBet. Upon finding an opportunity, it notifies the user of the match and the calculated arb opportunity.

## Usage
### Setup
There are a few packages that this program requires, outlined in the provided requirements.txt.
```
pip3 install requirements.txt
```


To use the auto-email functionality, please enter the your login information by creating a file named credentials.json with the format given in example_credentials.json. 
```
{"sender_email":"YOUREMAIL@gmail.com", "app_password":"YOURAPPPASSWORD"}
```

### Commands
To use this program, simply run
```
python3 main.py
```
There are certain arguments that can be run with the program
```
--gui
--email
--refreshtime day/hour/week/minute
```

### Usecase
By default, the information - such as an arbitrage opportunities - is outputed onto the console. However, if the program is run with the --gui flag, it will open a GUI that displays the relevant information. Furthermore, with the --email flag, the program will send an email containing arbitrage opportunities. The --refreshtime argument can be used to edit how often the program checks for opportunities; although we suspect checking every day will be more than sufficient, considering bets aren't updated frequently.

If you choose to use the email functionality, please enter your own email in utils.py line 114, and enter the email you wish to be notfied with.


## Overview
### Betting odds
There are many types of betting odds; the one that we use for arbitrage opportunity calculations is decimal odds. Let's say I bet on a team and it has odds of 2.5. If that team wins, I get a return of 2.5x the stake that I put in. If I bet $100 on the team, I get $250 returned. (This includes the stake, so I get a net profit of $150.) Other types of odds are common too, such as American odds or fractional odds, but we found that decimal odds were easiest to use.

The probability that a team will win is calculated by $1/\text{decimal odds}$. For example, $1/2.5 = 0.4 = 40%$ chance that this team will win. Notice that as the probability that the team wins decreases, the decimal odd increases.


### Arb betting
The way betting sites generate profit is through manipulating betting odds such that they are stacked slightly in their favor regardless of which team wins or loses. Let's say that there's a 40% chance that a team wins. The reciprocal of this is the decimal odd, which is 2.5. Bettors decrease this number such that if I were to win, I would win less than the probability suggests I should. For example, if this is number is 2.4, my payout is treated as if my team had a 41.67% chance of winning instead of a 40% chance. Ideally, the sum of probabilites of each team winning should be 100%. Bettors decrease the decimal odds such that **the sum of winning probabilities is greater than 100.**

That's where arb betting comes in: we find matchups where the sum of winning probabilities is less than 100%. League of Legends is played by two teams, so this looks like: $$1/\text{decimal odds of Team A} + 1/\text{decimal odds of Team B} < 1$$.

We then bet on both sides, betting different amounts of money for each team such that we either make zero or positive profit regardless of who wins.

## Implementation
### Webscraping
Our webscraping is all done with Selenium. Each website is a little different in terms of how they are scraped because of their uniqueness, which is why we didn’t write a general function for them. For example, some require cookies, others require scrolling towards the bottom to generate more entries, etc. However, they all follow a general sequence:
- Find team names and odds using XPath
- Exclude irrelevant odds, e.g. over/under
- Convert web elements to string and float types and append to arrays for names and teams respectively

### Graph
We store all matchup information in a graph. Each node corresponds to a team, while each edge contains the betting odds and website between the team and another team. Outward facing edges contain the betting odd for the team that the edge is pointing from against the team that the edge is pointing to.

Given that this is Python, this graph is a dictionary. The key is the team and the value is a dictionary; the key for this dictionary is the other team and the value is a list containing the website and odds between the two teams. All in all, each entry in the dictionary looks like:

$$\text{key}:[\text{key},[\text{list}[0], \text{list}[1]]] \rightarrow \text{team-a}: [\text{team-b}, [\text{website}, \text{odds}]]$$

We first initialize this graph with Pinnacle by creating a graph and inputting nodes and edges. For each subsequent website scraper, we see if the graph contains the team. If not, the nodes and edges get initialized in the graph. If so, we see if there are better (higher) odds from the new website compared to the odds in the current graph. If that is true, we replace the odds and calculate if an arbitrage opportunity exists. If it exists, we notify the user.

### Other
Obviously, there are other minor steps along the way. One challenge worth pointing out is the occasional existence of small differences in names for the same team between each website. For this, we tried to “normalize” names as much as possible: that means removing words like “Esports”, stripping strings and converting them to lowercase, etc. After this "normalization," names within a certain similarity threshold were considered the name.

Another set of useful functions we employed are ones that output the graph, website HTMLs, and individual website matchup information to txt files.
