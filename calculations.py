

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

