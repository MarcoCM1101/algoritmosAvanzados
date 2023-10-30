from math import sqrt
from turtle import circle, fd, rt, done

PHI = 1/((sqrt(5) - 1) / 2)


def square():
    for _ in range(4):
        fd(50)
        rt(90)


""" square()
circle(50,90) """


def spiral(n):
    x = 4
    for _ in range(n):
        circle(x, 90)
        x *= PHI


""" spiral(10)
done() """


def print_fibo(n):
    a = 1
    b = 1
    for _ in range(n):
        c = b / a
        print(f'{a:10d}{b:10d}{c:20.15f}')
        a, b = b, a + b


print_fibo(10)
