from numpy import arange
import math


def f(x):
    return math.sqrt(x) * math.cos(math.pow(x, 2))


def derivative(x):
    return (math.cos(x ** 2) - 4 * (x ** 2) * math.sin(x ** 2)) / (2 * math.sqrt(x))


def middle_rectangle(h, a, b):
    values = []
    for i in arange(a, b, h / 2):
        values.append(i)
    result = 0
    for xi in values:
        if xi == 1.0:
            continue
        result += f(xi)
    print("Метод средних прямоугольников с h={0}, a={1},b={2}".format(h, a, b))
    print(result * ((b - a) / len(values)))


def eiler(h, a, b):
    values = []
    for i in arange(a, b, h):
        values.append(i)
    summ = 0
    for xi in values:
        if xi == 1.0:
            continue
        summ += f(xi)
    res = (h / 2) * (f(a) + f(b) + 2 * summ) + ((h ** 2) / 12)*(derivative(a) - derivative(b))
    print("Метод эйлера с h={0}, a={1},b={2}".format(h, a, b))
    print(res)


if __name__ == '__main__':
    middle_rectangle(0.1, 1, 2)
    middle_rectangle(0.05, 1, 2)
    middle_rectangle(0.025, 1, 2)
    eiler(0.1, 1, 2)
    eiler(0.05, 1, 2)
    eiler(0.025, 1, 2)
