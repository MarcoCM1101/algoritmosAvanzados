# ----------------------------------------------------------
# Lab #2: Ordered Set Class
#
# Date: 20-Sep-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastian González Mora
# ----------------------------------------------------------

from collections import defaultdict
import heapq
from typing import Dict, Set, Tuple, Optional

WeightedGraph = Dict[str, Set[Tuple[str, float]]]


def dijkstra_spt(initial: str, graph: WeightedGraph) -> Tuple[Dict[str, float], Dict[str, Set[Tuple[str, float]]]]:
    distances = {v: float('inf') for v in graph}
    distances[initial] = 0
    unvisited_nodes: list[Tuple[float, str]] = [(0, initial)]
    prev_vertex: Dict[str, Tuple[Optional[str], float]] = {
        v: (None, float('inf')) for v in graph}

    while unvisited_nodes:
        cur_cost, cur_node = heapq.heappop(unvisited_nodes)
        if not cur_cost > distances[cur_node]:
            for neighbor, weight in graph[cur_node]:
                new_cost = distances[cur_node] + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    prev_vertex[neighbor] = (cur_node, weight)
                    heapq.heappush(unvisited_nodes, (new_cost, neighbor))

    tree: WeightedGraph = {v: set() for v in graph}
    for vertex, (prev_v, weight) in prev_vertex.items():
        if prev_v is not None:
            tree[prev_v].add((vertex, weight))
            tree[vertex].add((prev_v, weight))

    return distances, tree


if __name__ == '__main__':
    distances, tree = dijkstra_spt('A', {
        'A': {('B', 5), ('C', 10), ('E', 6)},
        'B': {('A', 5), ('D', 2)},
        'C': {('A', 10), ('D', 1), ('E', 3)},
        'D': {('B', 2), ('C', 1), ('E', 4)},
        'E': {('A', 6), ('C', 3), ('D', 4)},
    })

    print((distances, tree))
