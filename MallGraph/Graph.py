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

        self.mall.add_connection("Entrance Hall", "Service Counter")
        self.mall.add_connection("Service Counter", "Rest Area")
        self.mall.add_connection("Rest Area", "Stairs")
        self.mall.add_connection("Elevator", "Stairs")
        self.mall.add_connection("Stairs", "HP")
        self.mall.add_connection("HP", "Apple")
        self.mall.add_connection("Apple", "Dell")
        self.mall.add_connection("Dell", "Samsung")
        self.mall.add_connection("Samsung", "Coridoor 1")
        self.mall.add_connection("Coridoor 1", "Coridoor 2")

        self.mall.add_connection("Dell", "Coridoor 1")
        self.mall.add_connection("Coridoor 2", "MyG")
        self.mall.add_connection("Coridoor 2", "Acer")
        self.mall.add_connection("Stairs", "HP")

        #working till here
        self.mall.add_connection("Coridoor 3", "MyG")
        self.mall.add_connection("Coridoor 3", "Rest Area")
        self.mall.add_connection("Coridoor 2", "Chicking")
        self.mall.add_connection("Rest Area", "Hug A Mug")
        self.mall.add_connection("Service Counter", "KFC")
        self.mall.add_connection("KFC", "Dominos")
        self.mall.add_connection("KFC", "StarBucks")

        self.mall.add_connection("Service Counter", "Dominos")
        self.mall.add_connection("KFC", "McDonalds")
        self.mall.add_connection("Dominos", "McDonalds")
        self.mall.add_connection("StarBucks", "Chickos")
        self.mall.add_connection("McDonalds", "Chickos")
        self.mall.add_connection("Coridoor 4", "StarBucks")
        self.mall.add_connection("Coridoor 4", "Chickos")
        self.mall.add_connection("Coridoor 5", "Coridoor 4")
        self.mall.add_connection("Coridoor 5", "Acer")
        self.mall.add_connection("Coridoor 5", "Chicking")
        self.mall.add_connection("Coridoor 3", "Stairs")











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



