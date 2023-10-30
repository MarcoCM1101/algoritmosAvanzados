# ----------------------------------------------------------
# Lab #2: Ordered Set Class
#
# Date: 20-Sep-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastian González Mora
# ----------------------------------------------------------

from __future__ import annotations
from typing import Generic, TypeVar
from collections.abc import Iterator, Iterable

T = TypeVar('T')
IT = TypeVar('IT')


class OrderedSet(Generic[T]):

    class __Iterator(Generic[IT]):

        __data: list[IT]
        __current: int

        def __init__(self, values: list[IT]) -> None:
            self.__data = values
            self.__current = 0

        def __iter__(self) -> Iterator[IT]:
            return self

        def __next__(self) -> IT:
            if self.__current < len(self.__data):
                result = self.__data[self.__current]
                self.__current += 1
                return result
            else:
                raise StopIteration

    __data: list[T]

    def __init__(self, values: Iterable[T] = []) -> None:
        self.__data = []
        for elem in values:
            self.add(elem)

    def add(self, value: T) -> None:
        if value not in self.__data:
            self.__data.append(value)

    def __repr__(self) -> str:
        return f'OrderedSet({"" if len(self) == 0 else self.__data})'

    def __len__(self) -> int:
        return len(self.__data)

    def __contains__(self, value: T) -> bool:
        return value in self.__data

    def __iter__(self) -> Iterator[T]:
        return OrderedSet.__Iterator(self.__data)

    def discard(self, value: T) -> None:
        for (index, elem) in enumerate(self):
            if elem == value:
                del self.__data[index]
                return

    def __eq__(self, other: object) -> bool:
        if isinstance(other, OrderedSet) and len(self) == len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True
        else:
            return False

    def __le__(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem not in other:
                return False
        return True

    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    def remove(self, value: T) -> None:
        try:
            index = self.__data.index(value)
            self.__data.pop(index)
        except ValueError:
            raise KeyError(f"{value} not found in OrderedSet")

    def __lt__(self, other: OrderedSet[T]) -> bool:
        lt = len(self) < len(other) and all(elem in other for elem in self)
        return lt

    def __ge__(self, other: OrderedSet[T]) -> bool:
        ge = len(self) > len(other) or self == other
        return ge

    def __gt__(self, other: OrderedSet[T]) -> bool:
        gt = len(self) != len(other) and other < self
        return gt

    def isdisjoint(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem in other:
                return False
        return True

    def __or__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result = OrderedSet(self)
        for elem in other:
            if elem not in result:
                result.add(elem)
        return result

    def __sub__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result

    def __xor__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result = OrderedSet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result

    def clear(self) -> None:
        self.__data = []

    def pop(self) -> T:
        if not self.__data:
            raise KeyError("OrderedSet is empty")
        return self.__data.pop()


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    a.add(5)
    a.add(7)
    a.add(5)
    print(f'{a = }')
    print(f'{len(a) = }')
    b: OrderedSet[str] = OrderedSet(['a', 'b', 'c', 'a'])
    print(f'{b = }')
    print(f'{len(b) = }')
    print(f'{5 in a = }')
    print(f'{10 in a = }')
    print(f'{"b" in b = }')
    print(f'{"x" in b = }')

    it = iter([4, 8, 15, 16, 23, 42])
    print(f'{it = }')
    try:
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
    except StopIteration:
        print('No more elements to iterate over')

    b_it = iter(b)
    try:
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
    except StopIteration:
        print('stop')

    for x in b:
        print(f'{x = }')

    print()

    new_iter = iter(b)
    try:
        while True:
            x = next(new_iter)
            print(f'{x = }')
    except StopIteration:
        ...

    d = OrderedSet(b)
    e = OrderedSet('hello')
    print(f'{d = }')
    print(f'{e = }')
