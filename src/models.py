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
        # TODO:  (Sistem/Veri Lead) burayı dolduracak
        pass

    def add_edge(self, edge: Edge):
        # TODO:  (Sistem/Veri Lead) burayı dolduracak
        pass

    def get_neighbors(self, node: str) -> List[Tuple[str, Edge]]:
        # TODO:  (Sistem/Veri Lead) burayı dolduracak
        pass