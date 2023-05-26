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

        #floor 2

        self.mall.add_connection("Stairs Floor 2", "Stairs")
        self.mall.add_connection("RestArea Floor 2", "Stairs Floor 2")
        self.mall.add_connection("Mall Office Floor 2", "RestArea Floor 2")
        self.mall.add_connection("RestArea Floor 2", "Gucci")
        self.mall.add_connection("Stairs Floor 2", "Gucci")
        self.mall.add_connection("Rollex", "Gucci")
        self.mall.add_connection("Rollex", "Rado")
        self.mall.add_connection("Rado", "Oris")
        self.mall.add_connection("Corridor 6", "Oris")
        self.mall.add_connection("Corridor 6", "Rollex")
        self.mall.add_connection("Gucci", "Corridor 6")
        self.mall.add_connection("Corridor 6", "Titan")
        self.mall.add_connection("Corridor 6", "Titan")
        self.mall.add_connection("Titan", "Fastrack")
        #working till here
        self.mall.add_connection("Fastrack", "Corridor 7")
        self.mall.add_connection("RestArea Floor 2", "Corridor 7")
        self.mall.add_connection("MI", "Corridor 7")
        self.mall.add_connection("Corridor 7", "Mall Office Floor 2")
        self.mall.add_connection("Corridor 8", "Corridor 7")
        self.mall.add_connection("Corridor 8", "Floor 2 RestRoom")
        self.mall.add_connection("Corridor 8", "Sony")
        self.mall.add_connection("Corridor 8", "Corridor 9")
        self.mall.add_connection("Corridor 9", "Sony")
        self.mall.add_connection("Corridor 9", "Floor 2 RestRoom")
        self.mall.add_connection("Corridor 9", "VGuard")
        self.mall.add_connection("Corridor 9", "Corridor 10")
        self.mall.add_connection("Corridor 10", "Fastrack")

        self.mall.add_connection("Corridor 10", "MI")
        self.mall.add_connection("Corridor 10", "Panasonic")
        self.mall.add_connection("Corridor 7", "Corridor 10")
        #working till here
        self.mall.add_connection("Stairs Floor 2", "Stairs Floor 3")
        self.mall.add_connection("Stairs Floor 3", "Puma")
        self.mall.add_connection("Stairs Floor 3", "Louis Phillipie")
        self.mall.add_connection("Stairs Floor 3", "Addidas")
        self.mall.add_connection("Stairs Floor 3", "Trends")
        self.mall.add_connection("Trends", "Puma")
        self.mall.add_connection("Corridor 11", "Trends")
        self.mall.add_connection("Corridor 11", "Puma")
        self.mall.add_connection("Corridor 11", "Stairs Floor 3")
        self.mall.add_connection("Corridor 11", "Jockey")
        self.mall.add_connection("Corridor 12", "Bata")
        self.mall.add_connection("Corridor 12", "US POLO")
        self.mall.add_connection("Corridor 12", "Trends")
        self.mall.add_connection("US POLO", "Trends")































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



