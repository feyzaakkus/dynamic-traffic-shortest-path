from typing import List, Tuple, Dict

class Edge:
    def __init__(self, u: str, v: str, base_time: float, capacity: int, alpha: float, beta: float):
        self.u = u
        self.v = v
        self.base_time = base_time
        self.capacity = capacity
        self.alpha = alpha
        self.beta = beta

class Graph:
    def __init__(self):
        # Komşuluk listesi: düğüm_adı -> list[(komşu_adı, Edge_objesi)]
        self.adjacency_list: Dict[str, List[Tuple[str, Edge]]] = {}

    def add_node(self, node: str):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, edge: Edge):
        if edge.u not in self.adjacency_list:
            self.add_node(edge.u)
        if edge.v not in self.adjacency_list:
            self.add_node(edge.v)

        self.adjacency_list[edge.u].append((edge.v, edge))
        self.adjacency_list[edge.v].append((edge.u, edge))  # çift yönlü

    def get_neighbors(self, node: str) -> List[Tuple[str, Edge]]:
        return self.adjacency_list.get(node, [])