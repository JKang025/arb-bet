import datetime

# Team name and website information
class Node:
    def __init__(self, website, scores):
        self.website = website
        self.scores = scores


class Graph:
    def __init__(self):
        self.graph = {}
        self.list_of_arb_opp = []
    # Inserts nodes into graph

    def initialize_node(self, team):
        if team not in self.graph:
            self.graph[team] = {}
            return True
        return False

    def initialize_graph(self, website, team_names, scores):
        for i in range(0, len(team_names), 2):

            team_1 = team_names[i]
            team_2 = team_names[i+1]

            self.initialize_node(team_1)
            self.initialize_node(team_2)

            self.graph[team_1][team_2] = [website, scores[i]] #input odds of team 1 winning against team 2
            self.graph[team_2][team_1] = [website, scores[i+1]]

    # Prints graph
    def output_graph(self, file):
        now = datetime.datetime.now()
        current_date_time = now.strftime('%Y-%m-%d %H:%M:%S')
        printed_teams = [] # list of printed teams so if they were visited again, the matchup doesn't get printed again

        with open(file, "a") as f:
            f.write(current_date_time + '\n')
            for element in self.graph:
                for neighbor in self.graph[element]:
                    if neighbor not in printed_teams:
                        f.write(str(self.graph[element][neighbor].og_name) + " - " 
                                + str(self.graph[element][neighbor].score) + " - " 
                                + str(self.graph[element][neighbor].website) + " : " 
                                + str(self.graph[neighbor][element].og_name) + " - " 
                                + str(self.graph[neighbor][element].score) + " - " 
                                + str(self.graph[neighbor][element].website) + " : " 
                                + str(round(1/self.graph[neighbor][element].score + 1/self.graph[element][neighbor].score,2))
                                + '\n')
                        printed_teams.append(neighbor)
            f.write('-----------------------------------------------------------\n')
        
    def update_graph(self, score_objs):

        arb_opportunities = "" #final string of working arb opportunities. If there are none, return empty string

        for i in range(0, len(score_objs), 2):
            team_1 = score_objs[i].name
            team_2 = score_objs[i+1].name

             # if either team is not in graph yet, initialize
            if self.initialize_node(team_1) or self.initialize_node(team_2):
                self.initialize_node(team_2)
                # print("Inputting either: ",team_1, ", ", team_2)

            # if both teams are in graphs but don't have matchup against each other
            # note that we only have to check one edge, since either both edges exist or neither
            if team_2 not in self.graph[team_1]:
                self.graph[team_1][team_2] = score_objs[i]
                self.graph[team_2][team_1] = score_objs[i+1]

            # else: both teams are already in graph
            else:
                old_score_1 = self.graph[team_1][team_2]
                old_score_2 = self.graph[team_2][team_1]
                
                if score_objs[i].score > old_score_1.score: #if current odds (scores[i]) < past odds (score_1), replace it
                    self.graph[team_1][team_2] = score_objs[i]
                    old_score_1 = score_objs[i]

                if score_objs[i+1].score > old_score_2.score: #if prev odds > current odds, replace it
                    self.graph[team_2][team_1] = score_objs[i+1]
                    old_score_2 = score_objs[i + 1]

                # Arb opportunity!
                arb = 1/old_score_1.score + 1/old_score_2.score
                if arb < 1 and arb > 0.95:
                    arb_opportunities = str(old_score_1.og_name) + " - " + str(old_score_1.score) + " - " + str(old_score_1.website) + " : " + str(old_score_2.og_name) + " - " + str(old_score_2.score) + " - " + str(old_score_2.website) + " : " + str(arb)
                    self.list_of_arb_opp.append(str(arb_opportunities))
                

        return arb_opportunities