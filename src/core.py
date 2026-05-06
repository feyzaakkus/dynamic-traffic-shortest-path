from src.models import Graph, Edge
from typing import List, Tuple

def get_traffic_density(time_step: float) -> float:
    """
    TODO: Kişi 2 (Model Lead) burayı Sinüs veya Gaussian dalgası ile dolduracak.
    Dönüş: O anki genel araç yoğunluk oranı.
    """
    return 0.5 

def get_dynamic_cost(edge: Edge, current_time: float, current_traffic_density: float) -> float:
    """
    TODO: Kişi 2 (Model Lead) burayı BPR formülü ile dolduracak.
    """
    return edge.base_time  

def time_dependent_dijkstra(graph: Graph, start_node: str, end_node: str, start_time: float) -> Tuple[List[str], float]:
    """
    TODO:  (Algoritma Lead) burayı Min-Heap kullanarak dolduracak.
    Dönüş: (Gidilen rotadaki düğümlerin listesi, toplam varış süresi)
    """
    return ([], 0.0)