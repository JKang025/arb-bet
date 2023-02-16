

# Team name and website information
class Node:
    def __init__(self, website, scores):
        self.website = website
        self.scores = scores


class Graph:
    def __init__(self):
        self.graph = {}
    # Inserts nodes into graph

    def initialize_node(self, website, team):
        if team not in self.graph:
            new_node = Node(website, {})
            self.graph[team] = new_node
            return True
        return False

    def initialize_graph(self, website, team_names, scores):
    # website = "Pinnacle"
        for i in range(0, len(team_names), 2):

            team_1 = team_names[i]
            team_2 = team_names[i+1]

            self.initialize_node(website, team_1)
            self.initialize_node(website, team_2)

            self.graph[team_1].scores[team_2] = scores[i] #input odds of team 1 winning against team 2
            self.graph[team_2].scores[team_1] = scores[i+1]

    


    # Prints graph
    def output_graph(self):
        for element in self.graph:
            print(element, " : ", self.graph[element].website, " : [", end="")

            for neighbor in self.graph[element].scores:
                print(neighbor, " - ", self.graph[element].scores[neighbor], end="")

            print("]")



    def update_graph(self, website, team_names, scores):

        print(len(team_names))

        for i in range(0, len(team_names), 2):
            team_1 = team_names[i]
            team_2 = team_names[i+1]

            scores[i] = scores[i] #cast as int
            scores[1+1] = scores[i+1]

             # if either team is not in graph yet, initialize
            if self.initialize_node(website, team_1) or self.initialize_node(website, team_2):
                self.initialize_node(website, team_2)

                self.graph[team_1].scores[team_2] = scores[i] #input odds of team 1 winning against team 2
                self.graph[team_2].scores[team_1] = scores[i+1]

                print("New team: ", team_1, " : ", team_2)

            # else: both teams are already in graph
            else:

                # scores are strings, so cast as int
                old_score_1 = self.graph[team_1].scores[team_2]
                old_score_2 = self.graph[team_2].scores[team_1]
                
                if scores[i] > old_score_1: #if current odds (scores[i]) < past odds (score_1), replace it
                    old_score_1 = scores[i]

                if scores[i+1] > old_score_2: #if prev odds > current odds, replace it
                    old_score_2 = scores[i+1]

                # Arb opportunity!
                if 1/old_score_1 + 1/old_score_2 < 1:
                    print("WORKS")

                print("Arb value: ", 1/old_score_1 + 1/old_score_2)



