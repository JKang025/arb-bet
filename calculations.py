

class processing:
    def __init__(self):
        self.arb_opp = ''
        self.odds_map = dict()
    
    def findArbitrage(self, obj_list):
        for i in range(0, len(obj_list), 2):
            team_1 = obj_list[i]
            team_2 = obj_list[i+1]
            match_string = '' # unique string of this matchup of two teams
            if team_1.name > team_2.name:
                match_string = team_1.name + team_2.name # generates match string
            else:
                match_string = team_2.name + team_1.name # generates same match string if teams are in other order
                temp = team_2
                team_2 = team_1
                team_1 = temp
            
            if match_string not in self.odds_map.keys(): # checks if matchstring already entered
                self.odds_map[match_string] = [team_1, team_2]
                arb = (1/team_1.score) + (1/team_2.score) # checks for arb opperunities
                if arb < 1:
                    self.arb_opp = self.arb_opp + team_1.website + " - " + team_1.og_name + " " + str(team_1.score) +" :: " + str(team_2.score) + " " + team_2.og_name + " - " + team_2.website + "||" + str(arb)
            else: # if matchstring already exists
                old_team_1 = self.odds_map[match_string][0]
                old_team_2 = self.odds_map[match_string][1]
                if(old_team_1.score < team_1.score): # inputs best odds into the map
                    self.odds_map[match_string][0] = team_1
                if(old_team_2.score < team_2.score):
                    self.odds_map[match_string][1] = team_2
                arb = (1/self.odds_map[match_string][0].score) + (1/self.odds_map[match_string][1].score) # checks for arb opperunities
                if arb < 1:
                    self.arb_opp = self.arb_opp + self.odds_map[match_string][0].website + " - " + self.odds_map[match_string][0].og_name + " " + str(self.odds_map[match_string][0].score) +" :: " + str(self.odds_map[match_string][1].score) + " " + self.odds_map[match_string][1].og_name + " - " + self.odds_map[match_string][1].website + "||" + str(arb) + "\n"
        return self.arb_opp
    
    def printOdds(self):
        for match in self.odds_map.keys():
            print(str(self.odds_map[match][0]) + str(self.odds_map[match][1]))
