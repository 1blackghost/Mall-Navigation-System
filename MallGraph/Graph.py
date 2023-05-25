import networkx as nx
from DBMS import datahandler
import string
import random

class MallGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_location(self, name, x, y, z):
        self.graph.add_node(name, pos=(int(x), int(y), int(z)))

    def add_connection(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def find_shortest_path(self, start, destination):
        shortest_path_nodes = nx.dijkstra_path(self.graph, start, destination)
        shortest_path_coordinates = [tuple(self.graph.nodes[node]['pos']) for node in shortest_path_nodes]
        return shortest_path_coordinates

class MakeGraph:
    def __init__(self):
        self.data = datahandler.read_user()
        self.mall = MallGraph()

    def create_connections(self):
        for i in self.data:
            coordinates = eval(i[3])
            self.mall.add_location(str(i[1]), coordinates[0], coordinates[1], coordinates[2])
        self.mall.add_connection("Entrance Hall", "Mall Office")
        self.mall.add_connection("Mall Office", "Data Center")
        self.mall.add_connection("Data Center", "Stairs")
        self.mall.add_connection("Stairs", "Floor 1 RestRoom")
        self.mall.add_connection("Floor 1 RestRoom", "Data Center")

    def find_path(self, start, destination):
        shortest_path = self.mall.find_shortest_path(start, destination)
        return shortest_path


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    generated_strings = set()

    while True:
        random_string = ''.join(random.choice(characters) for _ in range(length))
        if random_string not in generated_strings:
            generated_strings.add(random_string)
            return random_string



