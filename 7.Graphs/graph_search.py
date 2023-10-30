from typing import Iterator
from collections import deque

Graph = dict[str, list[str]]

g: Graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['A', 'C', 'E', 'G'],
    'G': ['F']
}


def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            yield current
            stack.extend(graph[current][::-1])
            visited.add(current)


def breadth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    queue: deque[str] = deque()
    visited: set[str] = set()
    queue.append(start)
    while queue:
        current: str = queue.popleft()
        if current not in visited:
            yield current
            queue.extend(graph[current])
            visited.add(current)


if __name__ == '__main__':
    print(f'{list(depth_first_search("A", g)) = }')
    print(f'{list(breadth_first_search("A", g)) = }')
    print(f'{list(depth_first_search("E", g)) = }')
    print(f'{list(breadth_first_search("E", g)) = }')

    # Do an actual search

    target = 'X'
    start = 'G'

    for i, x in enumerate(breadth_first_search(start, g)):
        if x == target:
            print(f'Found {target} in index {i}')
            break
    else:
        print(f'Didn´t find {target}!')
