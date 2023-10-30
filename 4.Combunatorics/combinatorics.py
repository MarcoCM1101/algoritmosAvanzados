# ----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetitions.
#
# Date: 20-Sep-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastian González Mora
# ----------------------------------------------------------

from comparable import C


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [t + [s[-1]] for t in r]
    else:
        return [[]]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:

    def size_and_content(t: list[C]) -> tuple[int, list[C]]:
        return (len(t), t)

    return sorted(s, key=size_and_content)


def combinations(s: list[C], k: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == k]


def insert(x: C, s: list[C], i: int) -> list[C]:
    return s[:i] + [x] + s[i:]


def insert_everywhere(x: C, s: list[C]) -> list[list[C]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        return sum([insert_everywhere(s[0], t)
                    for t in permute(s[1:])],
                   [])
    else:
        return [[]]


def permutations(s: list[C], k: int) -> list[list[C]]:
    return sum([permute(t)
                for t in combinations(s, k)],
               [])


def permutationlist(s, k):
    if k == 0 or not s:
        return [[]]
    else:
        return [t + [j] for j in s for t in permutationlist(s, k - 1)]


def permutations_with_repetition(s, k):
    if not s or k == 0:
        return []
    else:
        return [x for x in permutationlist(s, k) if len(x) == k]


def combinations_with_repetition(s, k):
    if not s or k == 0:
        return []
    res = []
    for x in permutationlist(s, k):
        sorted_x = sorted(x)
        if len(x) == k and sorted_x not in res:
            res.append(sorted_x)
    return res


if __name__ == '__main__':
    from pprint import pprint
    # pprint(sorted_nicely(power_set([1, 2, 3, 4])))
    # print()
    # pprint(sorted_nicely(power_set(['a', 'b', 'c'])))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 3)))
    # pprint(insert_everywhere('a', ['b', 'c', 'd', 'e']))
    pprint(sorted_nicely(permutations(['a', 'b', 'c', 'd'], 3)))
