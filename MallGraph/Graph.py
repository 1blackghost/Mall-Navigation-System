
import networkx as nx

class MallGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_location(self, x, y, z):
        # Add a location node to the graph
        self.graph.add_node((x, y, z))

    def add_connection(self, node1, node2):
        # Add a connection (edge) between two location nodes
        self.graph.add_edge(node1, node2)

    def find_shortest_path(self, start, destination):
        # Find the shortest path between start and destination using Dijkstra's algorithm
        shortest_path = nx.dijkstra_path(self.graph, start, destination)
        return shortest_path


''' 
mall = MallGraph()

mall.add_location(1, 2, 1)
mall.add_location(3, 4, 2)
mall.add_location(5, 6, 3)

mall.add_connection((1, 2, 1), (3, 4, 2))
mall.add_connection((3, 4, 2), (5, 6, 3))

start = (1, 2, 1)
destination = (5, 6, 3)
shortest_path = mall.find_shortest_path(start, destination)
print("Shortest Path:", shortest_path)
'''
