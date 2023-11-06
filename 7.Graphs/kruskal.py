from heapq import heapify, heappop
from typing import NamedTuple, Optional


WeightedGraph = dict[str, set[tuple[str, int]]]


class Edge(NamedTuple):

    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Edge):
            return (self.weight == other.weight
                    and ((self.u == other.u and self.v == other.v)
                         or (self.u == other.v and self.v == other.u)))
        else:
            return False

    def __hash__(self):
        return hash(self.weight) + hash(self.u) + hash(self.v)


def make_heap(graph: WeightedGraph) -> list[Edge]:
    result: set[Edge] = set()
    u: str
    neighbors: set[tuple[str, int]]
    for u, neighbors in graph.items():
        for neighbor in neighbors:
            v, weight = neighbor
            result.add(Edge(weight, u, v))
    queue: list[Edge] = list(result)
    heapify(queue)
    return queue


if __name__ == '__main__':
    from pprint import pprint
    g1: WeightedGraph = {
        'A': {('B', 4), ('C', 5)},
        'B': {('A', 4)},
        'C': {('A', 5), ('D', 6), ('E', 7)},
        'D': {('C', 6), ('E', 2), ('F', 1)},
        'E': {('C', 7), ('D', 2), ('F', 3)},
        'F': {('D', 1), ('E', 3)}
    }

    e1 = Edge(5, 'A', 'B')
    e2 = Edge(4, 'B', 'A')
    print(e1 == e2)
    print(hash(e1) == hash(e2))
