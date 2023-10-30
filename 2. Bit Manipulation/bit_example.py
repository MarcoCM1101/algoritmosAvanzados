x = 5
y = 7
z = 10

print(f'{x = :08b}')
print(f'{y = :08b}')
print(f'{z = :08b}')

# AND
print(f'{x & y = }')
print(f'{x & z = }')

# OR
print(f'{x | y = }')
print(f'{x | z = }')

# XOR
print(f'{x ^ y = }')
print(f'{x ^ z = }')

# NOT
print(f'{~x = }')

# SHL
print(f'{x << 1 = }')
print(f'{x << 3 = }')

# SHR
print(f'{x >> 1 = }')
print(f'{x >> 3 = }')


def is_even(n: int) -> bool:
    return n & 1 == 0


def is_power_of_2(n: int) -> bool:
    return (n & (n - 1)) == 0


def twos_complement(n: int) -> int:
    return ~n + 1


print(f'{is_even(5) = }')
print(f'{is_even(2342352326) = }')

print(f'{is_power_of_2(8) = }')
print(f'{is_power_of_2(1024) = }')
print(f'{is_power_of_2(666) = }')
print(f'{is_power_of_2(100) = }')
print(f'{is_power_of_2(128) = }')

print(f'{twos_complement(5) = }')
print(f'{twos_complement(-7) = }')

# SWAP EXAMPLES

print()
print('Temporary variable')
x = 5
y = 8
print(f'{x = }, {y = }')
t = x
x = y
y = t
print(f'{x = }, {y = }')

print()
print('Parallel assignment')
x = 5
y = 8
print(f'{x = }, {y = }')
x, y = y, x
print(f'{x = }, {y = }')

print()
print('XOR swap')
x = 5
y = 8
print(f'{x = }, {y = }')
x = x ^ y
y = x ^ y
x = x ^ y
print(f'{x = }, {y = }')


def binary(n: int) -> str:
    if n == 0:
        return '0'
    result = []
    while n:
        result.append(str(n & 1))
        n = n >> 1
    return ''.join(result[::-1])  # reverse binary


print(binary(5))
print(binary(10))
