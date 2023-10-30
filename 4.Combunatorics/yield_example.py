from collections.abc import Iterator


def numbers() -> Iterator[int]:
    x = 1
    yield x
    x *= 3
    yield x
    x += 2
    yield x


def pow2(n: int) -> Iterator[int]:
    i = 0
    while True:
        yield 2 ** i
        i += 1


if __name__ == '__main__':
    g1 = numbers()
    print(f'{next(g1) = }')
    print(f'{next(g1) = }')
    print(f'{next(g1) = }')
    # print(f'{next(g1) = }')
    for w in numbers():
        print(f'{w = }')
    g2 = pow2(5)
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')
    print(f'{next(g2) = }')

    for u in pow2(0):
        print(f'{u = }')
        if u > 1_000_000:
            break
