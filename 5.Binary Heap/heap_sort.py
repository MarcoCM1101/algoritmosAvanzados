from heapq import heappush, heappop


def heap_sort(data: list[int]) -> list[int]:
    result: list[int] = []
    for elem in data:
        heappush(result, elem)
    return [heappop(result) for _ in range(len(result))]


if __name__ == '__main__':
    from pprint import pprint
    pprint(heap_sort([5, 1, 9, 0, 2, 7, 3, 5, 4, 6, 8]))
