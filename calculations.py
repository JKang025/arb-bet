

# Team name and website information
class Node:
    def __init__(self, website, scores):
        self.website = website
        self.scores = scores


class Graph:
    def __init__(self):
        self.graph = {}
    # Inserts nodes into graph

    def initialize_node(self, team):
        if team not in self.graph:
            # new_node = Node(website, {})
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
        printed_teams = [] # list of printed teams so if they were visited again, the matchup doesn't get printed again

        with open(file, "w") as f:
            for element in self.graph:
                for neighbor in self.graph[element]:
                    if neighbor not in printed_teams:
                        f.write(element + ", " + self.graph[element][neighbor][0] + ", " + str(self.graph[element][neighbor][1]))
                        f.write("\t - \t")
                        f.write(str(self.graph[neighbor][element][1]) + ", " + self.graph[neighbor][element][0] + ", " + neighbor)
                        f.write("\t : \t")
                        f.write(str(round(1/self.graph[neighbor][element][1] + 1/self.graph[element][neighbor][1],2)))
                        f.write("\n")
                        printed_teams.append(neighbor)


    def update_graph(self, website, team_names, scores):

        arb_opportunities = "" #final string of working arb opportunities. If there are none, return empty string

        for i in range(0, len(team_names), 2):
            team_1 = team_names[i]
            team_2 = team_names[i+1]

             # if either team is not in graph yet, initialize
            if self.initialize_node(team_1) or self.initialize_node(team_2):
                self.initialize_node(team_2)
                # print("Inputting either: ",team_1, ", ", team_2)

            # if both teams are in graphs but don't have matchup against each other
            # note that we only have to check one edge, since either both edges exist or neither
            if team_2 not in self.graph[team_1]:
                self.graph[team_1][team_2] = [website, scores[i]]
                self.graph[team_2][team_1] = [website, scores[i+1]]
                # print("Inputting scores for: ",team_1, ", ", team_2)

            # else: both teams are already in graph
            else:
                old_score_1 = self.graph[team_1][team_2][1]
                old_score_2 = self.graph[team_2][team_1][1]
                
                if scores[i] > old_score_1: #if current odds (scores[i]) < past odds (score_1), replace it
                    self.graph[team_1][team_2][1] = scores[i]
                    self.graph[team_1][team_2][0] = website
                    print("Found lower score")

                if scores[i+1] > old_score_2: #if prev odds > current odds, replace it
                    self.graph[team_2][team_1][1] = scores[i+1]
                    self.graph[team_2][team_1][0] = website
                    print("Found lower score")

                # Arb opportunity!
                arb = 1/old_score_1 + 1/old_score_2
                if arb < 1:
                    print("WORKS")
                    arb_opportunities = team_1 + ", " + str(old_score_1) + " : " + team_2 + ", ", str(old_score_2), " : " + str(arb) + '\n'
                    print(arb_opportunities)
                
                # print(self.graph[team_1].team, ", " , old_score_1, " : ", self.graph[team_2].team, ", ", old_score_2,", ",arb)

        return arb_opportunities