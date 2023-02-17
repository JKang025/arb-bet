from webscraper import luckbox
from webscraper import pinnacle
from webscraper import vulkan
from calculations import Graph


def main():
    luckboxInfo = luckbox()
    luckboxTeamNames = luckboxInfo[0]
    luckboxScores = luckboxInfo[1]
    pinnacleInfo = pinnacle()
    pinnacleTeamNames = pinnacleInfo[0]
    pinnacleScores = pinnacleInfo[1]
    vulkanInfo = vulkan()
    vulkanTeamNames = vulkanInfo[0]
    vulkanScores = vulkanInfo[1]


    g = Graph()
    g.initialize_graph("Pinnacle", pinnacleTeamNames, pinnacleScores)
    # g.update_graph("Luckbox", luckboxTeamNames, luckboxScores)
    g.update_graph("Vulkan", vulkanTeamNames, vulkanScores)
    g.output_graph()

if __name__ == '__main__':
	main()