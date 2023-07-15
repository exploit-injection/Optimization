import math
from decimal import Decimal, getcontext
getcontext()


def fx(x):
    return (x - 6) * (x - 8) * (x - 4)


def fx_sin(x):
    return x + 6 * Decimal(math.sin(Decimal('2.3') * Decimal('3.14') * x + 4))


def fx_exp(x):
    return 1 - 6 * math.exp(-pow((x - Decimal('6.5')) / 4, 2))


def Dihotom(operation):
    a0 = Decimal(input('Введите начало отрезка: '))
    b0 = Decimal(input('Введите конец отрезка: '))
    epsilon = Decimal(input('Введите точность: '))
    stop = Decimal(50)
    delta = Decimal(epsilon / 2)
    iteration = 1
    result_x = Decimal(0)
    result_fx = Decimal(0)

    while stop >= epsilon:

        print("№ итeрации:", iteration)
        x1 = Decimal(((a0 + b0) / 2) - (delta / 2))
        print("x1 = ", x1)
        x2 = Decimal(((a0 + b0) / 2) + (delta / 2))
        print("x2 = ", x2)
        fx1 = operation(x1)
        print("f(x1) = ", fx1)
        fx2 = operation(x2)
        print("f(x2) = ", fx2)

        if fx1 < fx2:
            b0 = x2
            stop = b0 - a0
        else:
            a0 = x1
            stop = b0 - a0

        if stop < epsilon:
            break

        print("Значение точки останова = ", stop, "\n")

        result_x = (x1 + x2) / 2
        iteration = iteration + 1

        if fx1 < fx2:
            result_fx = fx1
        else:
            result_fx = fx2

    print("\nЗначение точки (x1+x2)/2 = ", result_x)
    print("Минимальное значение функции fx = ", result_fx)
    print("Крайнее значение точки останова = ", stop)
    print("Количество итераций = ", iteration)


if __name__ == "__main__":
    print("\nМетод дихотомии\n")
    Dihotom(fx)
    Dihotom(fx_sin)
    Dihotom(fx_exp)
