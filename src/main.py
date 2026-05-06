from src.models import Graph
from src.core import time_dependent_dijkstra, get_traffic_density
import json

def load_graph_from_json(filepath: str) -> Graph:
    """
    TODO:  (Sistem/Veri Lead) burayı yazacak. 
    JSON'ı parse edip Graph objesi döndürecek.
    """
    return Graph()

def run_simulation():
    """
    TODO:  (Algoritma Lead) simülasyon döngüsünü kuracak.
    """
    print("Simülasyon başlatılıyor...")
    
    # 1. Grafı yükle 
    # my_graph = load_graph_from_json("data/test_scenario.json")
    
    # 2. Döngüyü kur 
    # t = 0
    # while t < 100:
    #     density = get_traffic_density(t)
    #     path, total_time = time_dependent_dijkstra(my_graph, "A", "E", t)
    #     print(f"Time: {t}, Path: {path}, Duration: {total_time}")
    #     t += 10
    
    print("Simülasyon iskeleti hazır.")

if __name__ == "__main__":
    run_simulation()